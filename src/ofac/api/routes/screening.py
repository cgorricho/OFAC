"""Screening endpoints for single and batch entity screening."""

import time
from datetime import UTC, datetime
from uuid import uuid4

import pandas as pd
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status

from ofac.api.deps import get_matcher
from ofac.api.schemas import SingleScreeningRequest, SingleScreeningResponse
from ofac.core.classifier import classify_with_gl_context
from ofac.core.exceptions import (
    ColumnMappingError,
    FileFormatError,
    FileParseError,
    FileTooLargeError,
)
from ofac.core.file_parser import detect_columns, parse_file
from ofac.core.matcher import EntityMatcher
from ofac.core.models import (
    BatchScreeningResponse,
    EntityInput,
    MatchStatus,
    ScreeningResult,
)

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

        # Classify result with GL context (OK/REVIEW/NOK)
        highest_score = matches[0].match_score if matches else 0
        match_status, is_humanitarian, gl_note = classify_with_gl_context(
            highest_score=highest_score,
            matches=matches,
            entity_country=entity_input.country,
            description=entity_input.description,
        )

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
            humanitarian_flag=is_humanitarian,
            general_license_note=gl_note,
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
        # Read file content
        file_content = await file.read()
        filename = file.filename or "uploaded_file"

        # Parse file
        df = parse_file(file_content, filename)

        # Detect columns
        column_mapping = detect_columns(df)

        # Process each row
        results: list[ScreeningResult] = []
        ok_count = 0
        review_count = 0
        nok_count = 0

        for _, row in df.iterrows():
            entity_name = str(row[column_mapping.entity_name_column]).strip()
            if not entity_name or entity_name == "nan":
                continue

            # Extract optional fields
            country = None
            if column_mapping.country_column:
                country_val = row.get(column_mapping.country_column)
                if pd.notna(country_val):
                    country = str(country_val).strip()

            description = None
            if column_mapping.description_column:
                desc_val = row.get(column_mapping.description_column)
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

            # Classify result with GL context
            highest_score = matches[0].match_score if matches else 0
            match_status, is_humanitarian, gl_note = classify_with_gl_context(
                highest_score=highest_score,
                matches=matches,
                entity_country=entity_input.country,
                description=entity_input.description,
            )

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
                humanitarian_flag=is_humanitarian,
                general_license_note=gl_note,
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
    except ColumnMappingError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "code": e.code,
                "message": str(e),
                "details": e.details,
            },
        ) from e
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
