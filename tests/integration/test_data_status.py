"""Integration tests for data status endpoint."""

from fastapi.testclient import TestClient

from ofac.api.main import create_app
from ofac.data.loader import OFACDataLoader


def test_get_status_returns_freshness_info(mock_ofac_data_dir) -> None:
    """GET /data/status returns freshness information."""
    loader = OFACDataLoader(data_path=mock_ofac_data_dir)
    data = loader.load()

    app = create_app()
    app.state.ofac_data = data
    app.state.ofac_loader = loader

    client = TestClient(app)
    response = client.get("/data/status")
    assert response.status_code == 200

    result = response.json()
    assert "version" in result
    assert "last_updated" in result
    assert "age_days" in result
    assert "freshness_status" in result
    assert "record_count" in result

    # Check freshness_status is valid
    assert result["freshness_status"] in ["CURRENT", "STALE", "CRITICAL"]


def test_get_status_includes_age_days(mock_ofac_data_dir) -> None:
    """GET /data/status includes age_days field."""
    loader = OFACDataLoader(data_path=mock_ofac_data_dir)
    data = loader.load()

    app = create_app()
    app.state.ofac_data = data
    app.state.ofac_loader = loader

    client = TestClient(app)
    response = client.get("/data/status")
    assert response.status_code == 200

    result = response.json()
    assert "age_days" in result
    assert isinstance(result["age_days"], int)
    assert result["age_days"] >= 0


def test_get_status_includes_record_count(mock_ofac_data_dir) -> None:
    """GET /data/status includes record_count field."""
    loader = OFACDataLoader(data_path=mock_ofac_data_dir)
    data = loader.load()

    app = create_app()
    app.state.ofac_data = data
    app.state.ofac_loader = loader

    client = TestClient(app)
    response = client.get("/data/status")
    assert response.status_code == 200

    result = response.json()
    assert "record_count" in result
    assert isinstance(result["record_count"], int)
    assert result["record_count"] >= 0

