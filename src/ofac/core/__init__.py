"""Core business logic for OFAC screening.

This module contains:
- config: Pydantic Settings configuration
- models: Pydantic data models
- exceptions: Custom exception hierarchy
- matcher: Fuzzy matching engine
- classifier: OK/REVIEW/NOK classification
- reporter: Report generation
"""

from ofac.core.classifier import ScreeningClassifier, classify_screening_result
from ofac.core.countries import (
    GeneralLicense,
    get_all_sanctioned_countries,
    get_countries_with_gl,
    get_general_license,
    is_sanctioned_country,
)
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
    "ScreeningClassifier",
    "classify_screening_result",
    "classify_with_gl_context",
    "detect_humanitarian_keywords",
    "HUMANITARIAN_KEYWORDS",
    # Reporter
    "ReportGenerator",
    # Countries
    "is_sanctioned_country",
    "get_general_license",
    "get_all_sanctioned_countries",
    "get_countries_with_gl",
    "GeneralLicense",
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

