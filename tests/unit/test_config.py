"""Unit tests for configuration module."""

import os
from pathlib import Path
from unittest.mock import patch

import pytest
from pydantic import ValidationError

from ofac.core.config import Settings


class TestSettingsDefaults:
    """Test that all settings have sensible defaults."""

    def test_default_threshold_nok(self) -> None:
        """Default NOK threshold is 95."""
        settings = Settings()
        assert settings.match_threshold_nok == 95

    def test_default_threshold_review(self) -> None:
        """Default REVIEW threshold is 80."""
        settings = Settings()
        assert settings.match_threshold_review == 80

    def test_default_ofac_data_path(self) -> None:
        """Default OFAC data path is ./data/ofac."""
        settings = Settings()
        assert settings.ofac_data_path == Path("./data/ofac")

    def test_default_log_level(self) -> None:
        """Default log level is INFO."""
        settings = Settings()
        assert settings.log_level == "INFO"

    def test_default_batch_size(self) -> None:
        """Default batch size is 100."""
        settings = Settings()
        assert settings.batch_size == 100

    def test_default_max_file_rows(self) -> None:
        """Default max file rows is 10000."""
        settings = Settings()
        assert settings.max_file_rows == 10000

    def test_default_api_host(self) -> None:
        """Default API host is 127.0.0.1."""
        settings = Settings()
        assert settings.api_host == "127.0.0.1"

    def test_default_api_port(self) -> None:
        """Default API port is 8000."""
        settings = Settings()
        assert settings.api_port == 8000

    def test_default_streamlit_port(self) -> None:
        """Default Streamlit port is 8501."""
        settings = Settings()
        assert settings.streamlit_port == 8501

    def test_default_auto_update(self) -> None:
        """Default auto_update is True."""
        settings = Settings()
        assert settings.auto_update is True

    def test_default_update_check_hours(self) -> None:
        """Default update check hours is 24."""
        settings = Settings()
        assert settings.update_check_hours == 24

    def test_default_log_path(self) -> None:
        """Default log path is ./data/logs."""
        settings = Settings()
        assert settings.log_path == Path("./data/logs")


class TestEnvironmentVariableOverride:
    """Test that environment variables override defaults."""

    def test_override_threshold_nok(self) -> None:
        """OFAC_MATCH_THRESHOLD_NOK overrides default."""
        with patch.dict(os.environ, {"OFAC_MATCH_THRESHOLD_NOK": "90"}):
            settings = Settings()
            assert settings.match_threshold_nok == 90

    def test_override_threshold_review(self) -> None:
        """OFAC_MATCH_THRESHOLD_REVIEW overrides default."""
        with patch.dict(os.environ, {"OFAC_MATCH_THRESHOLD_REVIEW": "75"}):
            settings = Settings()
            assert settings.match_threshold_review == 75

    def test_override_log_level(self) -> None:
        """OFAC_LOG_LEVEL overrides default."""
        with patch.dict(os.environ, {"OFAC_LOG_LEVEL": "DEBUG"}):
            settings = Settings()
            assert settings.log_level == "DEBUG"

    def test_override_ofac_data_path(self) -> None:
        """OFAC_OFAC_DATA_PATH overrides default."""
        with patch.dict(os.environ, {"OFAC_OFAC_DATA_PATH": "/custom/path"}):
            settings = Settings()
            assert settings.ofac_data_path == Path("/custom/path")

    def test_override_api_port(self) -> None:
        """OFAC_API_PORT overrides default."""
        with patch.dict(os.environ, {"OFAC_API_PORT": "9000"}):
            settings = Settings()
            assert settings.api_port == 9000

    def test_override_batch_size(self) -> None:
        """OFAC_BATCH_SIZE overrides default."""
        with patch.dict(os.environ, {"OFAC_BATCH_SIZE": "50"}):
            settings = Settings()
            assert settings.batch_size == 50

    def test_override_auto_update_false(self) -> None:
        """OFAC_AUTO_UPDATE=false disables auto update."""
        with patch.dict(os.environ, {"OFAC_AUTO_UPDATE": "false"}):
            settings = Settings()
            assert settings.auto_update is False


