"""Report generation service for OFAC screening results.

This module provides the ReportGenerator class for creating Excel reports
from screening results with multiple sheets, color coding, and audit trail fields.

Usage:
    from ofac.core.reporter import ReportGenerator
    from ofac.core.models import BatchScreeningResponse

    generator = ReportGenerator()
    workbook_bytes = generator.generate(batch_response)
"""

import io
from typing import TYPE_CHECKING

from openpyxl import Workbook

if TYPE_CHECKING:
    from ofac.core.models import BatchScreeningResponse


class ReportGenerator:
    """Generates Excel reports from OFAC screening results.

    Creates multi-sheet Excel workbooks with:
    - Summary sheet with statistics
    - Detailed results sheet
    - Exceptions sheet (REVIEW/NOK only)
    - Color coding and professional formatting
    - Complete audit trail fields

    Attributes:
        workbook: The openpyxl Workbook instance

    Example:
        generator = ReportGenerator()
        workbook_bytes = generator.generate(batch_response)
        with open("report.xlsx", "wb") as f:
            f.write(workbook_bytes)
    """

    def __init__(self) -> None:
        """Initialize the report generator."""
        self.workbook: Workbook | None = None

    def generate(self, batch_response: "BatchScreeningResponse") -> bytes:
        """Generate Excel report from batch screening results.

        Args:
            batch_response: BatchScreeningResponse containing all screening results.

        Returns:
            bytes: Excel workbook as bytes for download.

        Raises:
            ValueError: If batch_response is empty or invalid.
        """
        if not batch_response.results:
            raise ValueError("Cannot generate report from empty results")

        self.workbook = Workbook()
        # Remove default sheet, we'll create our own
        default_sheet = self.workbook.active
        self.workbook.remove(default_sheet)

        # Generate sheets
        self._create_summary_sheet(batch_response)

        # Save to bytes
        output = io.BytesIO()
        self.workbook.save(output)
        output.seek(0)
        return output.read()

    def _create_summary_sheet(self, batch_response: "BatchScreeningResponse") -> None:
        """Create Summary sheet with statistics.

        Args:
            batch_response: BatchScreeningResponse containing screening results.
        """
        sheet = self.workbook.create_sheet("Summary")

        # Header
        sheet.append(["OFAC Screening Report - Summary"])
        sheet.append([])  # Empty row

        # Screening metadata
        sheet.append(["Screening Information"])
        if batch_response.results:
            first_result = batch_response.results[0]
            sheet.append(["Screening ID", first_result.screening_id])
            sheet.append(
                ["Screening Date", first_result.timestamp.strftime("%Y-%m-%d")]
            )
            sheet.append(
                ["Screening Time", first_result.timestamp.strftime("%H:%M:%S UTC")]
            )
            sheet.append(["OFAC Data Version", first_result.ofac_version or "Unknown"])
        else:
            sheet.append(["Screening ID", "N/A"])
            sheet.append(["Screening Date", "N/A"])
            sheet.append(["Screening Time", "N/A"])
            sheet.append(
                ["OFAC Data Version", batch_response.ofac_version or "Unknown"]
            )

        sheet.append([])  # Empty row

        # Statistics
        sheet.append(["Screening Statistics"])
        sheet.append(["Total Entities Screened", batch_response.total_screened])
        sheet.append([])  # Empty row

        # Status breakdown
        sheet.append(["Status Breakdown"])
        sheet.append(["Status", "Count", "Percentage"])

        total = batch_response.total_screened
        if total > 0:
            ok_pct = (batch_response.ok_count / total) * 100
            review_pct = (batch_response.review_count / total) * 100
            nok_pct = (batch_response.nok_count / total) * 100
        else:
            ok_pct = review_pct = nok_pct = 0.0

        sheet.append(["OK", batch_response.ok_count, f"{ok_pct:.1f}%"])
        sheet.append(["REVIEW", batch_response.review_count, f"{review_pct:.1f}%"])
        sheet.append(["NOK", batch_response.nok_count, f"{nok_pct:.1f}%"])

        # Auto-adjust column widths
        sheet.column_dimensions["A"].width = 25
        sheet.column_dimensions["B"].width = 15
        sheet.column_dimensions["C"].width = 15

    def _create_details_sheet(self, batch_response: "BatchScreeningResponse") -> None:
        """Create Detailed Results sheet (to be implemented in Story 4.3)."""
        pass  # Placeholder

    def _create_exceptions_sheet(
        self, batch_response: "BatchScreeningResponse"
    ) -> None:
        """Create Exceptions sheet (to be implemented in Story 4.4)."""
        pass  # Placeholder


__all__ = ["ReportGenerator"]
