"""Export component for Streamlit application.

This module provides the download button for generating and downloading
Excel reports from screening results.

Usage:
    from ofac.streamlit.components.export import render_export_button

    render_export_button()
"""

from datetime import datetime

import streamlit as st

from ofac.core.models import BatchScreeningResponse
from ofac.core.reporter import ReportGenerator


def render_export_button() -> None:
    """Render export button for downloading Excel report."""
    # Check if results exist
    if (
        "screening_results" not in st.session_state
        or st.session_state["screening_results"] is None
    ):
        st.warning("No screening results available. Please run screening first.")
        return

    results_data = st.session_state["screening_results"]

    # Convert to BatchScreeningResponse
    try:
        batch_response = BatchScreeningResponse(**results_data)
    except Exception as e:
        st.error(f"Error preparing report: {str(e)}")
        return

    # Generate report
    try:
        generator = ReportGenerator()
        report_bytes = generator.generate(batch_response)

        # Generate filename with date
        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"screening-{today}.xlsx"

        # Download button
        st.download_button(
            label="📥 Download Report",
            data=report_bytes,
            file_name=filename,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            help="Download Excel report with Summary, Details, and Exceptions sheets",
        )
    except Exception as e:
        st.error(f"Error generating report: {str(e)}")


__all__ = ["render_export_button"]

