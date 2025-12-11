"""Unit tests for custom exception hierarchy."""

import pytest

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


class TestOFACError:
    """Tests for base OFACError class."""

    def test_create_with_message(self) -> None:
        """OFACError can be created with just a message."""
        error = OFACError("Something went wrong")
        assert str(error) == "Something went wrong"
        assert error.message == "Something went wrong"
        assert error.code == "OFAC_ERROR"
        assert error.details == {}

    def test_create_with_code_override(self) -> None:
        """OFACError code can be overridden."""
        error = OFACError("Error", code="CUSTOM_CODE")
        assert error.code == "CUSTOM_CODE"

    def test_create_with_details(self) -> None:
        """OFACError can include details dict."""
        error = OFACError("Error", details={"file": "test.csv", "line": 42})
        assert error.details == {"file": "test.csv", "line": 42}

    def test_to_dict(self) -> None:
        """OFACError can be converted to dict for API response."""
        error = OFACError("Error message", details={"key": "value"})
        result = error.to_dict()
        assert result == {
            "code": "OFAC_ERROR",
            "message": "Error message",
            "details": {"key": "value"},
        }

    def test_repr(self) -> None:
        """OFACError has informative repr."""
        error = OFACError("Test error")
        assert "OFACError" in repr(error)
        assert "OFAC_ERROR" in repr(error)
        assert "Test error" in repr(error)

    def test_is_exception(self) -> None:
        """OFACError is an Exception."""
        error = OFACError("Test")
        assert isinstance(error, Exception)

    def test_can_be_raised_and_caught(self) -> None:
        """OFACError can be raised and caught."""
        with pytest.raises(OFACError) as exc_info:
            raise OFACError("Test error")
        assert exc_info.value.message == "Test error"


class TestFileValidationErrors:
    """Tests for file validation exception classes."""

    def test_file_validation_error_code(self) -> None:
        """FileValidationError has correct code."""
        error = FileValidationError("Invalid file")
        assert error.code == "FILE_VALIDATION_ERROR"
        assert isinstance(error, OFACError)

    def test_file_format_error_code(self) -> None:
        """FileFormatError has correct code."""
        error = FileFormatError("Unsupported format")
        assert error.code == "FILE_INVALID_FORMAT"
        assert isinstance(error, FileValidationError)

    def test_file_empty_error_code(self) -> None:
        """FileEmptyError has correct code."""
        error = FileEmptyError("File is empty")
        assert error.code == "FILE_EMPTY"
        assert isinstance(error, FileValidationError)

    def test_file_too_large_error_code(self) -> None:
        """FileTooLargeError has correct code."""
        error = FileTooLargeError("File exceeds limit")
        assert error.code == "FILE_TOO_LARGE"
        assert isinstance(error, FileValidationError)

    def test_file_parse_error_code(self) -> None:
        """FileParseError has correct code."""
        error = FileParseError("Cannot parse file")
        assert error.code == "FILE_PARSE_ERROR"
        assert isinstance(error, FileValidationError)

    def test_column_mapping_error_code(self) -> None:
        """ColumnMappingError has correct code."""
        error = ColumnMappingError("Cannot find required columns")
        assert error.code == "FILE_COLUMN_MAPPING_ERROR"
        assert isinstance(error, FileValidationError)

    def test_file_error_inheritance(self) -> None:
        """All file errors inherit from FileValidationError."""
        errors = [
            FileFormatError("test"),
            FileEmptyError("test"),
            FileTooLargeError("test"),
            FileParseError("test"),
            ColumnMappingError("test"),
        ]
        for error in errors:
            assert isinstance(error, FileValidationError)
            assert isinstance(error, OFACError)


class TestOFACDataErrors:
    """Tests for OFAC data exception classes."""

    def test_ofac_data_error_code(self) -> None:
        """OFACDataError has correct code."""
        error = OFACDataError("Data error")
        assert error.code == "OFAC_DATA_ERROR"
        assert isinstance(error, OFACError)

    def test_ofac_download_error_code(self) -> None:
        """OFACDownloadError has correct code."""
        error = OFACDownloadError("Download failed")
        assert error.code == "OFAC_DOWNLOAD_ERROR"
        assert isinstance(error, OFACDataError)

    def test_ofac_parse_error_code(self) -> None:
        """OFACParseError has correct code."""
        error = OFACParseError("Parse failed")
        assert error.code == "OFAC_PARSE_ERROR"
        assert isinstance(error, OFACDataError)

    def test_ofac_integrity_error_code(self) -> None:
        """OFACIntegrityError has correct code."""
        error = OFACIntegrityError("Integrity check failed")
        assert error.code == "OFAC_INTEGRITY_ERROR"
        assert isinstance(error, OFACDataError)

    def test_ofac_not_loaded_error_code(self) -> None:
        """OFACNotLoadedError has correct code."""
        error = OFACNotLoadedError("Data not loaded")
        assert error.code == "OFAC_NOT_LOADED"
        assert isinstance(error, OFACDataError)

    def test_ofac_stale_data_error_code(self) -> None:
        """OFACStaleDataError has correct code."""
        error = OFACStaleDataError("Data is stale")
        assert error.code == "OFAC_STALE_DATA"
        assert isinstance(error, OFACDataError)

    def test_ofac_error_inheritance(self) -> None:
        """All OFAC errors inherit from OFACDataError."""
        errors = [
            OFACDownloadError("test"),
            OFACParseError("test"),
            OFACIntegrityError("test"),
            OFACNotLoadedError("test"),
            OFACStaleDataError("test"),
        ]
        for error in errors:
            assert isinstance(error, OFACDataError)
            assert isinstance(error, OFACError)


