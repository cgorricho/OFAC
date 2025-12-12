"""Screening endpoints for single and batch entity screening."""

import io
import time
from datetime import UTC, datetime
from uuid import uuid4

import pandas as pd
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status

from ofac.api.deps import get_matcher
from ofac.api.schemas import SingleScreeningRequest, SingleScreeningResponse
from ofac.core.models import BatchScreeningResponse
from ofac.core.classifier import classify_screening_result
from ofac.core.config import settings
from ofac.core.exceptions import FileFormatError, FileParseError, FileTooLargeError
from ofac.core.matcher import EntityMatcher
from ofac.core.models import EntityInput, MatchStatus, ScreeningResult

router = APIRouter(prefix="/screenings", tags=["Screening"])


@router.post("/single", response_model=SingleScreeningResponse)
async def screen_single_entity(
    request: SingleScreeningRequest,
    matcher: EntityMatcher = Depends(get_matcher),
) -> SingleScreeningResponse:
    """Screen a single entity against OFAC lists.

    Args:
        request: SingleScreeningRequest with entity details.
        matcher: EntityMatcher instance (injected).

    Returns:
        SingleScreeningResponse with screening results and metadata.

    Raises:
        HTTPException: If screening fails or OFAC data not available.
    """
    start_time = time.time()

    try:
        # Convert request to EntityInput
        entity_input = request.to_entity_input()

        # Perform matching
        matches = matcher.match(
            entity_name=entity_input.entity_name,
            country=entity_input.country,
            max_results=10,
        )

        # Classify result (OK/REVIEW/NOK)
        highest_score = matches[0].match_score if matches else 0
        match_status = classify_screening_result(highest_score, matches)

        # Get OFAC version
        ofac_version = matcher.data.version.loaded_at or "unknown"

        # Create screening result
        screening_result = ScreeningResult(
            entity_input=entity_input,
            match_status=match_status,
            matches=matches,
            highest_score=highest_score,
            ofac_version=ofac_version,
            timestamp=datetime.now(UTC),
        )

        # Calculate duration
        duration_ms = int((time.time() - start_time) * 1000)

        return SingleScreeningResponse(
            data=screening_result,
            meta={
                "ofac_version": ofac_version,
                "duration_ms": duration_ms,
            },
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "code": "SCREENING_ERROR",
                "message": f"Screening failed: {str(e)}",
            },
        ) from e


def _parse_uploaded_file(file: UploadFile) -> pd.DataFrame:
    """Parse uploaded Excel or CSV file.

    Args:
        file: Uploaded file from FastAPI.

    Returns:
        DataFrame with parsed file contents.

    Raises:
        FileFormatError: If file format is not supported.
        FileParseError: If file cannot be parsed.
        FileTooLargeError: If file exceeds max size.
    """
    # Check file size
    file_content = file.file.read()
    file_size_mb = len(file_content) / (1024 * 1024)
    max_size_mb = 10  # 10MB limit

    if file_size_mb > max_size_mb:
        raise FileTooLargeError(
            f"File size ({file_size_mb:.2f}MB) exceeds maximum ({max_size_mb}MB)",
            details={"file_size_mb": file_size_mb, "max_size_mb": max_size_mb},
        )

    # Reset file pointer
    file.file.seek(0)

    # Determine file type
    filename = file.filename or ""
    file_ext = filename.split(".")[-1].lower() if "." in filename else ""

    try:
        if file_ext in ["xlsx", "xls"]:
            df = pd.read_excel(io.BytesIO(file_content), engine="openpyxl")
        elif file_ext == "csv":
            df = pd.read_csv(io.BytesIO(file_content), encoding="utf-8")
        else:
            raise FileFormatError(
                f"Unsupported file format: {file_ext}. Supported: xlsx, xls, csv",
                details={"filename": filename, "extension": file_ext},
            )

        # Check row count
        if len(df) > settings.max_file_rows:
            raise FileTooLargeError(
                f"File has {len(df)} rows, exceeds maximum {settings.max_file_rows}",
                details={"row_count": len(df), "max_rows": settings.max_file_rows},
            )

        return df

    except FileFormatError:
        raise
    except FileTooLargeError:
        raise
    except Exception as e:
        raise FileParseError(
            f"Failed to parse file: {str(e)}",
            details={"filename": filename, "error": str(e)},
        ) from e


