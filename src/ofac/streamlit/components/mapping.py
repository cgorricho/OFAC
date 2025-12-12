"""Column mapping component for Streamlit application.

This module provides the column mapping UI where users can confirm
or correct auto-detected column mappings.

Usage:
    from ofac.streamlit.components.mapping import render_column_mapping

    if render_column_mapping():
        # Mapping confirmed, proceed to screening
"""

import streamlit as st

from ofac.core.exceptions import ColumnMappingError
from ofac.core.file_parser import detect_columns
from ofac.streamlit.state import set_workflow_step


def render_column_mapping() -> bool:
    """Render column mapping component.

    Returns:
        True if mapping was confirmed, False otherwise.
    """
    st.markdown("### 📋 Column Mapping")

    # Check if file is uploaded
    if (
        "file_dataframe" not in st.session_state
        or st.session_state["file_dataframe"] is None
    ):
        st.error("No file uploaded. Please go back to the upload step.")
        if st.button("Back to Upload"):
            set_workflow_step("upload")
            st.rerun()
        return False

    df = st.session_state["file_dataframe"]
    all_columns = df.columns.tolist()

    # Try to auto-detect columns
    try:
        column_mapping = detect_columns(df)
        st.success("✅ Columns auto-detected successfully!")
    except ColumnMappingError:
        column_mapping = None
        st.warning(
            "⚠️ Could not auto-detect all required columns. Please select manually."
        )

    # Entity name column (required)
    st.markdown("#### Entity Name Column (Required)")
    if column_mapping:
        default_name_idx = (
            all_columns.index(column_mapping.entity_name_column)
            if column_mapping.entity_name_column in all_columns
            else 0
        )
    else:
        default_name_idx = 0

    name_column = st.selectbox(
        "Select the column containing organization names",
        options=all_columns,
        index=default_name_idx,
        key="mapping_name_column",
        help="This column will be used for OFAC screening",
    )

    # Country column (optional)
    st.markdown("#### Country Column (Optional)")
    country_options = [None] + all_columns
    if column_mapping and column_mapping.country_column:
        default_country = column_mapping.country_column
        default_country_idx = (
            country_options.index(default_country)
            if default_country in country_options
            else 0
        )
    else:
        default_country_idx = 0

    country_column = st.selectbox(
        "Select the column containing countries (optional)",
        options=country_options,
        index=default_country_idx,
        key="mapping_country_column",
        help="Country information helps improve match accuracy",
    )

    # Description column (optional)
    st.markdown("#### Description Column (Optional)")
    if column_mapping and column_mapping.description_column:
        default_desc = column_mapping.description_column
        default_desc_idx = (
            country_options.index(default_desc)
            if default_desc in country_options
            else 0
        )
    else:
        default_desc_idx = 0

    description_column = st.selectbox(
        "Select the column containing descriptions (optional)",
        options=country_options,
        index=default_desc_idx,
        key="mapping_description_column",
        help="Description helps with humanitarian context detection",
    )

    # Validate mapping
    if not name_column:
        st.error("❌ Entity name column is required!")
        return False

    # Save mapping
    if st.button("Confirm Mapping", type="primary"):
        st.session_state["column_mapping"] = {
            "name": name_column,
            "country": country_column if country_column else None,
            "description": description_column if description_column else None,
        }

        st.success("✅ Column mapping confirmed!")
        st.info("Ready to proceed to screening.")

        # Advance to screening step
        if st.button("Start Screening", type="primary"):
            set_workflow_step("screen")
            st.rerun()

        return True

    # Show preview of selected columns
    if name_column:
        st.markdown("#### Mapping Preview")
        preview_df = df[
            [name_column] + ([c for c in [country_column, description_column] if c])
        ].head(5)
        st.dataframe(preview_df, use_container_width=True)

    return False


__all__ = ["render_column_mapping"]
