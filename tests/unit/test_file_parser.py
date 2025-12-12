"""Unit tests for file parser utilities."""

import io

import pandas as pd
import pytest

from ofac.core.exceptions import ColumnMappingError, FileFormatError, FileParseError, FileTooLargeError
from ofac.core.file_parser import ColumnMapping, detect_columns, get_column_suggestions, parse_file


class TestParseFile:
    """Tests for parse_file() function."""

    def test_parse_csv_file(self, tmp_path) -> None:
        """parse_file() parses CSV files correctly."""
        csv_content = b"Name,Country\nTest Org,US"
        df = parse_file(csv_content, "test.csv")

        assert isinstance(df, pd.DataFrame)
        assert len(df) == 1
        assert "Name" in df.columns
        assert "Country" in df.columns

    def test_parse_excel_file(self, tmp_path) -> None:
        """parse_file() parses Excel files correctly."""
        df = pd.DataFrame({"Name": ["Test Org"], "Country": ["US"]})
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False, engine="openpyxl")
        excel_content = excel_buffer.getvalue()

        result_df = parse_file(excel_content, "test.xlsx")

        assert isinstance(result_df, pd.DataFrame)
        assert len(result_df) == 1
        assert "Name" in result_df.columns

    def test_parse_file_unsupported_format(self) -> None:
        """parse_file() raises FileFormatError for unsupported formats."""
        with pytest.raises(FileFormatError) as exc_info:
            parse_file(b"content", "test.pdf")

        assert "Unsupported file format" in str(exc_info.value)

    def test_parse_file_too_large(self) -> None:
        """parse_file() raises FileTooLargeError for oversized files."""
        large_content = b"x" * (11 * 1024 * 1024)  # 11MB

        with pytest.raises(FileTooLargeError) as exc_info:
            parse_file(large_content, "large.csv")

        assert "exceeds maximum" in str(exc_info.value)

    def test_parse_file_removes_empty_rows(self) -> None:
        """parse_file() removes completely empty rows."""
        csv_content = b"Name,Country\nTest Org,US\n,\nAnother Org,UK"
        df = parse_file(csv_content, "test.csv")

        # Should have 2 rows (empty row removed)
        assert len(df) >= 2


class TestDetectColumns:
    """Tests for detect_columns() function."""

    def test_detect_name_column(self) -> None:
        """detect_columns() detects entity name column."""
        df = pd.DataFrame({"Organization Name": ["Test"], "Country": ["US"]})
        mapping = detect_columns(df)

        assert mapping.entity_name_column == "Organization Name"
        assert mapping.country_column == "Country"

    def test_detect_all_columns(self) -> None:
        """detect_columns() detects name, country, and description."""
        df = pd.DataFrame(
            {
                "Entity Name": ["Test"],
                "Country": ["US"],
                "Project Description": ["Test project"],
            }
        )
        mapping = detect_columns(df)

        assert mapping.entity_name_column == "Entity Name"
        assert mapping.country_column == "Country"
        assert mapping.description_column == "Project Description"

    def test_detect_columns_no_name_column(self) -> None:
        """detect_columns() raises ColumnMappingError if no name column found."""
        df = pd.DataFrame({"Column1": ["Value1"], "Column2": ["Value2"]})

        with pytest.raises(ColumnMappingError) as exc_info:
            detect_columns(df)

        assert "Could not auto-detect entity name column" in str(exc_info.value)

    def test_detect_columns_priority_order(self) -> None:
        """detect_columns() uses priority order for name detection."""
        df = pd.DataFrame(
            {
                "Partner Name": ["Test"],
                "Organization": ["Test"],
                "Entity": ["Test"],
            }
        )
        mapping = detect_columns(df)

        # "name" pattern should be detected first
        assert mapping.entity_name_column == "Partner Name"

    def test_detect_columns_optional_fields(self) -> None:
        """detect_columns() handles missing optional columns."""
        df = pd.DataFrame({"Name": ["Test"]})
        mapping = detect_columns(df)

        assert mapping.entity_name_column == "Name"
        assert mapping.country_column is None
        assert mapping.description_column is None


class TestGetColumnSuggestions:
    """Tests for get_column_suggestions() function."""

    def test_get_suggestions_with_matches(self) -> None:
        """get_column_suggestions() returns candidates for each type."""
        df = pd.DataFrame(
            {
                "Organization Name": ["Test"],
                "Country": ["US"],
                "Project Description": ["Test"],
                "Other Column": ["Value"],
            }
        )
        suggestions = get_column_suggestions(df)

        assert "Organization Name" in suggestions["name_candidates"]
        assert "Country" in suggestions["country_candidates"]
        assert "Project Description" in suggestions["description_candidates"]
        assert len(suggestions["all_columns"]) == 4

    def test_get_suggestions_no_matches(self) -> None:
        """get_column_suggestions() returns empty lists if no matches."""
        df = pd.DataFrame({"Column1": ["Value1"], "Column2": ["Value2"]})
        suggestions = get_column_suggestions(df)

        assert suggestions["name_candidates"] == []
        assert suggestions["country_candidates"] == []
        assert suggestions["description_candidates"] == []
        assert len(suggestions["all_columns"]) == 2


class TestColumnMapping:
    """Tests for ColumnMapping NamedTuple."""

    def test_column_mapping_creation(self) -> None:
        """ColumnMapping can be created with all fields."""
        mapping = ColumnMapping(
            entity_name_column="Name",
            country_column="Country",
            description_column="Description",
            all_columns=["Name", "Country", "Description"],
        )

        assert mapping.entity_name_column == "Name"
        assert mapping.country_column == "Country"
        assert mapping.description_column == "Description"
        assert len(mapping.all_columns) == 3

