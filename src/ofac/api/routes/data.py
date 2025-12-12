"""Data status and refresh endpoints.

This module provides API endpoints for:
- GET /data/status: Get OFAC data freshness status
- POST /data/refresh: Trigger OFAC data update

Usage:
    from ofac.api.routes.data import router
    app.include_router(router)
"""

from fastapi import APIRouter, Depends, HTTPException, status

from ofac.api.deps import get_matcher
from ofac.core.exceptions import OFACNotLoadedError
from ofac.core.matcher import EntityMatcher
from ofac.data.status import calculate_freshness

router = APIRouter(prefix="/data", tags=["Data"])


@router.get("/status")
async def get_data_status(
    matcher: EntityMatcher = Depends(get_matcher),
) -> dict:
    """Get OFAC data status and freshness information.

    Returns:
        Dictionary with:
        - version: OFAC data version/date
        - last_updated: ISO timestamp of last update
        - age_days: Number of days since last update
        - freshness_status: CURRENT, STALE, or CRITICAL
        - record_count: Total number of SDN entries

    Raises:
        HTTPException: If OFAC data is not loaded.
    """
    try:
        data = matcher.data
        version_info = data.version

        # Calculate freshness
        freshness_status, age_days = calculate_freshness(version_info)

        return {
            "version": version_info.publish_date or version_info.loaded_at or "Unknown",
            "last_updated": version_info.loaded_at,
            "age_days": age_days,
            "freshness_status": freshness_status.value,
            "record_count": version_info.sdn_count,
        }
    except OFACNotLoadedError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "code": "DATA_NOT_LOADED",
                "message": "OFAC data is not loaded",
            },
        ) from e


__all__ = ["router"]
