"""Custom exception hierarchy for OFAC screening.

This module provides structured exceptions with:
- Error codes for API responses
- Human-readable messages
- Consistent exception handling

Error Code Prefixes:
- FILE_*: File validation and parsing errors
- OFAC_*: OFAC data errors (download, parse, integrity)
- SCREEN_*: Screening operation errors
- CONFIG_*: Configuration errors

Usage:
    from ofac.core.exceptions import FileValidationError, OFACDataError

    raise FileValidationError("Invalid file format", details={"format": "pdf"})
"""

from typing import Any


class OFACError(Exception):
    """Base exception for all OFAC screening errors.

    All custom exceptions inherit from this class, providing:
    - code: Machine-readable error code for API responses
    - message: Human-readable error message
    - details: Optional additional context

    Attributes:
        code: Error code string (e.g., "FILE_INVALID_FORMAT")
        message: Human-readable error message
        details: Optional dict with additional error context
    """

    code: str = "OFAC_ERROR"

    def __init__(
        self,
        message: str,
        *,
        code: str | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        """Initialize OFACError.

        Args:
            message: Human-readable error message
            code: Optional override for error code
            details: Optional additional context dict
        """
        super().__init__(message)
        self.message = message
        if code is not None:
            self.code = code
        self.details = details or {}

    def to_dict(self) -> dict[str, Any]:
        """Convert exception to API-friendly dict.

        Returns:
            Dict with code, message, and details for JSON response
        """
        return {
            "code": self.code,
            "message": self.message,
            "details": self.details,
        }

    def __repr__(self) -> str:
        """Return detailed string representation."""
        return f"{self.__class__.__name__}(code={self.code!r}, message={self.message!r})"


# =============================================================================
# File Validation Errors (FILE_*)
# =============================================================================


class FileValidationError(OFACError):
    """Base exception for file validation errors."""

    code = "FILE_VALIDATION_ERROR"


class FileFormatError(FileValidationError):
    """Raised when file format is not supported."""

    code = "FILE_INVALID_FORMAT"


class FileEmptyError(FileValidationError):
    """Raised when uploaded file is empty."""

    code = "FILE_EMPTY"


class FileTooLargeError(FileValidationError):
    """Raised when file exceeds maximum size or row limit."""

    code = "FILE_TOO_LARGE"


class FileParseError(FileValidationError):
    """Raised when file cannot be parsed (corrupt CSV/Excel)."""

    code = "FILE_PARSE_ERROR"


class ColumnMappingError(FileValidationError):
    """Raised when required columns cannot be mapped."""

    code = "FILE_COLUMN_MAPPING_ERROR"


# =============================================================================
# OFAC Data Errors (OFAC_*)
# =============================================================================


class OFACDataError(OFACError):
    """Base exception for OFAC data management errors."""

    code = "OFAC_DATA_ERROR"


class OFACDownloadError(OFACDataError):
    """Raised when OFAC data cannot be downloaded."""

    code = "OFAC_DOWNLOAD_ERROR"


class OFACParseError(OFACDataError):
    """Raised when OFAC CSV files cannot be parsed."""

    code = "OFAC_PARSE_ERROR"


class OFACIntegrityError(OFACDataError):
    """Raised when OFAC data fails integrity checks."""

    code = "OFAC_INTEGRITY_ERROR"


class OFACNotLoadedError(OFACDataError):
    """Raised when OFAC data is accessed but not loaded."""

    code = "OFAC_NOT_LOADED"


class OFACStaleDataError(OFACDataError):
    """Raised when OFAC data is older than acceptable threshold."""

    code = "OFAC_STALE_DATA"


# =============================================================================
# Screening Errors (SCREEN_*)
# =============================================================================


class ScreeningError(OFACError):
    """Base exception for screening operation errors."""

    code = "SCREEN_ERROR"


class ScreeningInputError(ScreeningError):
    """Raised when screening input is invalid."""

    code = "SCREEN_INVALID_INPUT"


class ScreeningTimeoutError(ScreeningError):
    """Raised when screening operation times out."""

    code = "SCREEN_TIMEOUT"


class BatchTooLargeError(ScreeningError):
    """Raised when batch exceeds maximum allowed size."""

    code = "SCREEN_BATCH_TOO_LARGE"


# =============================================================================
# Configuration Errors (CONFIG_*)
# =============================================================================


class ConfigurationError(OFACError):
    """Base exception for configuration errors."""

    code = "CONFIG_ERROR"


class InvalidThresholdError(ConfigurationError):
    """Raised when threshold configuration is invalid."""

    code = "CONFIG_INVALID_THRESHOLD"


__all__ = [
    # Base
    "OFACError",
    # File errors
    "FileValidationError",
    "FileFormatError",
    "FileEmptyError",
    "FileTooLargeError",
    "FileParseError",
    "ColumnMappingError",
    # OFAC data errors
    "OFACDataError",
    "OFACDownloadError",
    "OFACParseError",
    "OFACIntegrityError",
    "OFACNotLoadedError",
    "OFACStaleDataError",
    # Screening errors
    "ScreeningError",
    "ScreeningInputError",
    "ScreeningTimeoutError",
    "BatchTooLargeError",
    # Config errors
    "ConfigurationError",
    "InvalidThresholdError",
]

