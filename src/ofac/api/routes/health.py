"""Health check endpoint.

Provides basic health check endpoint to verify API is running.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("")
async def health_check() -> dict[str, str]:
    """Health check endpoint.

    Returns:
        Dict with status "healthy" if API is running.
    """
    return {"status": "healthy"}


@router.get("/ready")
async def readiness_check() -> dict[str, str]:
    """Readiness check endpoint.

    Verifies that OFAC data is loaded and API is ready to serve requests.

    Returns:
        Dict with status "ready" if OFAC data is loaded, "not_ready" otherwise.
    """
    from ofac.api.main import get_ofac_loader

    loader = get_ofac_loader()
    if loader and loader.is_loaded:
        return {"status": "ready", "ofac_data_loaded": "true"}
    return {"status": "not_ready", "ofac_data_loaded": "false"}


__all__ = ["router"]
