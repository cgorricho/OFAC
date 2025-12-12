"""Unit tests for humanitarian keyword detection."""

import pytest

from ofac.core.classifier import (
    HUMANITARIAN_KEYWORDS,
    detect_humanitarian_keywords,
)


class TestDetectHumanitarianKeywords:
    """Tests for detect_humanitarian_keywords() function."""

    def test_detects_emergency_medical(self) -> None:
        """detect_humanitarian_keywords() detects emergency and medical."""
        is_humanitarian, keywords = detect_humanitarian_keywords(
            "Emergency medical supplies for Syria"
        )
        assert is_humanitarian is True
        assert "emergency" in keywords
        assert "medical" in keywords

    def test_detects_multiple_keywords(self) -> None:
        """detect_humanitarian_keywords() detects multiple keywords."""
        is_humanitarian, keywords = detect_humanitarian_keywords(
            "Humanitarian aid and food assistance for refugee populations"
        )
        assert is_humanitarian is True
        assert "humanitarian" in keywords
        assert "aid" in keywords
        assert "food" in keywords
        assert "assistance" in keywords
        assert "refugee" in keywords

    def test_no_humanitarian_context(self) -> None:
        """detect_humanitarian_keywords() returns False for non-humanitarian text."""
        is_humanitarian, keywords = detect_humanitarian_keywords(
            "Banking services in Damascus"
        )
        assert is_humanitarian is False
        assert len(keywords) == 0

    def test_case_insensitive(self) -> None:
        """detect_humanitarian_keywords() is case-insensitive."""
        is_humanitarian1, keywords1 = detect_humanitarian_keywords("EMERGENCY MEDICAL")
        is_humanitarian2, keywords2 = detect_humanitarian_keywords("emergency medical")
        is_humanitarian3, keywords3 = detect_humanitarian_keywords("Emergency Medical")

        assert is_humanitarian1 == is_humanitarian2 == is_humanitarian3
        assert keywords1 == keywords2 == keywords3

    def test_word_boundary_matching(self) -> None:
        """detect_humanitarian_keywords() uses word boundaries to avoid partial matches."""
        # "aid" should match "aid" but not "paid" or "maid"
        is_humanitarian1, keywords1 = detect_humanitarian_keywords("humanitarian aid")
        is_humanitarian2, keywords2 = detect_humanitarian_keywords("paid services")
        is_humanitarian3, keywords3 = detect_humanitarian_keywords("maid service")

        assert is_humanitarian1 is True
        assert "aid" in keywords1
        assert is_humanitarian2 is False
        assert is_humanitarian3 is False

    def test_empty_description(self) -> None:
        """detect_humanitarian_keywords() returns False for empty description."""
        is_humanitarian, keywords = detect_humanitarian_keywords("")
        assert is_humanitarian is False
        assert len(keywords) == 0

    def test_none_description(self) -> None:
        """detect_humanitarian_keywords() returns False for None description."""
        is_humanitarian, keywords = detect_humanitarian_keywords(None)
        assert is_humanitarian is False
        assert len(keywords) == 0

    def test_all_keywords_detected(self) -> None:
        """detect_humanitarian_keywords() can detect all keywords."""
        # Create description with all keywords
        description = " ".join(HUMANITARIAN_KEYWORDS)
        is_humanitarian, keywords = detect_humanitarian_keywords(description)

        assert is_humanitarian is True
        assert len(keywords) == len(HUMANITARIAN_KEYWORDS)
        assert set(keywords) == set(HUMANITARIAN_KEYWORDS)

    def test_keywords_in_context(self) -> None:
        """detect_humanitarian_keywords() detects keywords in sentence context."""
        is_humanitarian, keywords = detect_humanitarian_keywords(
            "We provide emergency medical assistance and food aid to displaced populations."
        )
        assert is_humanitarian is True
        assert "emergency" in keywords
        assert "medical" in keywords
        assert "assistance" in keywords
        assert "food" in keywords
        assert "aid" in keywords
        assert "displaced" in keywords

