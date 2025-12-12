"""Unit tests for classification logic."""

import pytest

from ofac.core.classifier import ScreeningClassifier, classify_screening_result
from ofac.core.config import settings
from ofac.core.models import MatchResult, MatchStatus, MatchType, OFACList


class TestScreeningClassifier:
    """Tests for ScreeningClassifier class."""

    def test_classify_nok_high_score(self) -> None:
        """classify() returns NOK for scores >= threshold_nok."""
        classifier = ScreeningClassifier()
        assert classifier.classify(95) == MatchStatus.NOK
        assert classifier.classify(100) == MatchStatus.NOK
        assert classifier.classify(settings.match_threshold_nok) == MatchStatus.NOK

    def test_classify_review_medium_score(self) -> None:
        """classify() returns REVIEW for scores between thresholds."""
        classifier = ScreeningClassifier()
        assert classifier.classify(85) == MatchStatus.REVIEW
        assert classifier.classify(80) == MatchStatus.REVIEW
        assert (
            classifier.classify(settings.match_threshold_review) == MatchStatus.REVIEW
        )
        assert (
            classifier.classify(settings.match_threshold_nok - 1) == MatchStatus.REVIEW
        )

    def test_classify_ok_low_score(self) -> None:
        """classify() returns OK for scores < threshold_review."""
        classifier = ScreeningClassifier()
        assert classifier.classify(75) == MatchStatus.OK
        assert classifier.classify(0) == MatchStatus.OK
        assert (
            classifier.classify(settings.match_threshold_review - 1) == MatchStatus.OK
        )

    def test_classify_custom_thresholds(self) -> None:
        """classify() works with custom thresholds."""
        classifier = ScreeningClassifier(threshold_nok=90, threshold_review=75)
        assert classifier.classify(88) == MatchStatus.REVIEW  # Between thresholds
        assert classifier.classify(90) == MatchStatus.NOK
        assert classifier.classify(75) == MatchStatus.REVIEW
        assert classifier.classify(74) == MatchStatus.OK

    def test_classify_invalid_thresholds(self) -> None:
        """classify() raises ValueError if thresholds are invalid."""
        with pytest.raises(ValueError, match="threshold_review.*must be less"):
            ScreeningClassifier(threshold_nok=80, threshold_review=90)

        with pytest.raises(ValueError, match="threshold_review.*must be less"):
            ScreeningClassifier(threshold_nok=80, threshold_review=80)


class TestClassifyScreeningResult:
    """Tests for classify_screening_result function (backward compatibility)."""

    def test_classify_with_matches_nok(self) -> None:
        """classify_screening_result() returns NOK for high scores."""
        matches = [
            MatchResult(
                sdn_name="Test Entity",
                sdn_type="entity",
                match_score=95,
                match_type=MatchType.FUZZY,
                ofac_list=OFACList.SDN,
                programs=[],
                ent_num=1,
            )
        ]
        result = classify_screening_result(95, matches)
        assert result == MatchStatus.NOK

    def test_classify_with_matches_review(self) -> None:
        """classify_screening_result() returns REVIEW for medium scores."""
        matches = [
            MatchResult(
                sdn_name="Test Entity",
                sdn_type="entity",
                match_score=85,
                match_type=MatchType.FUZZY,
                ofac_list=OFACList.SDN,
                programs=[],
                ent_num=1,
            )
        ]
        result = classify_screening_result(85, matches)
        assert result == MatchStatus.REVIEW

    def test_classify_with_matches_ok(self) -> None:
        """classify_screening_result() returns OK for low scores."""
        matches = [
            MatchResult(
                sdn_name="Test Entity",
                sdn_type="entity",
                match_score=75,
                match_type=MatchType.FUZZY,
                ofac_list=OFACList.SDN,
                programs=[],
                ent_num=1,
            )
        ]
        result = classify_screening_result(75, matches)
        assert result == MatchStatus.OK

    def test_classify_no_matches(self) -> None:
        """classify_screening_result() returns OK when no matches."""
        result = classify_screening_result(0, [])
        assert result == MatchStatus.OK