class TestValidation:
    """Test that invalid values raise ValidationError."""

    def test_threshold_nok_below_zero(self) -> None:
        """NOK threshold below 0 raises ValidationError."""
        with (
            patch.dict(os.environ, {"OFAC_MATCH_THRESHOLD_NOK": "-1"}),
            pytest.raises(ValidationError),
        ):
            Settings()

    def test_threshold_nok_above_100(self) -> None:
        """NOK threshold above 100 raises ValidationError."""
        with (
            patch.dict(os.environ, {"OFAC_MATCH_THRESHOLD_NOK": "101"}),
            pytest.raises(ValidationError),
        ):
            Settings()

    def test_threshold_review_below_zero(self) -> None:
        """REVIEW threshold below 0 raises ValidationError."""
        with (
            patch.dict(os.environ, {"OFAC_MATCH_THRESHOLD_REVIEW": "-5"}),
            pytest.raises(ValidationError),
        ):
            Settings()

    def test_threshold_review_above_100(self) -> None:
        """REVIEW threshold above 100 raises ValidationError."""
        with (
            patch.dict(os.environ, {"OFAC_MATCH_THRESHOLD_REVIEW": "150"}),
            pytest.raises(ValidationError),
        ):
            Settings()

    def test_invalid_log_level(self) -> None:
        """Invalid log level raises ValidationError."""
        with (
            patch.dict(os.environ, {"OFAC_LOG_LEVEL": "INVALID"}),
            pytest.raises(ValidationError),
        ):
            Settings()

    def test_batch_size_below_one(self) -> None:
        """Batch size below 1 raises ValidationError."""
        with (
            patch.dict(os.environ, {"OFAC_BATCH_SIZE": "0"}),
            pytest.raises(ValidationError),
        ):
            Settings()

    def test_batch_size_above_max(self) -> None:
        """Batch size above max raises ValidationError."""
        with (
            patch.dict(os.environ, {"OFAC_BATCH_SIZE": "20000"}),
            pytest.raises(ValidationError),
        ):
            Settings()

    def test_invalid_api_port_below_one(self) -> None:
        """API port below 1 raises ValidationError."""
        with (
            patch.dict(os.environ, {"OFAC_API_PORT": "0"}),
            pytest.raises(ValidationError),
        ):
            Settings()

    def test_invalid_api_port_above_max(self) -> None:
        """API port above 65535 raises ValidationError."""
        with (
            patch.dict(os.environ, {"OFAC_API_PORT": "70000"}),
            pytest.raises(ValidationError),
        ):
            Settings()

    def test_threshold_review_must_be_less_than_nok(self) -> None:
        """REVIEW threshold must be less than NOK threshold."""
        with (
            patch.dict(
                os.environ,
                {"OFAC_MATCH_THRESHOLD_REVIEW": "95", "OFAC_MATCH_THRESHOLD_NOK": "80"},
            ),
            pytest.raises(ValidationError),
        ):
            Settings()

    def test_threshold_review_equal_to_nok_fails(self) -> None:
        """REVIEW threshold equal to NOK threshold fails."""
        with (
            patch.dict(
                os.environ,
                {"OFAC_MATCH_THRESHOLD_REVIEW": "90", "OFAC_MATCH_THRESHOLD_NOK": "90"},
            ),
            pytest.raises(ValidationError),
        ):
            Settings()


class TestSettingsImport:
    """Test that settings can be imported from expected locations."""

    def test_import_from_config(self) -> None:
        """Settings can be imported from ofac.core.config."""
        from ofac.core.config import settings

        assert settings is not None
        assert hasattr(settings, "match_threshold_nok")

    def test_import_from_core(self) -> None:
        """Settings can be imported from ofac.core."""
        from ofac.core import settings

        assert settings is not None
        assert hasattr(settings, "match_threshold_nok")

    def test_settings_class_import(self) -> None:
        """Settings class can be imported for custom instances."""
        from ofac.core.config import Settings

        custom_settings = Settings(match_threshold_nok=85)
        assert custom_settings.match_threshold_nok == 85


class TestPathConversion:
    """Test that string paths are converted to Path objects."""

    def test_ofac_data_path_string_conversion(self) -> None:
        """String paths are converted to Path objects."""
        settings = Settings(ofac_data_path="/custom/data/path")  # type: ignore[arg-type]
        assert isinstance(settings.ofac_data_path, Path)
        assert settings.ofac_data_path == Path("/custom/data/path")

    def test_log_path_string_conversion(self) -> None:
        """Log path strings are converted to Path objects."""
        settings = Settings(log_path="/custom/log/path")  # type: ignore[arg-type]
        assert isinstance(settings.log_path, Path)
        assert settings.log_path == Path("/custom/log/path")
