"""Unit tests for report generator service."""

import io

import pytest
from openpyxl import load_workbook

from ofac.core.models import (
    BatchScreeningResponse,
    EntityInput,
    MatchResult,
    MatchStatus,
    MatchType,
    OFACList,
    ScreeningResult,
)
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
            matches=[],
        ),
        ScreeningResult(
            entity_input=EntityInput(entity_name="Test Org 2", country="SY"),
            match_status=MatchStatus.REVIEW,
            highest_score=85,
            ofac_version="2025-12-01",
            matches=[
                MatchResult(
                    sdn_name="TEST ENTITY",
                    sdn_type="entity",
                    match_score=85,
                    match_type=MatchType.FUZZY,
                    ofac_list=OFACList.SDN,
                    programs=[],
                    ent_num=1,
                    country="Syria",
                    country_match=True,
                )
            ],
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

        with pytest.raises(
            ValueError, match="Cannot generate report from empty results"
        ):
            generator.generate(empty_response)

    def test_generate_workbook_structure(self, sample_batch_response) -> None:
        """generate() creates workbook with proper structure."""
        generator = ReportGenerator()
        workbook_bytes = generator.generate(sample_batch_response)

        workbook = load_workbook(io.BytesIO(workbook_bytes))
        # Workbook should exist with Summary sheet
        assert workbook is not None
        assert "Summary" in workbook.sheetnames

    def test_summary_sheet_contains_metadata(self, sample_batch_response) -> None:
        """Summary sheet contains screening metadata."""
        generator = ReportGenerator()
        workbook_bytes = generator.generate(sample_batch_response)

        workbook = load_workbook(io.BytesIO(workbook_bytes))
        sheet = workbook["Summary"]

        # Check for key metadata
        cell_values = [cell.value for row in sheet.iter_rows() for cell in row]
        assert "OFAC Screening Report - Summary" in cell_values
        assert "Screening ID" in cell_values
        assert "Total Entities Screened" in cell_values
        assert "Status Breakdown" in cell_values

    def test_summary_sheet_contains_statistics(self, sample_batch_response) -> None:
        """Summary sheet contains status breakdown."""
        generator = ReportGenerator()
        workbook_bytes = generator.generate(sample_batch_response)

        workbook = load_workbook(io.BytesIO(workbook_bytes))
        sheet = workbook["Summary"]

        # Check for status breakdown
        cell_values = [cell.value for row in sheet.iter_rows() for cell in row]
        assert "OK" in cell_values
        assert "REVIEW" in cell_values
        assert "NOK" in cell_values or 0 in cell_values  # NOK count might be 0

    def test_details_sheet_exists(self, sample_batch_response) -> None:
        """Details sheet is created in workbook."""
        generator = ReportGenerator()
        workbook_bytes = generator.generate(sample_batch_response)

        workbook = load_workbook(io.BytesIO(workbook_bytes))
        assert "All Results" in workbook.sheetnames

    def test_details_sheet_contains_headers(self, sample_batch_response) -> None:
        """Details sheet contains expected column headers."""
        generator = ReportGenerator()
        workbook_bytes = generator.generate(sample_batch_response)

        workbook = load_workbook(io.BytesIO(workbook_bytes))
        sheet = workbook["All Results"]

        # Check headers
        headers = [cell.value for cell in sheet[1]]
        assert "Row #" in headers
        assert "Organization Name" in headers
        assert "Status" in headers
        assert "Match Score" in headers

    def test_details_sheet_contains_data(self, sample_batch_response) -> None:
        """Details sheet contains screening result data."""
        generator = ReportGenerator()
        workbook_bytes = generator.generate(sample_batch_response)

        workbook = load_workbook(io.BytesIO(workbook_bytes))
        sheet = workbook["All Results"]

        # Should have header row + 2 data rows
        assert sheet.max_row == 3
        # Check that data rows contain organization names
        cell_values = [cell.value for row in sheet.iter_rows(min_row=2) for cell in row]
        assert "Test Org 1" in cell_values
        assert "Test Org 2" in cell_values