def _detect_name_column(df: pd.DataFrame) -> str | None:
    """Auto-detect entity name column.

    Args:
        df: DataFrame to search.

    Returns:
        Column name if found, None otherwise.
    """
    name_patterns = [
        "name",
        "organization",
        "entity",
        "partner",
        "beneficiary",
        "org",
        "company",
    ]

    for col in df.columns:
        col_lower = str(col).lower()
        for pattern in name_patterns:
            if pattern in col_lower:
                return col

    return None


@router.post("/batch", response_model=BatchScreeningResponse)
async def screen_batch(
    file: UploadFile = File(...),
    matcher: EntityMatcher = Depends(get_matcher),
) -> BatchScreeningResponse:
    """Screen multiple entities from uploaded file.

    Args:
        file: Uploaded Excel or CSV file.
        matcher: EntityMatcher instance (injected).

    Returns:
        BatchScreeningResponse with results for all entities.

    Raises:
        HTTPException: If file processing or screening fails.
    """
    start_time = time.time()
    screening_id = str(uuid4())

    try:
        # Parse file
        df = _parse_uploaded_file(file)

        # Auto-detect name column
        name_column = _detect_name_column(df)
        if not name_column:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "code": "FILE_COLUMN_MAPPING_ERROR",
                    "message": "Could not auto-detect entity name column. Available columns: "
                    + ", ".join(df.columns.tolist()),
                    "available_columns": df.columns.tolist(),
                },
            )

        # Process each row
        results: list[ScreeningResult] = []
        ok_count = 0
        review_count = 0
        nok_count = 0

        for _, row in df.iterrows():
            entity_name = str(row[name_column]).strip()
            if not entity_name or entity_name == "nan":
                continue

            # Extract optional fields
            country = None
            description = None

            # Try to find country column
            country_patterns = ["country", "nation", "location"]
            for col in df.columns:
                if any(pattern in str(col).lower() for pattern in country_patterns):
                    country_val = row.get(col)
                    if pd.notna(country_val):
                        country = str(country_val).strip()

            # Try to find description column
            desc_patterns = ["description", "project", "notes", "remarks"]
            for col in df.columns:
                if any(pattern in str(col).lower() for pattern in desc_patterns):
                    desc_val = row.get(col)
                    if pd.notna(desc_val):
                        description = str(desc_val).strip()

            # Create entity input
            entity_input = EntityInput(
                entity_name=entity_name,
                country=country,
                description=description,
            )

            # Perform matching
            matches = matcher.match(
                entity_name=entity_input.entity_name,
                country=entity_input.country,
                max_results=10,
            )

            # Classify result
            highest_score = matches[0].match_score if matches else 0
            match_status = classify_screening_result(highest_score, matches)

            # Count by status
            if match_status == MatchStatus.OK:
                ok_count += 1
            elif match_status == MatchStatus.REVIEW:
                review_count += 1
            elif match_status == MatchStatus.NOK:
                nok_count += 1

            # Create screening result
            ofac_version = matcher.data.version.loaded_at or "unknown"
            screening_result = ScreeningResult(
                screening_id=screening_id,
                entity_input=entity_input,
                match_status=match_status,
                matches=matches,
                highest_score=highest_score,
                ofac_version=ofac_version,
                timestamp=datetime.now(UTC),
            )
            results.append(screening_result)

        # Calculate duration
        duration_ms = int((time.time() - start_time) * 1000)
        ofac_version = matcher.data.version.loaded_at or "unknown"

        return BatchScreeningResponse(
            results=results,
            total_screened=len(results),
            ok_count=ok_count,
            review_count=review_count,
            nok_count=nok_count,
            ofac_version=ofac_version,
            processing_time_ms=duration_ms,
        )

    except HTTPException:
        raise
    except FileFormatError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "code": e.code,
                "message": str(e),
                "details": e.details,
            },
        ) from e
    except FileTooLargeError as e:
        raise HTTPException(
            status_code=status.HTTP_413_CONTENT_TOO_LARGE,
            detail={
                "code": e.code,
                "message": str(e),
                "details": e.details,
            },
        ) from e
    except FileParseError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "code": e.code,
                "message": str(e),
                "details": e.details,
            },
        ) from e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "code": "SCREENING_ERROR",
                "message": f"Batch screening failed: {str(e)}",
            },
        ) from e


__all__ = ["router"]

