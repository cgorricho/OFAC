"""Results display component for Streamlit application.

This module provides the results table UI with status badges,
filtering, and expandable match details.

Usage:
    from ofac.streamlit.components.results import render_results

    render_results()
"""

import pandas as pd
import streamlit as st

from ofac.core.models import MatchStatus


def _get_status_badge(status: str) -> str:
    """Get HTML badge for status.

    Args:
        status: Match status (OK, REVIEW, NOK).

    Returns:
        HTML badge string.
    """
    status_lower = status.lower()
    badge_map = {
        "ok": f'<span class="status-ok">{status}</span>',
        "review": f'<span class="status-review">{status}</span>',
        "nok": f'<span class="status-nok">{status}</span>',
    }
    return badge_map.get(status_lower, status)


def render_results() -> None:
    """Render results display component."""
    st.markdown("### 📊 Screening Results")

    # Check if results exist
    if "screening_results" not in st.session_state or st.session_state["screening_results"] is None:
        st.error("No screening results available. Please run screening first.")
        if st.button("Back to Screening"):
            from ofac.streamlit.state import set_workflow_step

            set_workflow_step("screen")
            st.rerun()
        return

    results_data = st.session_state["screening_results"]

    # Summary stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Screened", results_data.get("total_screened", 0))
    with col2:
        st.metric("✅ OK", results_data.get("ok_count", 0))
    with col3:
        st.metric("⚠️ REVIEW", results_data.get("review_count", 0))
    with col4:
        st.metric("❌ NOK", results_data.get("nok_count", 0))

    st.divider()

    # Filter by status
    status_filter = st.selectbox(
        "Filter by Status",
        options=["All", "OK", "REVIEW", "NOK"],
        key="results_status_filter",
    )

    # Prepare results DataFrame
    results = results_data.get("results", [])
    if not results:
        st.info("No results to display.")
        return

    # Convert to DataFrame
    rows = []
    for result in results:
        entity_input = result.get("entity_input", {})
        match_status = result.get("match_status", "OK")
        matches = result.get("matches", [])
        highest_score = result.get("highest_score", 0)

        rows.append(
            {
                "Entity Name": entity_input.get("entity_name", ""),
                "Country": entity_input.get("country", ""),
                "Status": match_status,
                "Score": highest_score,
                "Matches": len(matches),
                "Match Details": matches,
            }
        )

    df = pd.DataFrame(rows)

    # Apply filter
    if status_filter != "All":
        df = df[df["Status"] == status_filter]

    # Display table
    st.markdown(f"#### Results ({len(df)} entities)")

    # Create display DataFrame with badges
    display_df = df[["Entity Name", "Country", "Status", "Score", "Matches"]].copy()
    display_df["Status"] = display_df["Status"].apply(_get_status_badge)

    st.markdown(display_df.to_html(escape=False, index=False), unsafe_allow_html=True)

    # Expandable match details
    if len(df) > 0:
        st.markdown("#### Match Details")
        for _idx, row in df.iterrows():
            with st.expander(f"{row['Entity Name']} - {row['Status']} (Score: {row['Score']})"):
                if row["Match Details"]:
                    for match in row["Match Details"]:
                        st.write(f"**SDN Name:** {match.get('sdn_name', 'N/A')}")
                        st.write(f"**Match Type:** {match.get('match_type', 'N/A')}")
                        st.write(f"**Score:** {match.get('match_score', 0)}")
                        st.write(f"**Programs:** {', '.join(match.get('programs', []))}")
                        if match.get("country"):
                            st.write(f"**Country:** {match.get('country')}")
                        st.divider()
                else:
                    st.info("No matches found.")


__all__ = ["render_results"]

