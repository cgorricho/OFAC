"""File parsing and column detection utilities.

This module provides utilities for:
- Parsing Excel and CSV files
- Auto-detecting relevant columns (name, country, description)
- Creating column mappings

Usage:
    from ofac.core.file_parser import parse_file, detect_columns

    df, mapping = parse_file(uploaded_file)
    name_col = mapping.entity_name_column
"""

import io
from typing import NamedTuple

import pandas as pd

from ofac.core.config import settings
from ofac.core.exceptions import FileFormatError, FileParseError, FileTooLargeError


class ColumnMapping(NamedTuple):
    """Column mapping for uploaded file.

    Attributes:
        entity_name_column: Column name for entity names (required)
        country_column: Column name for countries (optional)
        description_column: Column name for descriptions (optional)
        all_columns: List of all column names in file
    """

    entity_name_column: str
    country_column: str | None
    description_column: str | None
    all_columns: list[str]


def parse_file(file_content: bytes, filename: str) -> pd.DataFrame:
    """Parse uploaded Excel or CSV file.

    Args:
        file_content: File content as bytes.
        filename: Original filename (for extension detection).

    Returns:
        DataFrame with parsed file contents.

    Raises:
        FileFormatError: If file format is not supported.
        FileParseError: If file cannot be parsed.
        FileTooLargeError: If file exceeds max size.
    """
    # Check file size
    file_size_mb = len(file_content) / (1024 * 1024)
    max_size_mb = 10  # 10MB limit

    if file_size_mb > max_size_mb:
        raise FileTooLargeError(
            f"File size ({file_size_mb:.2f}MB) exceeds maximum ({max_size_mb}MB)",
            details={"file_size_mb": file_size_mb, "max_size_mb": max_size_mb},
        )

    # Determine file type
    file_ext = filename.split(".")[-1].lower() if "." in filename else ""

    try:
        if file_ext in ["xlsx", "xls"]:
            df = pd.read_excel(io.BytesIO(file_content), engine="openpyxl")
        elif file_ext == "csv":
            # Try UTF-8 first, fallback to Latin-1
            try:
                df = pd.read_csv(io.BytesIO(file_content), encoding="utf-8")
            except UnicodeDecodeError:
                df = pd.read_csv(io.BytesIO(file_content), encoding="latin-1")
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

        # Remove completely empty rows
        df = df.dropna(how="all")

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


def detect_columns(df: pd.DataFrame) -> ColumnMapping:
    """Auto-detect relevant columns in DataFrame.

    Detects:
    - Entity name column (required)
    - Country column (optional)
    - Description column (optional)

    Args:
        df: DataFrame to analyze.

    Returns:
        ColumnMapping with detected columns.

    Raises:
        ColumnMappingError: If entity name column cannot be detected.
    """
    from ofac.core.exceptions import ColumnMappingError

    # Name column patterns (priority order)
    name_patterns = [
        "name",
        "organization",
        "entity",
        "partner",
        "beneficiary",
        "org",
        "company",
        "institution",
    ]

    # Country column patterns
    country_patterns = ["country", "nation", "location", "region"]

    # Description column patterns
    desc_patterns = ["description", "project", "notes", "remarks", "comment"]

    entity_name_column: str | None = None
    country_column: str | None = None
    description_column: str | None = None

    # Detect entity name column
    for col in df.columns:
        col_lower = str(col).lower()
        for pattern in name_patterns:
            if pattern in col_lower:
                entity_name_column = col
                break
        if entity_name_column:
            break

    # Detect country column
    for col in df.columns:
        if col == entity_name_column:
            continue
        col_lower = str(col).lower()
        for pattern in country_patterns:
            if pattern in col_lower:
                country_column = col
                break
        if country_column:
            break

    # Detect description column
    for col in df.columns:
        if col in [entity_name_column, country_column]:
            continue
        col_lower = str(col).lower()
        for pattern in desc_patterns:
            if pattern in col_lower:
                description_column = col
                break
        if description_column:
            break

    # Entity name column is required
    if not entity_name_column:
        raise ColumnMappingError(
            "Could not auto-detect entity name column",
            details={"available_columns": df.columns.tolist()},
        )

    return ColumnMapping(
        entity_name_column=entity_name_column,
        country_column=country_column,
        description_column=description_column,
        all_columns=df.columns.tolist(),
    )


def get_column_suggestions(df: pd.DataFrame) -> dict[str, list[str]]:
    """Get column mapping suggestions without raising errors.

    Returns all available columns organized by type for manual selection.

    Args:
        df: DataFrame to analyze.

    Returns:
        Dict with suggested columns by type:
        {
            "name_candidates": [...],
            "country_candidates": [...],
            "description_candidates": [...],
            "all_columns": [...]
        }
    """
    name_patterns = ["name", "organization", "entity", "partner", "beneficiary"]
    country_patterns = ["country", "nation", "location"]
    desc_patterns = ["description", "project", "notes"]

    name_candidates: list[str] = []
    country_candidates: list[str] = []
    desc_candidates: list[str] = []

    for col in df.columns:
        col_lower = str(col).lower()
        if any(pattern in col_lower for pattern in name_patterns):
            name_candidates.append(col)
        elif any(pattern in col_lower for pattern in country_patterns):
            country_candidates.append(col)
        elif any(pattern in col_lower for pattern in desc_patterns):
            desc_candidates.append(col)

    return {
        "name_candidates": name_candidates,
        "country_candidates": country_candidates,
        "description_candidates": desc_candidates,
        "all_columns": df.columns.tolist(),
    }


__all__ = ["parse_file", "detect_columns", "get_column_suggestions", "ColumnMapping"]

