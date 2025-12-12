"""Dependency injection for FastAPI endpoints.

This module provides dependency functions for accessing OFAC data
and other shared resources in API endpoints.

Usage:
    from ofac.api.deps import get_ofac_data, get_matcher

    @router.post("/screenings/single")
    async def screen_entity(
        request: SingleScreeningRequest,
        ofac_data: OFACData = Depends(get_ofac_data),
    ):
        ...
"""

from typing import TYPE_CHECKING

from fastapi import HTTPException, status

from ofac.core.matcher import EntityMatcher
from ofac.data.loader import OFACData

if TYPE_CHECKING:
    from fastapi import Request
else:
    from fastapi import Request


def get_ofac_data(request: Request) -> OFACData:
    """Get OFAC data from application state.

    Args:
        request: FastAPI request object.

    Returns:
        OFACData instance.

    Raises:
        HTTPException: If OFAC data is not loaded.
    """
    if not hasattr(request.app.state, "ofac_data") or request.app.state.ofac_data is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "code": "OFAC_DATA_NOT_LOADED",
                "message": "OFAC data is not loaded. Please wait for startup to complete.",
            },
        )
    ofac_data: OFACData = request.app.state.ofac_data
    return ofac_data


def get_matcher(request: Request) -> EntityMatcher:
    """Get EntityMatcher instance.

    Args:
        request: FastAPI request object.

    Returns:
        EntityMatcher instance.

    Raises:
        HTTPException: If OFAC data is not loaded.
    """
    ofac_data = get_ofac_data(request)
    return EntityMatcher(ofac_data)


__all__ = ["get_ofac_data", "get_matcher"]

