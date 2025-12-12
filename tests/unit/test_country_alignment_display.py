"""Unit tests for country alignment display."""

from ofac.streamlit.components.results import _get_country_alignment_display


class TestGetCountryAlignmentDisplay:
    """Tests for _get_country_alignment_display() function."""

    def test_match_display(self) -> None:
        """_get_country_alignment_display() returns 'Match' when countries match."""
        alignment = _get_country_alignment_display("Syria", "Syria", True)
        assert alignment == "Match"

    def test_mismatch_display(self) -> None:
        """_get_country_alignment_display() returns 'Mismatch' when countries don't match."""
        alignment = _get_country_alignment_display("Syria", "France", False)
        assert alignment == "Mismatch"

    def test_na_no_entity_country(self) -> None:
        """_get_country_alignment_display() returns 'N/A' when entity country is missing."""
        alignment = _get_country_alignment_display(None, "Syria", False)
        assert alignment == "N/A"

    def test_na_no_ofac_country(self) -> None:
        """_get_country_alignment_display() returns 'N/A' when OFAC country is missing."""
        alignment = _get_country_alignment_display("Syria", None, False)
        assert alignment == "N/A"

    def test_na_both_missing(self) -> None:
        """_get_country_alignment_display() returns 'N/A' when both countries are missing."""
        alignment = _get_country_alignment_display(None, None, False)
        assert alignment == "N/A"

    def test_na_empty_strings(self) -> None:
        """_get_country_alignment_display() returns 'N/A' when countries are empty strings."""
        alignment = _get_country_alignment_display("", "", False)
        assert alignment == "N/A"

    def test_match_with_different_case(self) -> None:
        """_get_country_alignment_display() respects country_match flag regardless of case."""
        # Even if strings differ in case, if country_match is True, show Match
        alignment = _get_country_alignment_display("syria", "Syria", True)
        assert alignment == "Match"
