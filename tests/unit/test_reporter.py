"""Unit tests for report generator service."""

import io

import pytest
from openpyxl import load_workbook

from ofac.core.models import BatchScreeningResponse, EntityInput, MatchStatus, ScreeningResult
from ofac.core.reporter import ReportGenerator


@pytest.fixture
def sample_batch_response() -> BatchScreeningResponse:
    """Create sample batch response for testing."""
    results = [
        ScreeningResult(
            entity_input=EntityInput(entity_name="Test Org 1", country="US"),
            match_status=MatchStatus.OK,
            highest_score=0,
            ofac_version="2025-12-01",
        ),
        ScreeningResult(
            entity_input=EntityInput(entity_name="Test Org 2", country="SY"),
            match_status=MatchStatus.REVIEW,
            highest_score=85,
            ofac_version="2025-12-01",
        ),
    ]
    return BatchScreeningResponse(
        results=results,
        total_screened=2,
        ok_count=1,
        review_count=1,
        nok_count=0,
    )


class TestReportGenerator:
    """Tests for ReportGenerator class."""

    def test_generate_creates_workbook(self, sample_batch_response) -> None:
        """generate() creates a valid Excel workbook."""
        generator = ReportGenerator()
        workbook_bytes = generator.generate(sample_batch_response)

        # Verify it's a valid Excel file
        workbook = load_workbook(io.BytesIO(workbook_bytes))
        assert workbook is not None

    def test_generate_returns_bytes(self, sample_batch_response) -> None:
        """generate() returns bytes suitable for download."""
        generator = ReportGenerator()
        workbook_bytes = generator.generate(sample_batch_response)

        assert isinstance(workbook_bytes, bytes)
        assert len(workbook_bytes) > 0

    def test_generate_empty_results_raises_error(self) -> None:
        """generate() raises ValueError for empty results."""
        generator = ReportGenerator()
        empty_response = BatchScreeningResponse(
            results=[],
            total_screened=0,
            ok_count=0,
            review_count=0,
            nok_count=0,
        )

        with pytest.raises(ValueError, match="Cannot generate report from empty results"):
            generator.generate(empty_response)

    def test_generate_workbook_structure(self, sample_batch_response) -> None:
        """generate() creates workbook with proper structure."""
        generator = ReportGenerator()
        workbook_bytes = generator.generate(sample_batch_response)

        workbook = load_workbook(io.BytesIO(workbook_bytes))
        # Workbook should exist (sheets will be added in subsequent stories)
        assert workbook is not None

