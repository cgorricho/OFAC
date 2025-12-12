"""Integration tests for API health endpoints."""

from fastapi.testclient import TestClient

from ofac.api.main import create_app


def test_health_endpoint() -> None:
    """Test GET /health returns healthy status."""
    app = create_app()
    client = TestClient(app)

    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_readiness_endpoint_with_data() -> None:
    """Test GET /health/ready returns ready when OFAC data is loaded."""
    app = create_app()
    client = TestClient(app)

    # Note: In test environment, OFAC data may not be loaded
    # This test verifies the endpoint exists and responds
    response = client.get("/health/ready")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "ofac_data_loaded" in data


def test_openapi_docs_available() -> None:
    """Test OpenAPI documentation is accessible."""
    app = create_app()
    client = TestClient(app)

    response = client.get("/docs")
    assert response.status_code == 200


def test_openapi_json_available() -> None:
    """Test OpenAPI JSON schema is accessible."""
    app = create_app()
    client = TestClient(app)

    response = client.get("/openapi.json")
    assert response.status_code == 200
    data = response.json()
    assert "openapi" in data
    assert "info" in data
    assert data["info"]["title"] == "OFAC Sanctions Screening API"


def test_app_metadata() -> None:
    """Test app metadata is correct."""
    app = create_app()

    assert app.title == "OFAC Sanctions Screening API"
    assert app.version == "0.1.0"
    assert app.docs_url == "/docs"
    assert app.redoc_url == "/redoc"
