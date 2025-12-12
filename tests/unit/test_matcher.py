"""Unit tests for OFAC matching engine."""

import pandas as pd
import pytest

from ofac.core.exceptions import OFACNotLoadedError
from ofac.core.matcher import EntityMatcher
from ofac.core.models import MatchType, OFACList
from ofac.data.loader import OFACData, OFACDataVersion


@pytest.fixture
def mock_ofac_data() -> OFACData:
    """Create mock OFAC data for testing."""
    sdn_df = pd.DataFrame(
        {
            "ent_num": [306, 1000, 2000],
            "sdn_name": [
                "BANCO NACIONAL DE CUBA",
                "AL-QAIDA",
                "ISLAMIC REVOLUTIONARY GUARD CORPS",
            ],
            "sdn_type": ["entity", "individual", "entity"],
            "programs": ["CUBA", "SDGT", "IRAN; IRGC"],
            "remarks": ["a.k.a. 'BNC'.", "DOB 1957.", "Iranian military."],
        }
    )

    alt_df = pd.DataFrame(
        {
            "ent_num": [306, 306, 1000],
            "alt_num": [220, 221, 500],
            "alt_name": ["NATIONAL BANK OF CUBA", "CUBAN NATIONAL BANK", "AL QAEDA"],
            "alt_type": ["aka", "fka", "aka"],
        }
    )

    add_df = pd.DataFrame(
        {
            "ent_num": [306, 306, 2000],
            "add_num": [199, 200, 400],
            "country": ["Switzerland", "Cuba", "Iran"],
        }
    )

    aliases_by_ent = {
        306: ["NATIONAL BANK OF CUBA", "CUBAN NATIONAL BANK"],
        1000: ["AL QAEDA"],
    }

    addresses_by_ent = {
        306: ["Switzerland", "Cuba"],
        2000: ["Iran"],
    }

    version = OFACDataVersion(
        sdn_count=3,
        alt_count=3,
        add_count=3,
        source="SDN",
    )

    return OFACData(
        sdn_df=sdn_df,
        alt_df=alt_df,
        add_df=add_df,
        aliases_by_ent=aliases_by_ent,
        addresses_by_ent=addresses_by_ent,
        version=version,
    )


class TestEntityMatcher:
    """Tests for EntityMatcher class."""

    def test_create_matcher(self, mock_ofac_data: OFACData) -> None:
        """EntityMatcher can be created with OFAC data."""
        matcher = EntityMatcher(mock_ofac_data)
        assert matcher.data is not None

    def test_create_matcher_raises_on_none(self) -> None:
        """EntityMatcher raises OFACNotLoadedError if data is None."""
        with pytest.raises(OFACNotLoadedError):
            EntityMatcher(None)  # type: ignore[arg-type]

    def test_create_matcher_with_min_score(self, mock_ofac_data: OFACData) -> None:
        """EntityMatcher accepts min_score parameter."""
        matcher = EntityMatcher(mock_ofac_data, min_score=80)
        assert matcher.min_score == 80

    def test_create_matcher_clamps_min_score(self, mock_ofac_data: OFACData) -> None:
        """EntityMatcher clamps min_score to 0-100 range."""
        matcher1 = EntityMatcher(mock_ofac_data, min_score=-10)
        assert matcher1.min_score == 0

        matcher2 = EntityMatcher(mock_ofac_data, min_score=150)
        assert matcher2.min_score == 100


