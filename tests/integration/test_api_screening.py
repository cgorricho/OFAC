"""Integration tests for screening API endpoints."""

from fastapi.testclient import TestClient

from ofac.api.main import create_app
from ofac.data.loader import OFACDataLoader


def test_single_screening_endpoint_with_mock_data(mock_ofac_data_dir) -> None:
    """Test POST /screenings/single with mock OFAC data."""
    # Create app with mock data path
    loader = OFACDataLoader(data_path=mock_ofac_data_dir)
    data = loader.load()

    app = create_app()
    # Inject mock data into app state
    app.state.ofac_data = data
    app.state.ofac_loader = loader

    client = TestClient(app)

    # Test screening
    response = client.post(
        "/screenings/single",
        json={"entity_name": "BANCO NACIONAL DE CUBA"},
    )

    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "meta" in data
    assert data["data"]["screening_id"] is not None
    assert data["data"]["timestamp"] is not None
    assert data["data"]["match_status"] in ["OK", "REVIEW", "NOK"]
    assert "ofac_version" in data["meta"]
    assert "duration_ms" in data["meta"]


def test_single_screening_with_country(mock_ofac_data_dir) -> None:
    """Test single screening with country parameter."""
    loader = OFACDataLoader(data_path=mock_ofac_data_dir)
    data = loader.load()

    app = create_app()
    app.state.ofac_data = data
    app.state.ofac_loader = loader

    client = TestClient(app)

    response = client.post(
        "/screenings/single",
        json={"entity_name": "BANCO NACIONAL", "country": "Cuba"},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["data"]["entity_input"]["country"] == "Cuba"


def test_single_screening_invalid_json() -> None:
    """Test single screening with invalid JSON."""
    app = create_app()
    client = TestClient(app)

    response = client.post(
        "/screenings/single",
        json={"invalid": "data"},
    )

    # Should return 422 (validation error) or 503 (data not loaded)
    assert response.status_code in [422, 503]


def test_single_screening_missing_entity_name(mock_ofac_data_dir) -> None:
    """Test single screening with missing entity_name."""
    loader = OFACDataLoader(data_path=mock_ofac_data_dir)
    data = loader.load()

    app = create_app()
    app.state.ofac_data = data
    app.state.ofac_loader = loader

    client = TestClient(app)

    response = client.post(
        "/screenings/single",
        json={},
    )

    assert response.status_code == 422  # Validation error


def test_single_screening_no_ofac_data() -> None:
    """Test single screening when OFAC data is not loaded."""
    app = create_app()
    # Don't set ofac_data in app.state
    client = TestClient(app)

    response = client.post(
        "/screenings/single",
        json={"entity_name": "Test Org"},
    )

    assert response.status_code == 503
    data = response.json()
    assert "detail" in data
    assert "OFAC_DATA_NOT_LOADED" in str(data["detail"])

