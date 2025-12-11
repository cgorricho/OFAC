"""Unit tests for OFAC data updater."""

import json
from datetime import UTC, datetime
from pathlib import Path
from unittest.mock import MagicMock, Mock, patch

import httpx
import pytest

from ofac.core.exceptions import OFACDownloadError, OFACIntegrityError
from ofac.data.updater import OFACUpdater, OFAC_BASE_URL, SDN_FILES


@pytest.fixture
def temp_data_path(tmp_path: Path) -> Path:
    """Create temporary data directory."""
    data_path = tmp_path / "ofac_data"
    data_path.mkdir(parents=True, exist_ok=True)
    return data_path


@pytest.fixture
def updater(temp_data_path: Path) -> OFACUpdater:
    """Create updater with temporary data path."""
    return OFACUpdater(data_path=temp_data_path)


class TestOFACUpdater:
    """Tests for OFACUpdater class."""

    def test_create_updater_default_path(self) -> None:
        """Updater uses settings.ofac_data_path by default."""
        updater = OFACUpdater()
        assert updater.data_path is not None

    def test_create_updater_custom_path(self, temp_data_path: Path) -> None:
        """Updater can use custom data path."""
        updater = OFACUpdater(data_path=temp_data_path)
        assert updater.data_path == temp_data_path

    def test_create_updater_creates_directory(self, tmp_path: Path) -> None:
        """Updater creates data directory if it doesn't exist."""
        data_path = tmp_path / "new_ofac_data"
        OFACUpdater(data_path=data_path)
        assert data_path.exists()


class TestDownloadSDNFiles:
    """Tests for download_sdn_files() method."""

    @patch("httpx.Client")
    def test_download_success(self, mock_client_class: MagicMock, updater: OFACUpdater) -> None:
        """download_sdn_files() successfully downloads all files."""
        # Mock HTTP responses
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"test,csv,content\n1,2,3"
        mock_response.headers = {"Last-Modified": "Mon, 10 Dec 2025 15:00:00 GMT"}

        mock_client = Mock()
        mock_client.__enter__ = Mock(return_value=mock_client)
        mock_client.__exit__ = Mock(return_value=None)
        mock_client.get.return_value = mock_response
        mock_client.head.return_value = mock_response
        mock_client_class.return_value = mock_client

        result = updater.download_sdn_files()

        # Verify all files downloaded
        assert (updater.data_path / "sdn.csv").exists()
        assert (updater.data_path / "alt.csv").exists()
        assert (updater.data_path / "add.csv").exists()
        assert (updater.data_path / "sdn.csv").read_text() == "test,csv,content\n1,2,3"

        # Verify version.json created
        version_path = updater.data_path / "version.json"
        assert version_path.exists()
        version_data = json.loads(version_path.read_text())
        assert "download_date" in version_data
        assert "files_downloaded" in version_data
        assert len(version_data["files_downloaded"]) == 3

        # Verify return value
        assert result["files_downloaded"] == ["sdn.csv", "alt.csv", "add.csv"]
        assert "download_date" in result

    @patch("httpx.Client")
    def test_download_http_error(self, mock_client_class: MagicMock, updater: OFACUpdater) -> None:
        """download_sdn_files() raises OFACDownloadError on HTTP error."""
        mock_response = Mock()
        mock_response.status_code = 404

        mock_client = Mock()
        mock_client.__enter__ = Mock(return_value=mock_client)
        mock_client.__exit__ = Mock(return_value=None)
        mock_client.get.return_value = mock_response
        mock_client_class.return_value = mock_client

        with pytest.raises(OFACDownloadError) as exc_info:
            updater.download_sdn_files()

        assert "HTTP 404" in str(exc_info.value)

    @patch("httpx.Client")
    def test_download_timeout(self, mock_client_class: MagicMock, updater: OFACUpdater) -> None:
        """download_sdn_files() raises OFACDownloadError on timeout."""
        mock_client = Mock()
        mock_client.__enter__ = Mock(return_value=mock_client)
        mock_client.__exit__ = Mock(return_value=None)
        mock_client.get.side_effect = httpx.TimeoutException("Request timed out")
        mock_client_class.return_value = mock_client

        with pytest.raises(OFACDownloadError) as exc_info:
            updater.download_sdn_files()

        assert "Timeout" in str(exc_info.value)

    @patch("httpx.Client")
    def test_download_empty_file(self, mock_client_class: MagicMock, updater: OFACUpdater) -> None:
        """download_sdn_files() raises OFACIntegrityError on empty file."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b""  # Empty file
        mock_response.headers = {}

        mock_client = Mock()
        mock_client.__enter__ = Mock(return_value=mock_client)
        mock_client.__exit__ = Mock(return_value=None)
        mock_client.get.return_value = mock_response
        mock_client_class.return_value = mock_client

        with pytest.raises(OFACDownloadError) as exc_info:
            updater.download_sdn_files()

        # The error is wrapped in OFACDownloadError
        assert "empty" in str(exc_info.value).lower() or "corrupted" in str(
            exc_info.value
        ).lower()

    @patch("httpx.Client")
    def test_atomic_swap_preserves_existing_on_failure(
        self, mock_client_class: MagicMock, updater: OFACUpdater
    ) -> None:
        """Atomic swap preserves existing files if download fails."""
        # Create existing files
        existing_file = updater.data_path / "sdn.csv"
        existing_file.write_text("existing,content\n1,2")

        # Mock first download success, second fails
        mock_response_ok = Mock()
        mock_response_ok.status_code = 200
        mock_response_ok.content = b"new,content\n3,4"
        mock_response_ok.headers = {}

        mock_response_fail = Mock()
        mock_response_fail.status_code = 500

        mock_client = Mock()
        mock_client.__enter__ = Mock(return_value=mock_client)
        mock_client.__exit__ = Mock(return_value=None)
        mock_client.get.side_effect = [mock_response_ok, mock_response_fail, mock_response_ok]
        mock_client_class.return_value = mock_client

        # Download should fail, existing file should remain
        with pytest.raises(OFACDownloadError):
            updater.download_sdn_files()

        # Existing file should still exist with original content
        assert existing_file.exists()
        assert "existing" in existing_file.read_text()


class TestGetCurrentVersion:
    """Tests for get_current_version() method."""

    def test_get_version_exists(self, updater: OFACUpdater) -> None:
        """get_current_version() returns version data if version.json exists."""
        version_data = {
            "download_date": "2025-12-10T10:00:00Z",
            "last_modified": "2025-12-09T15:00:00Z",
            "files_downloaded": ["sdn.csv"],
        }
        version_path = updater.data_path / "version.json"
        version_path.write_text(json.dumps(version_data))

        result = updater.get_current_version()
        assert result == version_data

    def test_get_version_not_exists(self, updater: OFACUpdater) -> None:
        """get_current_version() returns None if version.json doesn't exist."""
        result = updater.get_current_version()
        assert result is None

    def test_get_version_invalid_json(self, updater: OFACUpdater) -> None:
        """get_current_version() returns None if version.json is invalid."""
        version_path = updater.data_path / "version.json"
        version_path.write_text("invalid json{")

        result = updater.get_current_version()
        assert result is None


