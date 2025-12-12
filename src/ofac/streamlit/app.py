"""Main Streamlit application for OFAC Sanctions Screening.

This module provides the Streamlit web interface for batch screening
organizations against OFAC sanctions lists.

Usage:
    streamlit run src/ofac/streamlit/app.py
"""

import streamlit as st

from ofac.data.loader import OFACDataLoader
from ofac.streamlit.state import init_session_state
from ofac.streamlit.styles import inject_custom_css

# Page configuration
st.set_page_config(
    page_title="OFAC Sanctions Screening Tool",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Initialize session state
init_session_state()

# Inject custom CSS
inject_custom_css()

# Load OFAC data version
try:
    loader = OFACDataLoader()
    if loader.is_loaded:
        ofac_data = loader.data
        ofac_version = ofac_data.version.loaded_at or "unknown"
    else:
        ofac_data = loader.load()
        ofac_version = ofac_data.version.loaded_at or "unknown"
except Exception:
    ofac_version = "not loaded"

# Store in session state
st.session_state.ofac_version = ofac_version


def main() -> None:
    """Main application entry point."""
    # Header
    st.markdown('<div class="main-header">', unsafe_allow_html=True)
    st.title("🔍 OFAC Sanctions Screening Tool")
    st.markdown(
        f'<div class="ofac-version">OFAC Data Version: {ofac_version}</div>',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # Get current workflow step
    from ofac.streamlit.state import get_workflow_step

    workflow_step = get_workflow_step()

    # Route to appropriate component based on workflow step
    if workflow_step == "upload":
        from ofac.streamlit.components.upload import render_file_upload

        render_file_upload()
    elif workflow_step == "map":
        st.info("🚧 Column mapping component coming in Story 2.7...")
    elif workflow_step == "screen":
        st.info("🚧 Screening execution component coming in Story 2.8...")
    elif workflow_step == "review":
        st.info("🚧 Results display component coming in Story 2.9...")


if __name__ == "__main__":
    main()
