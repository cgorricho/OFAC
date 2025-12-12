"""Risk level classification for OFAC matches.

This module provides functions to classify match risk levels based on
match score, match type, and country alignment.

Usage:
    from ofac.core.risk import classify_risk_level, RiskLevel

    risk = classify_risk_level(score=95, match_type=MatchType.EXACT, country_match=True)
    print(f"Risk level: {risk.value}")
"""

from enum import Enum

from ofac.core.models import MatchType


class RiskLevel(str, Enum):
    """Risk level classification for OFAC matches.

    HIGH: High risk match (exact match, high score, country match)
    MEDIUM: Medium risk match (fuzzy match, moderate score)
    LOW: Low risk match (fuzzy match, low score, country mismatch)
    """

    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


def classify_risk_level(
    score: int,
    match_type: MatchType,
    country_match: bool,
) -> RiskLevel:
    """Classify risk level for an OFAC match.

    Risk classification rules:
    - HIGH: Exact match OR (score >= 90 AND country_match)
    - MEDIUM: Score >= 70 AND (fuzzy match OR country mismatch)
    - LOW: Score < 70 OR (fuzzy match AND country mismatch)

    Args:
        score: Match score (0-100).
        match_type: Match type (EXACT or FUZZY).
        country_match: Whether countries match.

    Returns:
        RiskLevel enum value.

    Example:
        risk = classify_risk_level(score=95, match_type=MatchType.EXACT, country_match=True)
        assert risk == RiskLevel.HIGH
    """
    # High risk: exact match or high score with country match
    if match_type == MatchType.EXACT:
        return RiskLevel.HIGH
    if score >= 90 and country_match:
        return RiskLevel.HIGH

    # Medium risk: moderate score
    if score >= 70:
        return RiskLevel.MEDIUM

    # Low risk: low score or country mismatch
    return RiskLevel.LOW


__all__ = ["RiskLevel", "classify_risk_level"]