class TestCheckForUpdates:
    """Tests for check_for_updates() method."""

    def test_check_updates_no_local_version(self, updater: OFACUpdater) -> None:
        """check_for_updates() returns True if no local version exists."""
        result = updater.check_for_updates()
        assert result is True

    @patch("httpx.Client")
    def test_check_updates_remote_newer(
        self, mock_client_class: MagicMock, updater: OFACUpdater
    ) -> None:
        """check_for_updates() returns True if remote is newer."""
        # Create local version with old timestamp
        version_data = {
            "download_date": "2025-12-10T10:00:00Z",
            "last_modified": "2025-12-09T15:00:00Z",
        }
        version_path = updater.data_path / "version.json"
        version_path.write_text(json.dumps(version_data))

        # Mock remote with newer timestamp
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {"Last-Modified": "Mon, 11 Dec 2025 15:00:00 GMT"}

        mock_client = Mock()
        mock_client.__enter__ = Mock(return_value=mock_client)
        mock_client.__exit__ = Mock(return_value=None)
        mock_client.head.return_value = mock_response
        mock_client_class.return_value = mock_client

        result = updater.check_for_updates()
        assert result is True

    @patch("httpx.Client")
    def test_check_updates_local_newer(
        self, mock_client_class: MagicMock, updater: OFACUpdater
    ) -> None:
        """check_for_updates() returns False if local is newer."""
        # Create local version with new timestamp
        version_data = {
            "download_date": "2025-12-11T10:00:00Z",
            "last_modified": "2025-12-11T10:00:00Z",
        }
        version_path = updater.data_path / "version.json"
        version_path.write_text(json.dumps(version_data))

        # Mock remote with older timestamp
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {"Last-Modified": "Mon, 10 Dec 2025 15:00:00 GMT"}

        mock_client = Mock()
        mock_client.__enter__ = Mock(return_value=mock_client)
        mock_client.__exit__ = Mock(return_value=None)
        mock_client.head.return_value = mock_response
        mock_client_class.return_value = mock_client

        result = updater.check_for_updates()
        assert result is False

    @patch("httpx.Client")
    def test_check_updates_network_error(
        self, mock_client_class: MagicMock, updater: OFACUpdater
    ) -> None:
        """check_for_updates() returns True on network error (safe default)."""
        version_data = {
            "download_date": "2025-12-10T10:00:00Z",
            "last_modified": "2025-12-10T10:00:00Z",
        }
        version_path = updater.data_path / "version.json"
        version_path.write_text(json.dumps(version_data))

        mock_client = Mock()
        mock_client.__enter__ = Mock(return_value=mock_client)
        mock_client.__exit__ = Mock(return_value=None)
        mock_client.head.side_effect = httpx.RequestError("Network error")
        mock_client_class.return_value = mock_client

        result = updater.check_for_updates()
        assert result is True  # Safe default: assume update needed


class TestUpdaterImports:
    """Tests for updater imports."""

    def test_import_from_updater(self) -> None:
        """OFACUpdater can be imported from ofac.data.updater."""
        from ofac.data.updater import OFACUpdater, OFAC_BASE_URL, SDN_FILES

        assert OFACUpdater is not None
        assert OFAC_BASE_URL is not None
        assert SDN_FILES is not None

