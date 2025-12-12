"""File upload component for Streamlit application.

This module provides the file upload UI component with drag-and-drop
support, file validation, and preview functionality.

Usage:
    from ofac.streamlit.components.upload import render_file_upload

    if render_file_upload():
        # File uploaded, proceed to next step
"""

import streamlit as st

from ofac.core.exceptions import FileFormatError, FileParseError, FileTooLargeError
from ofac.core.file_parser import get_column_suggestions, parse_file
from ofac.streamlit.state import set_workflow_step


def render_file_upload() -> bool:
    """Render file upload component.

    Returns:
        True if file was successfully uploaded and validated, False otherwise.
    """
    st.markdown("### 📤 Upload File")

    st.markdown(
        "Upload an Excel (.xlsx, .xls) or CSV file containing organization names to screen."
    )

    uploaded_file = st.file_uploader(
        "Choose a file",
        type=["xlsx", "xls", "csv"],
        help="Supported formats: Excel (.xlsx, .xls) or CSV (.csv)",
    )

    if uploaded_file is None:
        return False

    # Validate and parse file
    try:
        file_content = uploaded_file.read()
        df = parse_file(file_content, uploaded_file.name)

        # Get column suggestions
        suggestions = get_column_suggestions(df)

        # Store in session state
        st.session_state["uploaded_file"] = uploaded_file
        st.session_state["file_dataframe"] = df
        st.session_state["column_suggestions"] = suggestions

        # Display file info
        st.success(f"✅ File uploaded: {uploaded_file.name}")
        st.info(f"📊 Rows: {len(df)}, Columns: {len(df.columns)}")

        # Show preview
        st.markdown("#### File Preview")
        st.dataframe(df.head(10), use_container_width=True)

        # Show column suggestions
        if suggestions["name_candidates"]:
            st.markdown("#### Detected Columns")
            st.write(f"**Entity Name:** {suggestions['name_candidates'][0]}")
            if suggestions["country_candidates"]:
                st.write(f"**Country:** {suggestions['country_candidates'][0]}")
            if suggestions["description_candidates"]:
                st.write(f"**Description:** {suggestions['description_candidates'][0]}")

            # Auto-set column mapping
            st.session_state["column_mapping"] = {
                "name": suggestions["name_candidates"][0],
                "country": suggestions["country_candidates"][0]
                if suggestions["country_candidates"]
                else None,
                "description": suggestions["description_candidates"][0]
                if suggestions["description_candidates"]
                else None,
            }

            # Move to mapping step
            if st.button("Continue to Column Mapping", type="primary"):
                set_workflow_step("map")
                st.rerun()

        else:
            st.warning(
                "⚠️ Could not auto-detect entity name column. "
                "You'll need to manually select columns in the next step."
            )
            st.write("**Available columns:**", ", ".join(suggestions["all_columns"]))

            # Still allow proceeding
            if st.button("Continue to Column Mapping", type="primary"):
                set_workflow_step("map")
                st.rerun()

        return True

    except FileFormatError as e:
        st.error(f"❌ Unsupported file format: {str(e)}")
        st.info("Please upload an Excel (.xlsx, .xls) or CSV (.csv) file.")
        return False

    except FileTooLargeError as e:
        st.error(f"❌ File too large: {str(e)}")
        st.info("Maximum file size: 10MB. Maximum rows: 10,000")
        return False

    except FileParseError as e:
        st.error(f"❌ Failed to parse file: {str(e)}")
        st.info("The file may be corrupted or in an unexpected format.")
        return False

    except Exception as e:
        st.error(f"❌ Unexpected error: {str(e)}")
        return False


__all__ = ["render_file_upload"]