class TestScreeningErrors:
    """Tests for screening exception classes."""

    def test_screening_error_code(self) -> None:
        """ScreeningError has correct code."""
        error = ScreeningError("Screening error")
        assert error.code == "SCREEN_ERROR"
        assert isinstance(error, OFACError)

    def test_screening_input_error_code(self) -> None:
        """ScreeningInputError has correct code."""
        error = ScreeningInputError("Invalid input")
        assert error.code == "SCREEN_INVALID_INPUT"
        assert isinstance(error, ScreeningError)

    def test_screening_timeout_error_code(self) -> None:
        """ScreeningTimeoutError has correct code."""
        error = ScreeningTimeoutError("Timeout")
        assert error.code == "SCREEN_TIMEOUT"
        assert isinstance(error, ScreeningError)

    def test_batch_too_large_error_code(self) -> None:
        """BatchTooLargeError has correct code."""
        error = BatchTooLargeError("Batch too large")
        assert error.code == "SCREEN_BATCH_TOO_LARGE"
        assert isinstance(error, ScreeningError)

    def test_screening_error_inheritance(self) -> None:
        """All screening errors inherit from ScreeningError."""
        errors = [
            ScreeningInputError("test"),
            ScreeningTimeoutError("test"),
            BatchTooLargeError("test"),
        ]
        for error in errors:
            assert isinstance(error, ScreeningError)
            assert isinstance(error, OFACError)


class TestConfigurationErrors:
    """Tests for configuration exception classes."""

    def test_configuration_error_code(self) -> None:
        """ConfigurationError has correct code."""
        error = ConfigurationError("Config error")
        assert error.code == "CONFIG_ERROR"
        assert isinstance(error, OFACError)

    def test_invalid_threshold_error_code(self) -> None:
        """InvalidThresholdError has correct code."""
        error = InvalidThresholdError("Invalid threshold")
        assert error.code == "CONFIG_INVALID_THRESHOLD"
        assert isinstance(error, ConfigurationError)


class TestExceptionImports:
    """Tests for exception imports from ofac.core."""

    def test_import_from_exceptions(self) -> None:
        """Exceptions can be imported from ofac.core.exceptions."""
        from ofac.core.exceptions import (
            FileValidationError,
            OFACDataError,
            OFACError,
            ScreeningError,
        )

        assert OFACError is not None
        assert FileValidationError is not None
        assert OFACDataError is not None
        assert ScreeningError is not None

    def test_import_from_core(self) -> None:
        """Exceptions can be imported from ofac.core."""
        from ofac.core import (
            FileValidationError,
            OFACDataError,
            OFACError,
            ScreeningError,
        )

        assert OFACError is not None
        assert FileValidationError is not None
        assert OFACDataError is not None
        assert ScreeningError is not None


class TestExceptionUsagePatterns:
    """Tests for common exception usage patterns."""

    def test_catch_specific_before_general(self) -> None:
        """Specific exceptions can be caught before general ones."""
        try:
            raise FileFormatError("PDF not supported", details={"format": "pdf"})
        except FileFormatError as e:
            assert e.code == "FILE_INVALID_FORMAT"
            assert e.details["format"] == "pdf"
        except FileValidationError:
            pytest.fail("Should have caught FileFormatError first")

    def test_catch_by_base_class(self) -> None:
        """All exceptions can be caught by OFACError."""
        exceptions_to_test = [
            FileFormatError("test"),
            OFACDownloadError("test"),
            ScreeningInputError("test"),
            ConfigurationError("test"),
        ]
        for exc in exceptions_to_test:
            try:
                raise exc
            except OFACError as e:
                assert e.code is not None
                assert e.message == "test"

    def test_to_dict_for_api_response(self) -> None:
        """Exception can be converted to API response format."""
        error = FileFormatError(
            "Unsupported file format: PDF",
            details={"filename": "test.pdf", "supported": ["csv", "xlsx"]},
        )
        response = error.to_dict()
        assert response["code"] == "FILE_INVALID_FORMAT"
        assert "PDF" in response["message"]
        assert response["details"]["filename"] == "test.pdf"
