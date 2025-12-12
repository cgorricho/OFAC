"""Update trigger component for Streamlit application.

This module provides the update button and progress tracking for
triggering OFAC data updates.

Usage:
    from ofac.streamlit.components.update import trigger_update

    trigger_update()
"""

import requests
import streamlit as st

from ofac.core.config import settings


def trigger_update() -> None:
    """Trigger OFAC data update and show progress."""
    try:
        api_url = f"http://{settings.api_host}:{settings.api_port}/data/refresh"
        with st.spinner("Updating OFAC data... This may take a few minutes."):
            response = requests.post(api_url, timeout=300)  # 5 minute timeout

        if response.status_code == 200:
            data = response.json()
            st.success("✅ OFAC data updated successfully!")
            st.info(f"New version: {data.get('version', 'Unknown')}")
            st.rerun()  # Refresh to show new freshness status
        elif response.status_code == 503:
            st.error("⚠️ Update failed. Please try again later.")
        else:
            st.error(f"⚠️ Update failed: {response.status_code}")
    except requests.exceptions.Timeout:
        st.error("⚠️ Update timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        st.error("⚠️ Cannot connect to API. Is the API server running?")
    except Exception as e:
        st.error(f"⚠️ Update failed: {str(e)}")


__all__ = ["trigger_update"]

