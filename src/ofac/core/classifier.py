"""Classification logic for screening results.

This module provides functions to classify screening results into
OK, REVIEW, or NOK categories based on match scores and thresholds.

Usage:
    from ofac.core.classifier import classify_screening_result

    status = classify_screening_result(highest_score, matches)
"""

from ofac.core.config import settings
from ofac.core.models import MatchResult, MatchStatus


def classify_screening_result(
    highest_score: int,
    matches: list[MatchResult],
) -> MatchStatus:
    """Classify screening result based on match scores.

    Classification rules:
    - NOK: highest_score >= match_threshold_nok (default: 95)
    - REVIEW: highest_score >= match_threshold_review (default: 80)
    - OK: highest_score < match_threshold_review

    Args:
        highest_score: Highest match score found (0-100).
        matches: List of all matches found.

    Returns:
        MatchStatus: OK, REVIEW, or NOK.
    """
    if not matches:
        return MatchStatus.OK

    if highest_score >= settings.match_threshold_nok:
        return MatchStatus.NOK

    if highest_score >= settings.match_threshold_review:
        return MatchStatus.REVIEW

    return MatchStatus.OK


__all__ = ["classify_screening_result"]