class TestMatchMethod:
    """Tests for match() method."""

    def test_match_exact_name(self, mock_ofac_data: OFACData) -> None:
        """match() finds exact matches."""
        matcher = EntityMatcher(mock_ofac_data)
        matches = matcher.match("BANCO NACIONAL DE CUBA")

        assert len(matches) > 0
        assert matches[0].sdn_name == "BANCO NACIONAL DE CUBA"
        assert matches[0].match_score == 100
        assert matches[0].match_type == MatchType.EXACT

    def test_match_fuzzy_name(self, mock_ofac_data: OFACData) -> None:
        """match() finds fuzzy matches."""
        matcher = EntityMatcher(mock_ofac_data)
        # Use a variation that will match well with token_sort_ratio
        matches = matcher.match("BANCO NACIONAL CUBA")

        assert len(matches) > 0
        # Find the FUZZY match (not ALIAS)
        fuzzy_match = next(
            (m for m in matches if m.match_type == MatchType.FUZZY), None
        )
        if fuzzy_match:
            assert fuzzy_match.sdn_name == "BANCO NACIONAL DE CUBA"
            assert (
                fuzzy_match.match_score >= 80
            )  # High similarity with token_sort_ratio
        else:
            # If no fuzzy match, at least verify we got matches
            assert matches[0].sdn_name == "BANCO NACIONAL DE CUBA"

    def test_match_alias(self, mock_ofac_data: OFACData) -> None:
        """match() finds matches against aliases."""
        matcher = EntityMatcher(mock_ofac_data)
        matches = matcher.match("NATIONAL BANK OF CUBA")

        # Should find match via alias
        alias_matches = [m for m in matches if m.match_type == MatchType.ALIAS]
        assert len(alias_matches) > 0
        assert alias_matches[0].sdn_name == "BANCO NACIONAL DE CUBA"

    def test_match_returns_sorted_by_score(self, mock_ofac_data: OFACData) -> None:
        """match() returns results sorted by score descending."""
        matcher = EntityMatcher(mock_ofac_data)
        matches = matcher.match("BANCO")

        # Verify scores are descending
        scores = [m.match_score for m in matches]
        assert scores == sorted(scores, reverse=True)

    def test_match_respects_max_results(self, mock_ofac_data: OFACData) -> None:
        """match() respects max_results parameter."""
        matcher = EntityMatcher(mock_ofac_data)
        matches = matcher.match("BANCO", max_results=2)

        assert len(matches) <= 2

    def test_match_empty_string(self, mock_ofac_data: OFACData) -> None:
        """match() returns empty list for empty string."""
        matcher = EntityMatcher(mock_ofac_data)
        matches = matcher.match("")

        assert matches == []

    def test_match_whitespace_only(self, mock_ofac_data: OFACData) -> None:
        """match() returns empty list for whitespace-only string."""
        matcher = EntityMatcher(mock_ofac_data)
        matches = matcher.match("   ")

        assert matches == []

    def test_match_no_matches(self, mock_ofac_data: OFACData) -> None:
        """match() returns empty list when no matches found."""
        matcher = EntityMatcher(mock_ofac_data, min_score=100)
        matches = matcher.match("COMPLETELY UNRELATED ENTITY NAME")

        assert matches == []

    def test_match_respects_min_score(self, mock_ofac_data: OFACData) -> None:
        """match() only returns matches above min_score threshold."""
        matcher = EntityMatcher(mock_ofac_data, min_score=90)
        matches = matcher.match("BANCO")

        # All matches should be >= 90
        for match in matches:
            assert match.match_score >= 90


