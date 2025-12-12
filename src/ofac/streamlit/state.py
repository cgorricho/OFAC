"""Session state management for Streamlit application.

This module provides utilities for managing Streamlit session state
according to the architecture-defined schema.

Usage:
    from ofac.streamlit.state import init_session_state, get_workflow_step

    init_session_state()
    step = get_workflow_step()
"""

from typing import Literal

import streamlit as st

WorkflowStep = Literal["upload", "map", "screen", "review"]


def init_session_state() -> None:
    """Initialize session state with default values.

    Sets up all required session state keys according to architecture schema.
    """
    if "workflow_step" not in st.session_state:
        st.session_state["workflow_step"] = "upload"

    if "uploaded_file" not in st.session_state:
        st.session_state["uploaded_file"] = None

    if "column_mapping" not in st.session_state:
        st.session_state["column_mapping"] = {
            "name": None,
            "country": None,
            "description": None,
        }

    if "screening_results" not in st.session_state:
        st.session_state["screening_results"] = None

    if "ofac_version" not in st.session_state:
        st.session_state["ofac_version"] = "unknown"

    if "screening_id" not in st.session_state:
        st.session_state["screening_id"] = None


def get_workflow_step() -> WorkflowStep:
    """Get current workflow step.

    Returns:
        Current workflow step.
    """
    step = st.session_state.get("workflow_step", "upload")
    if isinstance(step, str) and step in ["upload", "map", "screen", "review"]:
        return step  # type: ignore[return-value]
    return "upload"


def set_workflow_step(step: WorkflowStep) -> None:
    """Set workflow step.

    Args:
        step: New workflow step.
    """
    st.session_state["workflow_step"] = step


def reset_session_state() -> None:
    """Reset session state to initial values."""
    st.session_state["workflow_step"] = "upload"
    st.session_state["uploaded_file"] = None
    st.session_state["column_mapping"] = {"name": None, "country": None, "description": None}
    st.session_state["screening_results"] = None
    st.session_state["screening_id"] = None


__all__ = [
    "init_session_state",
    "get_workflow_step",
    "set_workflow_step",
    "reset_session_state",
    "WorkflowStep",
]

