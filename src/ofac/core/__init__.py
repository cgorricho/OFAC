"""Core business logic for OFAC screening.

This module contains:
- config: Pydantic Settings configuration
- models: Pydantic data models
- exceptions: Custom exception hierarchy
- matcher: Fuzzy matching engine
- classifier: OK/REVIEW/NOK classification
- reporter: Report generation
"""

from ofac.core.classifier import classify_screening_result
from ofac.core.config import Settings, settings
from ofac.core.exceptions import (
    BatchTooLargeError,
    ColumnMappingError,
    ConfigurationError,
    FileEmptyError,
    FileFormatError,
    FileParseError,
    FileTooLargeError,
    FileValidationError,
    InvalidThresholdError,
    OFACDataError,
    OFACDownloadError,
    OFACError,
    OFACIntegrityError,
    OFACNotLoadedError,
    OFACParseError,
    OFACStaleDataError,
    ScreeningError,
    ScreeningInputError,
    ScreeningTimeoutError,
)
from ofac.core.matcher import EntityMatcher
from ofac.core.models import (
    BatchScreeningRequest,
    BatchScreeningResponse,
    EntityInput,
    MatchResult,
    MatchStatus,
    MatchType,
    OFACList,
    ScreeningResult,
)

__all__ = [
    # Config
    "Settings",
    "settings",
    # Classifier
    "classify_screening_result",
    # Matcher
    "EntityMatcher",
    # Models
    "MatchStatus",
    "MatchType",
    "OFACList",
    "EntityInput",
    "MatchResult",
    "ScreeningResult",
    "BatchScreeningRequest",
    "BatchScreeningResponse",
    # Exceptions
    "OFACError",
    "FileValidationError",
    "FileFormatError",
    "FileEmptyError",
    "FileTooLargeError",
    "FileParseError",
    "ColumnMappingError",
    "OFACDataError",
    "OFACDownloadError",
    "OFACParseError",
    "OFACIntegrityError",
    "OFACNotLoadedError",
    "OFACStaleDataError",
    "ScreeningError",
    "ScreeningInputError",
    "ScreeningTimeoutError",
    "BatchTooLargeError",
    "ConfigurationError",
    "InvalidThresholdError",
]