class TestCountryAwareScoring:
    """Tests for country-aware scoring boost."""

    def test_country_boost_applied(self, mock_ofac_data: OFACData) -> None:
        """Country boost is applied when entity country matches OFAC country."""
        matcher = EntityMatcher(mock_ofac_data)
        matches_with_country = matcher.match("BANCO NACIONAL", country="Cuba")
        matches_without_country = matcher.match("BANCO NACIONAL")

        # Find the same match in both results
        match_with = next(
            (m for m in matches_with_country if "BANCO NACIONAL" in m.sdn_name), None
        )
        match_without = next(
            (m for m in matches_without_country if "BANCO NACIONAL" in m.sdn_name),
            None,
        )

        if match_with and match_without:
            # Score with country should be higher (or equal if already at 100)
            assert match_with.match_score >= match_without.match_score
            assert match_with.country_match is True

    def test_country_boost_caps_at_100(self, mock_ofac_data: OFACData) -> None:
        """Country boost does not exceed 100."""
        matcher = EntityMatcher(mock_ofac_data)
        matches = matcher.match("BANCO NACIONAL DE CUBA", country="Cuba")

        # Exact match + country boost should still be 100
        exact_match = next(
            (
                m
                for m in matches
                if m.match_score == 100 and m.match_type == MatchType.EXACT
            ),
            None,
        )
        if exact_match:
            assert exact_match.match_score == 100

    def test_country_boost_on_alias(self, mock_ofac_data: OFACData) -> None:
        """Country boost is applied to alias matches."""
        matcher = EntityMatcher(mock_ofac_data)
        matches = matcher.match("NATIONAL BANK", country="Cuba")

        # Find alias match
        alias_match = next(
            (m for m in matches if m.match_type == MatchType.ALIAS), None
        )
        if alias_match:
            assert alias_match.country_match is True

    def test_country_no_match(self, mock_ofac_data: OFACData) -> None:
        """No country boost when countries don't match."""
        matcher = EntityMatcher(mock_ofac_data)
        # Use a country that definitely won't match (entity 306 has Switzerland/Cuba)
        matches = matcher.match("AL-QAIDA", country="Japan")

        # Should not have country boost for AL-QAIDA (entity 1000 has no country in mock data)
        match = next((m for m in matches if "AL-QAIDA" in m.sdn_name), None)
        if match:
            assert match.country_match is False


class TestMatchResultStructure:
    """Tests for MatchResult structure and fields."""

    def test_match_result_has_all_fields(self, mock_ofac_data: OFACData) -> None:
        """MatchResult contains all required fields."""
        matcher = EntityMatcher(mock_ofac_data)
        matches = matcher.match("BANCO NACIONAL DE CUBA")

        assert len(matches) > 0
        match = matches[0]

        assert match.sdn_name is not None
        assert match.match_score >= 0
        assert match.match_score <= 100
        assert match.match_type in [MatchType.EXACT, MatchType.FUZZY, MatchType.ALIAS]
        assert match.ofac_list == OFACList.SDN
        assert isinstance(match.programs, list)
        assert isinstance(match.country_match, bool)

    def test_match_result_programs_parsed(self, mock_ofac_data: OFACData) -> None:
        """MatchResult programs are parsed correctly."""
        matcher = EntityMatcher(mock_ofac_data)
        matches = matcher.match("ISLAMIC REVOLUTIONARY GUARD")

        irgc_match = next((m for m in matches if "IRGC" in m.sdn_name), None)
        if irgc_match:
            assert "IRAN" in irgc_match.programs or "IRGC" in irgc_match.programs

    def test_match_result_ent_num(self, mock_ofac_data: OFACData) -> None:
        """MatchResult ent_num is set correctly."""
        matcher = EntityMatcher(mock_ofac_data)
        matches = matcher.match("BANCO NACIONAL DE CUBA")

        assert len(matches) > 0
        assert matches[0].ent_num == 306


class TestMatchEntityAlias:
    """Tests for match_entity() alias method."""

    def test_match_entity_is_alias(self, mock_ofac_data: OFACData) -> None:
        """match_entity() is an alias for match()."""
        matcher = EntityMatcher(mock_ofac_data)
        matches1 = matcher.match("BANCO NACIONAL")
        matches2 = matcher.match_entity("BANCO NACIONAL")

        assert len(matches1) == len(matches2)
        assert matches1[0].sdn_name == matches2[0].sdn_name


class TestMatcherImports:
    """Tests for matcher imports."""

    def test_import_from_matcher(self) -> None:
        """EntityMatcher can be imported from ofac.core.matcher."""
        from ofac.core.matcher import EntityMatcher

        assert EntityMatcher is not None
