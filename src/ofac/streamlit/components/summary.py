"""Summary dashboard component for Streamlit application.

This module provides the summary statistics dashboard showing
overview of screening results.

Usage:
    from ofac.streamlit.components.summary import render_summary

    render_summary()
"""

import streamlit as st


def render_summary() -> None:
    """Render summary dashboard component."""
    st.markdown("### 📈 Summary Dashboard")

    # Check if results exist
    if "screening_results" not in st.session_state or st.session_state["screening_results"] is None:
        st.info("No screening results available. Run screening to see summary.")
        return

    results_data = st.session_state["screening_results"]

    # Calculate statistics
    total = results_data.get("total_screened", 0)
    ok_count = results_data.get("ok_count", 0)
    review_count = results_data.get("review_count", 0)
    nok_count = results_data.get("nok_count", 0)

    # Calculate percentages
    ok_pct = (ok_count / total * 100) if total > 0 else 0
    review_pct = (review_count / total * 100) if total > 0 else 0
    nok_pct = (nok_count / total * 100) if total > 0 else 0

    # Display metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Screened", total)
    with col2:
        st.metric("✅ OK", f"{ok_count} ({ok_pct:.1f}%)")
    with col3:
        st.metric("⚠️ REVIEW", f"{review_count} ({review_pct:.1f}%)")
    with col4:
        st.metric("❌ NOK", f"{nok_count} ({nok_pct:.1f}%)")

    st.divider()

    # Exceptions summary
    exceptions = review_count + nok_count
    exceptions_pct = (exceptions / total * 100) if total > 0 else 0

    if exceptions > 0:
        st.warning(f"⚠️ {exceptions} exceptions require review ({exceptions_pct:.1f}%)")
    else:
        st.success("✅ All entities cleared - no exceptions found!")

    # Metadata
    st.markdown("#### Screening Metadata")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Screening ID:** {st.session_state.get('screening_id', 'N/A')}")
        st.write(f"**OFAC Version:** {st.session_state.get('ofac_version', 'unknown')}")
    with col2:
        processing_time = results_data.get("processing_time_ms", 0)
        st.write(f"**Processing Time:** {processing_time}ms ({processing_time/1000:.2f}s)")
        ofac_version = results_data.get("ofac_version", "unknown")
        st.write(f"**OFAC Data Version:** {ofac_version}")


__all__ = ["render_summary"]

