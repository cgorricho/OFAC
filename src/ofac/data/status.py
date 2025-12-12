"""OFAC data freshness status calculation.

This module provides functions to calculate and determine the freshness
status of OFAC data based on when it was last updated.

Usage:
    from ofac.data.status import calculate_freshness, FreshnessStatus
    from ofac.data.loader import OFACDataLoader

    loader = OFACDataLoader()
    data = loader.load()
    status, age_days = calculate_freshness(data.version)
    print(f"Data is {status.value} ({age_days} days old)")
"""

from datetime import UTC, datetime
from enum import Enum

from ofac.data.schemas import OFACDataVersion


class FreshnessStatus(str, Enum):
    """OFAC data freshness status.

    CURRENT: Data is fresh (< 7 days old)
    STALE: Data is getting old (7-14 days old)
    CRITICAL: Data is very old (> 14 days old)
    """

    CURRENT = "CURRENT"
    STALE = "STALE"
    CRITICAL = "CRITICAL"


def calculate_freshness(version: OFACDataVersion) -> tuple[FreshnessStatus, int]:
    """Calculate freshness status and age in days for OFAC data.

    Args:
        version: OFACDataVersion containing loaded_at timestamp.

    Returns:
        Tuple of (FreshnessStatus, age_days).
        - age_days: Number of days since last update (0 if never updated)
        - FreshnessStatus: CURRENT (<7 days), STALE (7-14 days), CRITICAL (>14 days)

    Example:
        status, age = calculate_freshness(data.version)
        if status == FreshnessStatus.CRITICAL:
            print(f"Warning: Data is {age} days old!")
    """
    if not version.loaded_at:
        # If no timestamp, assume data is very old (critical)
        return FreshnessStatus.CRITICAL, 999

    # Calculate age in days
    now = datetime.now(UTC)
    age_delta = now - version.loaded_at
    age_days = age_delta.days

    # Determine status based on thresholds
    if age_days < 7:
        return FreshnessStatus.CURRENT, age_days
    elif age_days < 15:  # 7-14 days
        return FreshnessStatus.STALE, age_days
    else:  # 15+ days
        return FreshnessStatus.CRITICAL, age_days


__all__ = ["FreshnessStatus", "calculate_freshness"]
