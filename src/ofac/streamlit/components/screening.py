"""Screening execution component for Streamlit application.

This module provides the screening execution UI with progress tracking
and API integration.

Usage:
    from ofac.streamlit.components.screening import render_screening

    render_screening()
"""

import io
import time

import requests
import streamlit as st

from ofac.core.config import settings
from ofac.streamlit.state import set_workflow_step


def render_screening() -> bool:
    """Render screening execution component.

    Returns:
        True if screening completed successfully, False otherwise.
    """
    st.markdown("### 🔍 Screening Execution")

    # Check prerequisites
    if (
        "file_dataframe" not in st.session_state
        or st.session_state["file_dataframe"] is None
    ):
        st.error("No file uploaded. Please go back to the upload step.")
        if st.button("Back to Upload"):
            set_workflow_step("upload")
            st.rerun()
        return False

    if "column_mapping" not in st.session_state or not st.session_state[
        "column_mapping"
    ].get("name"):
        st.error("Column mapping not configured. Please go back to the mapping step.")
        if st.button("Back to Mapping"):
            set_workflow_step("map")
            st.rerun()
        return False

    # Prepare file for API
    if (
        "uploaded_file" not in st.session_state
        or st.session_state["uploaded_file"] is None
    ):
        st.error("Uploaded file not found. Please go back to the upload step.")
        return False

    uploaded_file = st.session_state["uploaded_file"]

    # Start screening button
    if "screening_started" not in st.session_state:
        st.info("Ready to start screening. Click the button below to begin.")
        if st.button("Start Screening", type="primary"):
            st.session_state["screening_started"] = True
            st.rerun()

    if not st.session_state.get("screening_started"):
        return False

    # Execute screening
    if "screening_results" not in st.session_state:
        # Show progress
        progress_bar = st.progress(0)
        status_text = st.empty()

        try:
            status_text.text("Preparing file for screening...")
            progress_bar.progress(10)

            # Read file content
            uploaded_file.seek(0)
            file_content = uploaded_file.read()

            status_text.text("Sending request to API...")
            progress_bar.progress(30)

            # Call batch screening API
            api_url = f"http://{settings.api_host}:{settings.api_port}/screenings/batch"
            files = {
                "file": (
                    uploaded_file.name,
                    io.BytesIO(file_content),
                    uploaded_file.type,
                )
            }

            status_text.text("Processing entities...")
            progress_bar.progress(50)

            start_time = time.time()
            response = requests.post(api_url, files=files, timeout=300)

            progress_bar.progress(90)

            if response.status_code == 200:
                result_data = response.json()
                processing_time = time.time() - start_time

                status_text.text("Screening completed!")
                progress_bar.progress(100)

                # Store results
                st.session_state["screening_results"] = result_data
                st.session_state["screening_id"] = (
                    result_data.get("results", [{}])[0].get("screening_id")
                    if result_data.get("results")
                    else None
                )

                st.success(f"✅ Screening completed in {processing_time:.2f} seconds!")
                st.info(
                    f"Processed {result_data.get('total_screened', 0)} entities. "
                    f"OK: {result_data.get('ok_count', 0)}, "
                    f"REVIEW: {result_data.get('review_count', 0)}, "
                    f"NOK: {result_data.get('nok_count', 0)}"
                )

                # Advance to review step
                time.sleep(1)  # Brief pause to show completion
                set_workflow_step("review")
                st.rerun()

            else:
                error_data = response.json() if response.content else {}
                error_message = error_data.get("detail", {}).get(
                    "message", "Unknown error"
                )
                st.error(f"❌ Screening failed: {error_message}")
                progress_bar.empty()
                status_text.empty()

                if st.button("Try Again"):
                    st.session_state["screening_started"] = False
                    st.rerun()

                return False

        except requests.exceptions.ConnectionError:
            st.error("❌ Could not connect to API. Is the API server running?")
            st.info(f"Expected API URL: {api_url}")
            if st.button("Try Again"):
                st.session_state["screening_started"] = False
                st.rerun()
            return False

        except requests.exceptions.Timeout:
            st.error("❌ Screening request timed out. The file may be too large.")
            progress_bar.empty()
            status_text.empty()
            if st.button("Try Again"):
                st.session_state["screening_started"] = False
                st.rerun()
            return False

        except Exception as e:
            st.error(f"❌ Unexpected error: {str(e)}")
            progress_bar.empty()
            status_text.empty()
            if st.button("Try Again"):
                st.session_state["screening_started"] = False
                st.rerun()
            return False

    return True


__all__ = ["render_screening"]
