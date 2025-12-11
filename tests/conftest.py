"""Pytest configuration and shared fixtures.

This module provides fixtures for:
- Mock OFAC data
- Test client setup
- Temporary directories
- Sample entities for testing
"""

from collections.abc import Generator
from pathlib import Path

import pytest

# Test data directory
FIXTURES_DIR = Path(__file__).parent / "fixtures"
MOCK_OFAC_DATA_DIR = FIXTURES_DIR / "mock_ofac_data"


@pytest.fixture
def fixtures_dir() -> Path:
    """Return the path to the test fixtures directory."""
    return FIXTURES_DIR


@pytest.fixture
def mock_ofac_data_dir() -> Path:
    """Return the path to mock OFAC data directory."""
    return MOCK_OFAC_DATA_DIR


@pytest.fixture
def temp_data_dir(tmp_path: Path) -> Generator[Path, None, None]:
    """Provide a temporary directory for OFAC data during tests."""
    data_dir = tmp_path / "ofac_data"
    data_dir.mkdir()
    yield data_dir
    # Cleanup is automatic via tmp_path


@pytest.fixture
def sample_entities() -> list[dict[str, str]]:
    """Sample entities for testing screening operations."""
    return [
        {"name": "ACME Corporation", "country": "US"},
        {"name": "Archdiocese of Bangui", "country": "CF"},
        {"name": "Syrian Development Foundation", "country": "SY"},
        {"name": "Test Organization", "country": "GB"},
    ]


@pytest.fixture
def sample_entity_names() -> list[str]:
    """Simple list of entity names for basic matching tests."""
    return [
        "ACME Corporation",
        "Archdiocèse de Bangui",  # Unicode variant
        "Al-Noor Trading Company",
        "International Relief Organization",
    ]

