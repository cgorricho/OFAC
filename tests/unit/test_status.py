"""Unit tests for OFAC data freshness status calculation."""

from datetime import UTC, datetime, timedelta

from ofac.data.schemas import OFACDataVersion
from ofac.data.status import FreshnessStatus, calculate_freshness


class TestFreshnessStatus:
    """Tests for FreshnessStatus enum."""

    def test_enum_values(self) -> None:
        """FreshnessStatus has correct values."""
        assert FreshnessStatus.CURRENT.value == "CURRENT"
        assert FreshnessStatus.STALE.value == "STALE"
        assert FreshnessStatus.CRITICAL.value == "CRITICAL"


class TestCalculateFreshness:
    """Tests for calculate_freshness function."""

    def test_current_status_less_than_7_days(self) -> None:
        """Data less than 7 days old returns CURRENT."""
        loaded_at_str = (datetime.now(UTC) - timedelta(days=5)).isoformat()
        version = OFACDataVersion(
            loaded_at=loaded_at_str,
            sdn_count=1000,
        )
        status, age_days = calculate_freshness(version)
        assert status == FreshnessStatus.CURRENT
        assert age_days == 5

    def test_current_status_exactly_6_days(self) -> None:
        """Data exactly 6 days old returns CURRENT."""
        loaded_at_str = (datetime.now(UTC) - timedelta(days=6)).isoformat()
        version = OFACDataVersion(
            loaded_at=loaded_at_str,
            sdn_count=1000,
        )
        status, age_days = calculate_freshness(version)
        assert status == FreshnessStatus.CURRENT
        assert age_days == 6

    def test_stale_status_7_days(self) -> None:
        """Data exactly 7 days old returns STALE."""
        loaded_at_str = (datetime.now(UTC) - timedelta(days=7)).isoformat()
        version = OFACDataVersion(
            loaded_at=loaded_at_str,
            sdn_count=1000,
        )
        status, age_days = calculate_freshness(version)
        assert status == FreshnessStatus.STALE
        assert age_days == 7

    def test_stale_status_10_days(self) -> None:
        """Data 10 days old returns STALE."""
        loaded_at_str = (datetime.now(UTC) - timedelta(days=10)).isoformat()
        version = OFACDataVersion(
            loaded_at=loaded_at_str,
            sdn_count=1000,
        )
        status, age_days = calculate_freshness(version)
        assert status == FreshnessStatus.STALE
        assert age_days == 10

    def test_stale_status_14_days(self) -> None:
        """Data exactly 14 days old returns STALE."""
        loaded_at_str = (datetime.now(UTC) - timedelta(days=14)).isoformat()
        version = OFACDataVersion(
            loaded_at=loaded_at_str,
            sdn_count=1000,
        )
        status, age_days = calculate_freshness(version)
        assert status == FreshnessStatus.STALE
        assert age_days == 14

    def test_critical_status_15_days(self) -> None:
        """Data exactly 15 days old returns CRITICAL."""
        loaded_at_str = (datetime.now(UTC) - timedelta(days=15)).isoformat()
        version = OFACDataVersion(
            loaded_at=loaded_at_str,
            sdn_count=1000,
        )
        status, age_days = calculate_freshness(version)
        assert status == FreshnessStatus.CRITICAL
        assert age_days == 15

    def test_critical_status_30_days(self) -> None:
        """Data 30 days old returns CRITICAL."""
        loaded_at_str = (datetime.now(UTC) - timedelta(days=30)).isoformat()
        version = OFACDataVersion(
            loaded_at=loaded_at_str,
            sdn_count=1000,
        )
        status, age_days = calculate_freshness(version)
        assert status == FreshnessStatus.CRITICAL
        assert age_days == 30

    def test_no_timestamp_returns_critical(self) -> None:
        """Data with no timestamp returns CRITICAL with age 999."""
        version = OFACDataVersion(
            loaded_at=None,
            sdn_count=1000,
        )
        status, age_days = calculate_freshness(version)
        assert status == FreshnessStatus.CRITICAL
        assert age_days == 999

    def test_zero_days_returns_current(self) -> None:
        """Data loaded today returns CURRENT with age 0."""
        loaded_at_str = datetime.now(UTC).isoformat()
        version = OFACDataVersion(
            loaded_at=loaded_at_str,
            sdn_count=1000,
        )
        status, age_days = calculate_freshness(version)
        assert status == FreshnessStatus.CURRENT
        assert age_days == 0
