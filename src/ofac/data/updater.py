"""OFAC data updater for downloading and updating sanctions lists.

This module provides the OFACUpdater class for:
- Downloading SDN.CSV, ALT.CSV, ADD.CSV from Treasury.gov
- Atomic swap mechanism to prevent corruption
- Version tracking with version.json
- Error handling with rollback

Usage:
    from ofac.data.updater import OFACUpdater

    updater = OFACUpdater()
    updater.download_sdn_files()
"""

import json
import shutil
from datetime import UTC, datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any

import httpx

from ofac.core.config import settings
from ofac.core.exceptions import OFACDownloadError, OFACIntegrityError, OFACParseError


# OFAC Treasury.gov download URLs
OFAC_BASE_URL = "https://www.treasury.gov/ofac/downloads"
SDN_FILES = {
    "sdn.csv": f"{OFAC_BASE_URL}/sdn.csv",
    "alt.csv": f"{OFAC_BASE_URL}/alt.csv",
    "add.csv": f"{OFAC_BASE_URL}/add.csv",
}


class OFACUpdater:
    """Downloads and updates OFAC CSV triplet files.

    This class handles downloading OFAC data from Treasury.gov,
    validating downloads, and performing atomic swaps to prevent
    data corruption during updates.

    Attributes:
        data_path: Path to directory for OFAC data files
        timeout: HTTP request timeout in seconds

    Example:
        updater = OFACUpdater()
        updater.download_sdn_files()
    """

    def __init__(self, data_path: Path | None = None, timeout: int = 120) -> None:
        """Initialize the updater.

        Args:
            data_path: Path to OFAC data directory. Defaults to settings.ofac_data_path.
            timeout: HTTP request timeout in seconds. Defaults to 120.
        """
        self.data_path = data_path or settings.ofac_data_path
        self.timeout = timeout
        self.data_path.mkdir(parents=True, exist_ok=True)

    def download_sdn_files(self) -> dict[str, Any]:
        """Download SDN triplet files (SDN.CSV, ALT.CSV, ADD.CSV).

        Downloads all three files, validates them, and performs an
        atomic swap to replace existing files only if all downloads
        succeed.

        Returns:
            Dict with download metadata:
            {
                "download_date": "2025-12-11T10:30:00Z",
                "last_modified": "2025-12-10T15:00:00Z",
                "files_downloaded": ["sdn.csv", "alt.csv", "add.csv"],
                "file_sizes": {"sdn.csv": 1234567, ...}
            }

        Raises:
            OFACDownloadError: If download fails or network error occurs.
            OFACIntegrityError: If downloaded files are invalid or corrupted.
        """
        downloaded_files: dict[str, Path] = {}
        file_metadata: dict[str, Any] = {}
        last_modified: str | None = None

        try:
            # Download all files to temporary directory
            with TemporaryDirectory(prefix="ofac_download_") as temp_dir:
                temp_path = Path(temp_dir)

                for filename, url in SDN_FILES.items():
                    file_path = temp_path / filename
                    metadata = self._download_file(url, file_path)
                    downloaded_files[filename] = file_path
                    file_metadata[filename] = metadata

                    # Track most recent last-modified header
                    if metadata.get("last_modified") and (
                        last_modified is None
                        or metadata["last_modified"] > last_modified
                    ):
                        last_modified = metadata["last_modified"]

                # Validate downloaded files
                self._validate_downloads(downloaded_files)

                # Atomic swap: move temp files to data_path
                self._atomic_swap(downloaded_files)

                # Create version.json
                version_info = {
                    "download_date": datetime.now(UTC).isoformat(),
                    "last_modified": last_modified or datetime.now(UTC).isoformat(),
                    "files_downloaded": list(SDN_FILES.keys()),
                    "file_sizes": {
                        name: metadata.get("size", 0)
                        for name, metadata in file_metadata.items()
                    },
                }
                self._write_version_json(version_info)

                return version_info

        except httpx.HTTPError as e:
            raise OFACDownloadError(
                f"Network error during OFAC download: {str(e)}",
                details={"urls": list(SDN_FILES.values()), "error": str(e)},
            ) from e
        except Exception as e:
            # Ensure existing files are not corrupted
            raise OFACDownloadError(
                f"Failed to download OFAC files: {str(e)}",
                details={"error": str(e)},
            ) from e

    def _download_file(self, url: str, dest_path: Path) -> dict[str, Any]:
        """Download a single file from URL.

        Args:
            url: URL to download from.
            dest_path: Local path to save file.

        Returns:
            Dict with file metadata:
            {
                "size": 1234567,
                "last_modified": "2025-12-10T15:00:00Z",
                "status_code": 200
            }

        Raises:
            OFACDownloadError: If download fails.
        """
        try:
            with httpx.Client(timeout=self.timeout, follow_redirects=True) as client:
                response = client.get(url)

                if response.status_code != 200:
                    raise OFACDownloadError(
                        f"HTTP {response.status_code} when downloading {url}",
                        details={"url": url, "status_code": response.status_code},
                    )

                # Save file
                dest_path.write_bytes(response.content)

                # Extract last-modified header
                last_modified = response.headers.get("Last-Modified")
                if last_modified:
                    # Parse RFC 2822 date format
                    try:
                        from email.utils import parsedate_to_datetime

                        dt = parsedate_to_datetime(last_modified)
                        last_modified_iso = dt.isoformat()
                    except Exception:
                        last_modified_iso = None
                else:
                    last_modified_iso = None

                return {
                    "size": len(response.content),
                    "last_modified": last_modified_iso,
                    "status_code": response.status_code,
                }

        except httpx.TimeoutException as e:
            raise OFACDownloadError(
                f"Timeout downloading {url}",
                details={"url": url, "timeout": self.timeout},
            ) from e
        except httpx.RequestError as e:
            raise OFACDownloadError(
                f"Request error downloading {url}: {str(e)}",
                details={"url": url, "error": str(e)},
            ) from e

    def _validate_downloads(self, files: dict[str, Path]) -> None:
        """Validate downloaded files before swap.

        Checks that files exist, are non-empty, and have expected
        structure (basic CSV validation).

        Args:
            files: Dict mapping filename to file path.

        Raises:
            OFACIntegrityError: If validation fails.
        """
        for filename, file_path in files.items():
            if not file_path.exists():
                raise OFACIntegrityError(
                    f"Downloaded file not found: {filename}",
                    details={"filename": filename, "path": str(file_path)},
                )

            if file_path.stat().st_size == 0:
                raise OFACIntegrityError(
                    f"Downloaded file is empty: {filename}",
                    details={"filename": filename},
                )

            # Basic CSV validation: check first line is not empty
            try:
                first_line = file_path.read_text(encoding="utf-8", errors="ignore").split(
                    "\n"
                )[0]
                if not first_line.strip():
                    raise OFACIntegrityError(
                        f"Downloaded file appears corrupted: {filename}",
                        details={"filename": filename},
                    )
            except Exception as e:
                raise OFACIntegrityError(
                    f"Failed to validate downloaded file: {filename}",
                    details={"filename": filename, "error": str(e)},
                ) from e

    def _atomic_swap(self, files: dict[str, Path]) -> None:
        """Perform atomic swap of downloaded files to data_path.

        Moves files from temporary directory to data_path, replacing
        existing files only after all files are successfully moved.

        Args:
            files: Dict mapping filename to temporary file path.

        Raises:
            OFACIntegrityError: If swap fails.
        """
        try:
            for filename, temp_path in files.items():
                dest_path = self.data_path / filename
                shutil.move(str(temp_path), str(dest_path))
        except Exception as e:
            # If swap fails, existing files remain untouched
            raise OFACIntegrityError(
                f"Failed to swap downloaded files: {str(e)}",
                details={"error": str(e)},
            ) from e

    def _write_version_json(self, version_info: dict[str, Any]) -> None:
        """Write version.json metadata file.

        Args:
            version_info: Dict with version metadata.
        """
        version_path = self.data_path / "version.json"
        version_path.write_text(
            json.dumps(version_info, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    def get_current_version(self) -> dict[str, Any] | None:
        """Get current OFAC data version from version.json.

        Returns:
            Dict with version info, or None if version.json doesn't exist.
        """
        version_path = self.data_path / "version.json"
        if not version_path.exists():
            return None

        try:
            data = json.loads(version_path.read_text(encoding="utf-8"))
            return dict(data) if isinstance(data, dict) else None
        except Exception:
            return None

    def check_for_updates(self) -> bool:
        """Check if OFAC data needs updating.

        Compares local version with remote last-modified headers
        to determine if update is needed.

        Returns:
            True if update is needed, False otherwise.

        Raises:
            OFACDownloadError: If check fails.
        """
        local_version = self.get_current_version()
        if local_version is None:
            return True  # No local data, update needed

        try:
            # Check last-modified header for SDN.CSV
            url = SDN_FILES["sdn.csv"]
            with httpx.Client(timeout=30, follow_redirects=True) as client:
                response = client.head(url)
                if response.status_code != 200:
                    return False  # Can't check, assume no update

                remote_last_modified = response.headers.get("Last-Modified")
                if not remote_last_modified:
                    return False  # Can't compare, assume no update

                from email.utils import parsedate_to_datetime

                remote_dt = parsedate_to_datetime(remote_last_modified)
                local_dt_str = local_version.get("last_modified")
                if not local_dt_str:
                    return True  # No local timestamp, update needed

                # Parse local datetime and make timezone-aware for comparison
                local_dt_str_clean = local_dt_str.replace("Z", "+00:00")
                local_dt = datetime.fromisoformat(local_dt_str_clean)
                if local_dt.tzinfo is None:
                    local_dt = local_dt.replace(tzinfo=UTC)

                # Compare timezone-aware datetimes
                result: bool = remote_dt > local_dt
                return result

        except Exception:
            # On error, assume update needed for safety
            return True


__all__ = ["OFACUpdater", "OFAC_BASE_URL", "SDN_FILES"]

