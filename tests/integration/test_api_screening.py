"""Integration tests for screening API endpoints."""

import io

import pandas as pd
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


class TestBatchScreening:
    """Tests for batch screening endpoint."""

    def test_batch_screening_with_csv(self, mock_ofac_data_dir) -> None:
        """Test POST /screenings/batch with CSV file."""
        loader = OFACDataLoader(data_path=mock_ofac_data_dir)
        data = loader.load()

        app = create_app()
        app.state.ofac_data = data
        app.state.ofac_loader = loader

        client = TestClient(app)

        # Create test CSV
        csv_content = "Organization Name,Country\nBANCO NACIONAL DE CUBA,Cuba\nTest Org,US"
        files = {"file": ("test.csv", io.BytesIO(csv_content.encode()), "text/csv")}

        response = client.post("/screenings/batch", files=files)

        assert response.status_code == 200
        result = response.json()
        assert "results" in result
        assert result["total_screened"] == 2
        assert result["ok_count"] + result["review_count"] + result["nok_count"] == 2
        # All results should have same screening_id
        screening_ids = {r["screening_id"] for r in result["results"]}
        assert len(screening_ids) == 1

    def test_batch_screening_with_excel(self, mock_ofac_data_dir) -> None:
        """Test POST /screenings/batch with Excel file."""
        loader = OFACDataLoader(data_path=mock_ofac_data_dir)
        data = loader.load()

        app = create_app()
        app.state.ofac_data = data
        app.state.ofac_loader = loader

        client = TestClient(app)

        # Create test Excel
        df = pd.DataFrame(
            {
                "Organization Name": ["BANCO NACIONAL DE CUBA", "Test Org"],
                "Country": ["Cuba", "US"],
            }
        )
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False, engine="openpyxl")
        excel_buffer.seek(0)

        files = {
            "file": (
                "test.xlsx",
                excel_buffer,
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
        }

        response = client.post("/screenings/batch", files=files)

        assert response.status_code == 200
        result = response.json()
        assert result["total_screened"] == 2

    def test_batch_screening_file_too_large(self, mock_ofac_data_dir) -> None:
        """Test batch screening with file exceeding size limit."""
        loader = OFACDataLoader(data_path=mock_ofac_data_dir)
        data = loader.load()

        app = create_app()
        app.state.ofac_data = data
        app.state.ofac_loader = loader

        client = TestClient(app)

        # Create large file (11MB)
        large_content = b"x" * (11 * 1024 * 1024)
        files = {"file": ("large.csv", io.BytesIO(large_content), "text/csv")}

        response = client.post("/screenings/batch", files=files)

        assert response.status_code == 413
        data = response.json()
        assert "FILE_TOO_LARGE" in str(data["detail"])

    def test_batch_screening_unsupported_format(self, mock_ofac_data_dir) -> None:
        """Test batch screening with unsupported file format."""
        loader = OFACDataLoader(data_path=mock_ofac_data_dir)
        data = loader.load()

        app = create_app()
        app.state.ofac_data = data
        app.state.ofac_loader = loader

        client = TestClient(app)

        files = {"file": ("test.pdf", io.BytesIO(b"PDF content"), "application/pdf")}

        response = client.post("/screenings/batch", files=files)

        assert response.status_code == 400
        data = response.json()
        assert "FILE_INVALID_FORMAT" in str(data["detail"])

    def test_batch_screening_no_name_column(self, mock_ofac_data_dir) -> None:
        """Test batch screening with file missing name column."""
        loader = OFACDataLoader(data_path=mock_ofac_data_dir)
        data = loader.load()

        app = create_app()
        app.state.ofac_data = data
        app.state.ofac_loader = loader

        client = TestClient(app)

        # CSV with no recognizable name column
        csv_content = "Column1,Column2\nValue1,Value2"
        files = {"file": ("test.csv", io.BytesIO(csv_content.encode()), "text/csv")}

        response = client.post("/screenings/batch", files=files)

        assert response.status_code == 400
        data = response.json()
        assert "FILE_COLUMN_MAPPING_ERROR" in str(data["detail"])

