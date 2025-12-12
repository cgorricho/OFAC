"""Results display component for Streamlit application.

This module provides the results table UI with status badges,
filtering, and expandable match details.

Usage:
    from ofac.streamlit.components.results import render_results

    render_results()
"""

import pandas as pd
import streamlit as st

from ofac.core.models import MatchType
from ofac.core.risk import classify_risk_level
from ofac.streamlit.components.export import render_export_button


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
        for idx, row in df.iterrows():
            entity_country = row.get("Country", "")
            entity_name = row["Entity Name"]
            status = row["Status"]
            score = row["Score"]
            result_key = f"analyst_notes_{idx}"

            # Initialize notes in session state if not present
            if result_key not in st.session_state:
                st.session_state[result_key] = ""

            with st.expander(f"{entity_name} - {status} (Score: {score})"):
                if row["Match Details"]:
                    for match in row["Match Details"]:
                        # Calculate risk level
                        match_score = match.get("match_score", 0)
                        match_type_str = match.get("match_type", "FUZZY")
                        match_type = (
                            MatchType.EXACT
                            if match_type_str == "EXACT"
                            else MatchType.FUZZY
                        )
                        country_match = match.get("country_match", False)
                        risk_level = classify_risk_level(
                            match_score, match_type, country_match
                        )

                        # Risk level badge
                        risk_color = {
                            "HIGH": "red",
                            "MEDIUM": "orange",
                            "LOW": "yellow",
                        }.get(risk_level.value, "gray")
                        st.markdown(
                            f"**Risk Level:** <span style='color: {risk_color}; font-weight: bold;'>{risk_level.value}</span>",
                            unsafe_allow_html=True,
                        )

                        st.write(f"**SDN Name:** {match.get('sdn_name', 'N/A')}")
                        st.write(f"**SDN Type:** {match.get('sdn_type', 'N/A')}")
                        st.write(f"**Match Type:** {match.get('match_type', 'N/A')}")
                        st.write(f"**Match Score:** {match.get('match_score', 0)}%")
                        st.write(
                            f"**Match Algorithm:** {match.get('match_type', 'N/A')}"
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

                        # OFAC entity ID and programs
                        ent_num = match.get("ent_num")
                        if ent_num:
                            st.write(f"**OFAC Entity ID:** {ent_num}")
                        programs = match.get("programs", [])
                        if programs:
                            st.write(f"**Programs:** {', '.join(programs)}")
                        else:
                            st.write("**Programs:** N/A")

                        # General License notes
                        gl_note = row.get("General License", "N/A")
                        if gl_note and gl_note != "N/A":
                            st.write(f"**General License Notes:** {gl_note}")

                        st.divider()
                else:
                    st.info("No matches found.")

                # Analyst notes field
                st.markdown("---")
                st.markdown("**Analyst Notes:**")
                notes = st.text_area(
                    "Add notes for this review",
                    value=st.session_state[result_key],
                    key=f"notes_input_{idx}",
                    height=100,
                    help="Add notes about your review decision, context, or follow-up actions.",
                )
                st.session_state[result_key] = notes

        # Export button
        st.divider()
        render_export_button()


__all__ = ["render_results"]
