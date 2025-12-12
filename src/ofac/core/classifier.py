"""Classification logic for screening results.

This module provides the ScreeningClassifier class and functions to classify
screening results into OK, REVIEW, or NOK categories based on match scores
and thresholds.

Usage:
    from ofac.core.classifier import ScreeningClassifier, classify_screening_result

    # Class-based approach
    classifier = ScreeningClassifier()
    status = classifier.classify(score=95)

    # Function-based approach (backward compatibility)
    status = classify_screening_result(highest_score, matches)
"""

from typing import Literal

from ofac.core.config import settings
from ofac.core.models import MatchResult, MatchStatus


class ScreeningClassifier:
    """Classifies match scores into OK, REVIEW, or NOK statuses.

    Uses configurable thresholds from settings to determine classification:
    - NOK: score >= match_threshold_nok (default: 95)
    - REVIEW: score >= match_threshold_review (default: 80)
    - OK: score < match_threshold_review

    Attributes:
        threshold_nok: Threshold for NOK classification (default: 95)
        threshold_review: Threshold for REVIEW classification (default: 80)

    Example:
        classifier = ScreeningClassifier()
        status = classifier.classify(score=95)  # Returns MatchStatus.NOK
        status = classifier.classify(score=85)  # Returns MatchStatus.REVIEW
        status = classifier.classify(score=75)  # Returns MatchStatus.OK
    """

    def __init__(
        self,
        threshold_nok: int | None = None,
        threshold_review: int | None = None,
    ) -> None:
        """Initialize the classifier with thresholds.

        Args:
            threshold_nok: Threshold for NOK classification. Defaults to settings.match_threshold_nok.
            threshold_review: Threshold for REVIEW classification. Defaults to settings.match_threshold_review.
        """
        self.threshold_nok = threshold_nok or settings.match_threshold_nok
        self.threshold_review = threshold_review or settings.match_threshold_review

        # Validate thresholds
        if self.threshold_review >= self.threshold_nok:
            msg = (
                f"threshold_review ({self.threshold_review}) must be "
                f"less than threshold_nok ({self.threshold_nok})"
            )
            raise ValueError(msg)

    def classify(self, score: int) -> Literal["OK", "REVIEW", "NOK"]:
        """Classify a match score into OK, REVIEW, or NOK.

        Args:
            score: Match score (0-100).

        Returns:
            MatchStatus: OK, REVIEW, or NOK.

        Example:
            classifier = ScreeningClassifier()
            status = classifier.classify(95)  # Returns MatchStatus.NOK
        """
        if score >= self.threshold_nok:
            return MatchStatus.NOK

        if score >= self.threshold_review:
            return MatchStatus.REVIEW

        return MatchStatus.OK


def classify_screening_result(
    highest_score: int,
    matches: list[MatchResult],
) -> MatchStatus:
    """Classify screening result based on match scores (backward compatibility).

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

    classifier = ScreeningClassifier()
    return classifier.classify(highest_score)


__all__ = ["ScreeningClassifier", "classify_screening_result"]
