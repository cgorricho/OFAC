"""Custom CSS styles for Streamlit application.

This module provides CSS injection for professional styling
following the "Tasteful Minimum" design approach.

Usage:
    from ofac.streamlit.styles import inject_custom_css

    inject_custom_css()
"""

import streamlit as st


def inject_custom_css() -> None:
    """Inject custom CSS styles into Streamlit app.

    Provides minimal, professional styling following UX spec.
    """
    css = """
    <style>
        /* Status badges - only 3 classes as per UX spec */
        .status-ok {
            background-color: #d4edda;
            color: #155724;
            padding: 4px 8px;
            border-radius: 4px;
            font-weight: 500;
            font-size: 0.875rem;
        }
        
        .status-review {
            background-color: #fff3cd;
            color: #856404;
            padding: 4px 8px;
            border-radius: 4px;
            font-weight: 500;
            font-size: 0.875rem;
        }
        
        .status-nok {
            background-color: #f8d7da;
            color: #721c24;
            padding: 4px 8px;
            border-radius: 4px;
            font-weight: 500;
            font-size: 0.875rem;
        }
        
        /* Professional header styling */
        .main-header {
            border-bottom: 2px solid #4A90A4;
            padding-bottom: 1rem;
            margin-bottom: 2rem;
        }
        
        /* OFAC version badge */
        .ofac-version {
            font-size: 0.75rem;
            color: #6c757d;
            margin-top: 0.5rem;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


__all__ = ["inject_custom_css"]

