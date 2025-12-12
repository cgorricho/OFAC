"""Unit tests for sanctioned countries registry."""

from ofac.core.countries import (
    get_all_sanctioned_countries,
    get_countries_with_gl,
    get_general_license,
    is_sanctioned_country,
)


class TestIsSanctionedCountry:
    """Tests for is_sanctioned_country() function."""

    def test_syria_is_sanctioned(self) -> None:
        """is_sanctioned_country() returns True for Syria."""
        assert is_sanctioned_country("SY") is True
        assert is_sanctioned_country("sy") is True  # Case insensitive

    def test_iran_is_sanctioned(self) -> None:
        """is_sanctioned_country() returns True for Iran."""
        assert is_sanctioned_country("IR") is True

    def test_cuba_is_sanctioned(self) -> None:
        """is_sanctioned_country() returns True for Cuba."""
        assert is_sanctioned_country("CU") is True

    def test_north_korea_is_sanctioned(self) -> None:
        """is_sanctioned_country() returns True for North Korea."""
        assert is_sanctioned_country("KP") is True

    def test_venezuela_is_sanctioned(self) -> None:
        """is_sanctioned_country() returns True for Venezuela."""
        assert is_sanctioned_country("VE") is True

    def test_us_is_not_sanctioned(self) -> None:
        """is_sanctioned_country() returns False for non-sanctioned countries."""
        assert is_sanctioned_country("US") is False
        assert is_sanctioned_country("FR") is False
        assert is_sanctioned_country("GB") is False

    def test_empty_string_returns_false(self) -> None:
        """is_sanctioned_country() returns False for empty string."""
        assert is_sanctioned_country("") is False

    def test_case_insensitive(self) -> None:
        """is_sanctioned_country() is case-insensitive."""
        assert is_sanctioned_country("sy") == is_sanctioned_country("SY")
        assert is_sanctioned_country("Sy") == is_sanctioned_country("SY")


class TestGetGeneralLicense:
    """Tests for get_general_license() function."""

    def test_get_gl_for_syria(self) -> None:
        """get_general_license() returns GL-21 for Syria."""
        gl = get_general_license("SY")
        assert gl is not None
        assert gl.code == "GL-21"
        assert "Syria" in gl.description
        assert "SY" in gl.applicable_countries

    def test_get_gl_for_iran(self) -> None:
        """get_general_license() returns GL D-1 for Iran."""
        gl = get_general_license("IR")
        assert gl is not None
        assert gl.code == "GL D-1"
        assert "Iran" in gl.description

    def test_get_gl_for_venezuela(self) -> None:
        """get_general_license() returns GL-41 for Venezuela."""
        gl = get_general_license("VE")
        assert gl is not None
        assert gl.code == "GL-41"
        assert "Venezuela" in gl.description

    def test_get_gl_for_cuba(self) -> None:
        """get_general_license() returns GL-21 for Cuba."""
        gl = get_general_license("CU")
        assert gl is not None
        assert gl.code == "GL-21"
        assert "Cuba" in gl.description

    def test_get_gl_for_non_gl_country(self) -> None:
        """get_general_license() returns None for countries without GL."""
        assert get_general_license("KP") is None  # North Korea has no GL
        assert get_general_license("US") is None

    def test_get_gl_case_insensitive(self) -> None:
        """get_general_license() is case-insensitive."""
        gl1 = get_general_license("sy")
        gl2 = get_general_license("SY")
        assert gl1 == gl2

    def test_get_gl_empty_string(self) -> None:
        """get_general_license() returns None for empty string."""
        assert get_general_license("") is None


class TestGetAllSanctionedCountries:
    """Tests for get_all_sanctioned_countries() function."""

    def test_returns_copy_of_set(self) -> None:
        """get_all_sanctioned_countries() returns a copy of the set."""
        countries = get_all_sanctioned_countries()
        assert isinstance(countries, set)
        assert "SY" in countries
        assert "IR" in countries
        assert "CU" in countries

    def test_modification_does_not_affect_original(self) -> None:
        """Modifying returned set does not affect original."""
        countries = get_all_sanctioned_countries()
        countries.add("XX")
        assert "XX" not in get_all_sanctioned_countries()


class TestGetCountriesWithGL:
    """Tests for get_countries_with_gl() function."""

    def test_returns_list_of_countries(self) -> None:
        """get_countries_with_gl() returns list of countries with GL."""
        countries = get_countries_with_gl()
        assert isinstance(countries, list)
        assert "SY" in countries
        assert "IR" in countries
        assert "VE" in countries
        assert "CU" in countries

    def test_does_not_include_countries_without_gl(self) -> None:
        """get_countries_with_gl() does not include countries without GL."""
        countries = get_countries_with_gl()
        # North Korea is sanctioned but has no GL
        assert "KP" not in countries
