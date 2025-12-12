"""Freshness indicator component for Streamlit application.

This module provides the freshness status display showing OFAC data age
and freshness status with color-coded indicators.

Usage:
    from ofac.streamlit.components.freshness import render_freshness_indicator

    render_freshness_indicator()
"""

import requests
import streamlit as st

from ofac.core.config import settings


def render_freshness_indicator() -> None:
    """Render OFAC data freshness indicator in header."""
    try:
        # Fetch freshness status from API
        api_url = f"http://{settings.api_host}:{settings.api_port}/data/status"
        response = requests.get(api_url, timeout=5)

        if response.status_code == 200:
            data = response.json()
            freshness_status = data.get("freshness_status", "UNKNOWN")
            age_days = data.get("age_days", 0)
            last_updated = data.get("last_updated", "Unknown")

            # Color coding based on status
            if freshness_status == "CURRENT":
                color = "🟢"
                badge_color = "green"
            elif freshness_status == "STALE":
                color = "🟡"
                badge_color = "orange"
            else:  # CRITICAL
                color = "🔴"
                badge_color = "red"

            # Display indicator
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(
                    f"""
                    <div style="padding: 0.5rem; background-color: #f0f2f6; border-radius: 0.25rem; margin-bottom: 1rem;">
                        <strong>OFAC Data:</strong>
                        <span style="color: {badge_color}; font-weight: bold;">{color} {freshness_status}</span>
                        ({age_days} days old)
                        <span style="font-size: 0.85em; color: #666; margin-left: 0.5rem;">
                            Last updated: {last_updated.split("T")[0] if "T" in str(last_updated) else last_updated}
                        </span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with col2:
                if st.button("🔄 Update OFAC Data", key="update_ofac_data"):
                    from ofac.streamlit.components.update import trigger_update

                    trigger_update()
        else:
            st.warning("⚠️ Unable to fetch OFAC data freshness status")
    except Exception:
        # If API is not available, show warning
        st.warning("⚠️ OFAC data freshness status unavailable")


__all__ = ["render_freshness_indicator"]
