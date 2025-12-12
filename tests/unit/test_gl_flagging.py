"""Unit tests for General License flagging logic."""

import pytest

from ofac.core.classifier import classify_with_gl_context
from ofac.core.models import MatchResult, MatchStatus, MatchType, OFACList


@pytest.fixture
def high_score_matches() -> list[MatchResult]:
    """Create matches with high score (NOK threshold)."""
    return [
        MatchResult(
            sdn_name="SYRIAN ENTITY",
            sdn_type="entity",
            match_score=95,
            match_type=MatchType.FUZZY,
            ofac_list=OFACList.SDN,
            programs=["SYRIA"],
            ent_num=1,
            country="Syria",
        )
    ]


@pytest.fixture
def medium_score_matches() -> list[MatchResult]:
    """Create matches with medium score (REVIEW threshold)."""
    return [
        MatchResult(
            sdn_name="TEST ENTITY",
            sdn_type="entity",
            match_score=85,
            match_type=MatchType.FUZZY,
            ofac_list=OFACList.SDN,
            programs=[],
            ent_num=1,
        )
    ]


class TestGeneralLicenseFlagging:
    """Tests for General License flagging logic."""

    def test_syria_with_humanitarian_keywords_review(self, high_score_matches) -> None:
        """High score in Syria with humanitarian keywords → REVIEW with GL-21."""
        status, is_humanitarian, gl_note = classify_with_gl_context(
            highest_score=95,
            matches=high_score_matches,
            entity_country="SY",
            description="Emergency medical supplies for Syria",
        )

        assert status == MatchStatus.REVIEW
        assert is_humanitarian is True
        assert gl_note is not None
        assert "GL-21" in gl_note
        assert "emergency" in gl_note.lower() or "medical" in gl_note.lower()

    def test_syria_without_humanitarian_keywords_nok(self, high_score_matches) -> None:
        """High score in Syria WITHOUT humanitarian keywords → NOK."""
        status, is_humanitarian, gl_note = classify_with_gl_context(
            highest_score=95,
            matches=high_score_matches,
            entity_country="SY",
            description="Banking services in Damascus",
        )

        assert status == MatchStatus.NOK
        assert is_humanitarian is False
        assert gl_note is None

    def test_iran_with_humanitarian_keywords_review(self) -> None:
        """High score in Iran with humanitarian keywords → REVIEW with GL D-1."""
        iran_matches = [
            MatchResult(
                sdn_name="IRANIAN ENTITY",
                sdn_type="entity",
                match_score=95,
                match_type=MatchType.FUZZY,
                ofac_list=OFACList.SDN,
                programs=["IRAN"],
                ent_num=2,
                country="Iran",
            )
        ]

        status, is_humanitarian, gl_note = classify_with_gl_context(
            highest_score=95,
            matches=iran_matches,
            entity_country="IR",
            description="Humanitarian aid and food assistance",
        )

        assert status == MatchStatus.REVIEW
        assert is_humanitarian is True
        assert gl_note is not None
        assert "GL D-1" in gl_note

    def test_non_sanctioned_country_nok(self, high_score_matches) -> None:
        """High score in non-sanctioned country → NOK (no GL)."""
        status, is_humanitarian, gl_note = classify_with_gl_context(
            highest_score=95,
            matches=high_score_matches,
            entity_country="US",
            description="Emergency medical supplies",
        )

        assert status == MatchStatus.NOK
        assert is_humanitarian is True  # Keywords detected but no GL
        assert gl_note is None  # No GL for non-sanctioned countries

    def test_review_threshold_stays_review(self, medium_score_matches) -> None:
        """Medium score (REVIEW threshold) stays REVIEW regardless of GL."""
        status, is_humanitarian, gl_note = classify_with_gl_context(
            highest_score=85,
            matches=medium_score_matches,
            entity_country="SY",
            description="Emergency medical supplies",
        )

        assert status == MatchStatus.REVIEW
        # GL note may or may not be present depending on implementation
        # The key is that status is REVIEW

    def test_ok_score_stays_ok(self) -> None:
        """Low score stays OK regardless of country or keywords."""
        low_matches = [
            MatchResult(
                sdn_name="TEST ENTITY",
                sdn_type="entity",
                match_score=75,
                match_type=MatchType.FUZZY,
                ofac_list=OFACList.SDN,
                programs=[],
                ent_num=1,
            )
        ]

        status, is_humanitarian, gl_note = classify_with_gl_context(
            highest_score=75,
            matches=low_matches,
            entity_country="SY",
            description="Emergency medical supplies",
        )

        assert status == MatchStatus.OK
        assert is_humanitarian is True
        assert gl_note is None  # No GL for OK scores

    def test_no_matches_returns_ok(self) -> None:
        """No matches returns OK."""
        status, is_humanitarian, gl_note = classify_with_gl_context(
            highest_score=0,
            matches=[],
            entity_country="SY",
            description="Emergency medical supplies",
        )

        assert status == MatchStatus.OK
        # Humanitarian keywords detected in description
        assert is_humanitarian is True
        assert gl_note is None  # No GL note for OK status (no matches to flag)

    def test_venezuela_with_humanitarian_keywords(self) -> None:
        """Venezuela with humanitarian keywords → REVIEW with GL-41."""
        ve_matches = [
            MatchResult(
                sdn_name="VENEZUELAN ENTITY",
                sdn_type="entity",
                match_score=95,
                match_type=MatchType.FUZZY,
                ofac_list=OFACList.SDN,
                programs=["VENEZUELA"],
                ent_num=3,
                country="Venezuela",
            )
        ]

        status, is_humanitarian, gl_note = classify_with_gl_context(
            highest_score=95,
            matches=ve_matches,
            entity_country="VE",
            description="Food aid and medical assistance",
        )

        assert status == MatchStatus.REVIEW
        assert is_humanitarian is True
        assert gl_note is not None
        assert "GL-41" in gl_note

