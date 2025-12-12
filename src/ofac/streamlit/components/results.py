"""Results display component for Streamlit application.

This module provides the results table UI with status badges,
filtering, and expandable match details.

Usage:
    from ofac.streamlit.components.results import render_results

    render_results()
"""

import pandas as pd
import streamlit as st


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


def _get_country_alignment_display(
    entity_country: str | None, ofac_country: str | None, country_match: bool
) -> str:
    """Get country alignment display string.

    Args:
        entity_country: Entity's country (from input).
        ofac_country: OFAC entry's country.
        country_match: Whether countries match (from matcher).

    Returns:
        Display string: "Match", "Mismatch", or "N/A".
    """
    if not entity_country or not ofac_country:
        return "N/A"
    return "Match" if country_match else "Mismatch"


def render_results() -> None:
    """Render results display component."""
    st.markdown("### 📊 Screening Results")

    # Check if results exist
    if (
        "screening_results" not in st.session_state
        or st.session_state["screening_results"] is None
    ):
        st.error("No screening results available. Please run screening first.")
        if st.button("Back to Screening"):
            from ofac.streamlit.state import set_workflow_step

            set_workflow_step("screen")
            st.rerun()
        return

    results_data = st.session_state["screening_results"]

    # Import and render summary
    from ofac.streamlit.components.summary import render_summary

    render_summary()
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
            entity_country = row.get("Country", "")
            with st.expander(
                f"{row['Entity Name']} - {row['Status']} (Score: {row['Score']})"
            ):
                if row["Match Details"]:
                    for match in row["Match Details"]:
                        st.write(f"**SDN Name:** {match.get('sdn_name', 'N/A')}")
                        st.write(f"**Match Type:** {match.get('match_type', 'N/A')}")
                        st.write(f"**Score:** {match.get('match_score', 0)}")
                        st.write(
                            f"**Programs:** {', '.join(match.get('programs', []))}"
                        )

                        # Country alignment display
                        ofac_country = match.get("country")
                        country_match = match.get("country_match", False)
                        alignment = _get_country_alignment_display(
                            entity_country, ofac_country, country_match
                        )

                        st.write(f"**Input Country:** {entity_country or 'N/A'}")
                        st.write(f"**OFAC Entry Country:** {ofac_country or 'N/A'}")
                        st.write(f"**Country Alignment:** {alignment}")
                        st.divider()
                else:
                    st.info("No matches found.")


__all__ = ["render_results"]
