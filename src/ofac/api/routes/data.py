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
from ofac.data.updater import OFACUpdater

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


@router.post("/refresh")
async def refresh_data() -> dict:
    """Trigger OFAC data update.

    Downloads and updates OFAC data from official sources.

    Returns:
        Dictionary with:
        - version: New OFAC data version/date
        - last_updated: ISO timestamp of update
        - record_count: Total number of SDN entries
        - status: "success" or "error"

    Raises:
        HTTPException: If update fails or OFAC data not available.
    """
    try:
        # Get loader from app state
        from ofac.api.main import get_ofac_loader

        loader = get_ofac_loader()
        if not loader:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail={
                    "code": "LOADER_NOT_AVAILABLE",
                    "message": "OFAC data loader is not available",
                },
            )

        # Trigger update
        data_path = loader.data_path
        updater = OFACUpdater(data_path=data_path)
        try:
            updater.download_sdn_files()
            # Reload data after successful update
            loader.clear_cache()
            loader.load()

            # Get new version info
            new_data = loader.data
            version_info = new_data.version
            freshness_status, age_days = calculate_freshness(version_info)

            return {
                "version": version_info.publish_date
                or version_info.loaded_at
                or "Unknown",
                "last_updated": version_info.loaded_at,
                "age_days": age_days,
                "freshness_status": freshness_status.value,
                "record_count": version_info.sdn_count,
                "status": "success",
            }
        except Exception as e:
            # Update failed, but existing data is preserved
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail={
                    "code": "UPDATE_FAILED",
                    "message": f"OFAC data update failed: {str(e)}",
                },
            ) from e
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "code": "UPDATE_ERROR",
                "message": f"Update failed: {str(e)}",
            },
        ) from e


__all__ = ["router"]
