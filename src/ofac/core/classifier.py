"""Classification logic for screening results.

This module provides the ScreeningClassifier class and functions to classify
screening results into OK, REVIEW, or NOK categories based on match scores
and thresholds. It also provides humanitarian keyword detection.

Usage:
    from ofac.core.classifier import ScreeningClassifier, classify_screening_result
    from ofac.core.classifier import detect_humanitarian_keywords

    # Class-based approach
    classifier = ScreeningClassifier()
    status = classifier.classify(score=95)

    # Humanitarian detection
    keywords = detect_humanitarian_keywords("Emergency medical supplies")
"""

import re
from typing import Literal

from ofac.core.config import settings
from ofac.core.countries import get_general_license, is_sanctioned_country
from ofac.core.models import MatchResult, MatchStatus

# Humanitarian keywords for context detection
HUMANITARIAN_KEYWORDS: list[str] = [
    "humanitarian",
    "aid",
    "relief",
    "medical",
    "emergency",
    "food",
    "water",
    "shelter",
    "assistance",
    "refugee",
    "disaster",
    "crisis",
    "healthcare",
    "medicine",
    "nutrition",
    "sanitation",
    "education",
    "protection",
    "vulnerable",
    "displaced",
]


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


def classify_with_gl_context(
    highest_score: int,
    matches: list[MatchResult],
    entity_country: str | None = None,
    description: str | None = None,
) -> tuple[MatchStatus, bool, str | None]:
    """Classify screening result with General License context detection.

    Enhanced classification that considers:
    - Match score thresholds
    - Sanctioned country context
    - Humanitarian keyword detection
    - General License applicability

    Classification rules:
    - If score >= NOK threshold AND sanctioned country AND NO humanitarian keywords → NOK
    - If score >= NOK threshold AND sanctioned country AND humanitarian keywords → REVIEW (GL applicable)
    - If score >= NOK threshold AND NOT sanctioned country → NOK
    - If score >= REVIEW threshold → REVIEW
    - Otherwise → OK

    Args:
        highest_score: Highest match score found (0-100).
        matches: List of all matches found.
        entity_country: Entity's country (for GL detection).
        description: Project description (for humanitarian detection).

    Returns:
        Tuple of (MatchStatus, is_humanitarian, general_license_note).
    """
    # Check humanitarian keywords even if no matches (for transparency)
    is_humanitarian, detected_keywords = detect_humanitarian_keywords(description)

    if not matches:
        return MatchStatus.OK, is_humanitarian, None

    classifier = ScreeningClassifier()
    base_status = classifier.classify(highest_score)

    # Check for General License applicability
    is_sanctioned = entity_country and is_sanctioned_country(entity_country)

    general_license_note: str | None = None

    # If high score in sanctioned country with humanitarian context → REVIEW with GL
    if (
        base_status == MatchStatus.NOK
        and is_sanctioned
        and is_humanitarian
    ):
        gl = get_general_license(entity_country)
        if gl:
            general_license_note = (
                f"{gl.code}: {gl.description}. "
                f"Potential humanitarian license applicability. "
                f"Detected keywords: {', '.join(detected_keywords)}"
            )
            return MatchStatus.REVIEW, True, general_license_note

    # If high score in sanctioned country WITHOUT humanitarian context → NOK
    if base_status == MatchStatus.NOK and is_sanctioned and not is_humanitarian:
        return MatchStatus.NOK, False, None

    # Otherwise, return base classification
    return base_status, is_humanitarian, general_license_note


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


def detect_humanitarian_keywords(description: str | None) -> tuple[bool, list[str]]:
    """Detect humanitarian keywords in project description.

    Performs case-insensitive keyword matching against a predefined list
    of humanitarian terms. Returns whether humanitarian context was detected
    and the list of keywords found.

    Args:
        description: Project or organization description text.

    Returns:
        Tuple of (is_humanitarian: bool, detected_keywords: list[str]).
        is_humanitarian is True if any keywords are found.
        detected_keywords contains the list of keywords found (lowercase).

    Example:
        is_humanitarian, keywords = detect_humanitarian_keywords(
            "Emergency medical supplies for Syria"
        )
        # Returns: (True, ["emergency", "medical"])
    """
    if not description:
        return False, []

    description_lower = description.lower()
    detected: list[str] = []

    for keyword in HUMANITARIAN_KEYWORDS:
        # Use word boundary matching to avoid partial matches
        pattern = r"\b" + re.escape(keyword) + r"\b"
        if re.search(pattern, description_lower):
            detected.append(keyword)

    return len(detected) > 0, detected


__all__ = [
    "ScreeningClassifier",
    "classify_screening_result",
    "classify_with_gl_context",
    "detect_humanitarian_keywords",
    "HUMANITARIAN_KEYWORDS",
]

