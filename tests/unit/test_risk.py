"""Unit tests for risk level classification."""

from ofac.core.models import MatchType
from ofac.core.risk import RiskLevel, classify_risk_level


class TestRiskLevel:
    """Tests for RiskLevel enum."""

    def test_enum_values(self) -> None:
        """RiskLevel has correct values."""
        assert RiskLevel.HIGH.value == "HIGH"
        assert RiskLevel.MEDIUM.value == "MEDIUM"
        assert RiskLevel.LOW.value == "LOW"


class TestClassifyRiskLevel:
    """Tests for classify_risk_level function."""

    def test_exact_match_returns_high(self) -> None:
        """Exact match always returns HIGH risk."""
        risk = classify_risk_level(
            score=50, match_type=MatchType.EXACT, country_match=False
        )
        assert risk == RiskLevel.HIGH

    def test_high_score_with_country_match_returns_high(self) -> None:
        """Score >= 90 with country match returns HIGH risk."""
        risk = classify_risk_level(
            score=95, match_type=MatchType.FUZZY, country_match=True
        )
        assert risk == RiskLevel.HIGH

    def test_high_score_without_country_match_returns_medium(self) -> None:
        """Score >= 90 without country match returns MEDIUM risk."""
        risk = classify_risk_level(
            score=95, match_type=MatchType.FUZZY, country_match=False
        )
        assert risk == RiskLevel.MEDIUM

    def test_medium_score_returns_medium(self) -> None:
        """Score >= 70 returns MEDIUM risk."""
        risk = classify_risk_level(
            score=75, match_type=MatchType.FUZZY, country_match=True
        )
        assert risk == RiskLevel.MEDIUM

    def test_low_score_returns_low(self) -> None:
        """Score < 70 returns LOW risk."""
        risk = classify_risk_level(
            score=65, match_type=MatchType.FUZZY, country_match=True
        )
        assert risk == RiskLevel.LOW

    def test_fuzzy_match_country_mismatch_low_score_returns_low(self) -> None:
        """Fuzzy match with country mismatch and low score returns LOW risk."""
        risk = classify_risk_level(
            score=60, match_type=MatchType.FUZZY, country_match=False
        )
        assert risk == RiskLevel.LOW

    def test_boundary_70_returns_medium(self) -> None:
        """Score exactly 70 returns MEDIUM risk."""
        risk = classify_risk_level(
            score=70, match_type=MatchType.FUZZY, country_match=True
        )
        assert risk == RiskLevel.MEDIUM

    def test_boundary_69_returns_low(self) -> None:
        """Score exactly 69 returns LOW risk."""
        risk = classify_risk_level(
            score=69, match_type=MatchType.FUZZY, country_match=True
        )
        assert risk == RiskLevel.LOW

    def test_boundary_90_with_country_match_returns_high(self) -> None:
        """Score exactly 90 with country match returns HIGH risk."""
        risk = classify_risk_level(
            score=90, match_type=MatchType.FUZZY, country_match=True
        )
        assert risk == RiskLevel.HIGH

    def test_boundary_90_without_country_match_returns_medium(self) -> None:
        """Score exactly 90 without country match returns MEDIUM risk."""
        risk = classify_risk_level(
            score=90, match_type=MatchType.FUZZY, country_match=False
        )
        assert risk == RiskLevel.MEDIUM
