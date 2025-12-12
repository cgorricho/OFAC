"""FastAPI application factory and lifespan management.

This module provides:
- FastAPI app factory with lifespan events
- OFAC data loading on startup
- CORS middleware configuration
- Router registration

Usage:
    from ofac.api.main import create_app

    app = create_app()
    # Run with: uvicorn ofac.api.main:app --reload
"""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ofac.core.config import settings
from ofac.data.loader import OFACDataLoader

# Global OFAC data loader instance
_ofac_loader: OFACDataLoader | None = None


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Lifespan context manager for FastAPI app.

    Loads OFAC data on startup and cleans up on shutdown.

    Args:
        app: FastAPI application instance.
    """
    global _ofac_loader

    # Startup: Load OFAC data
    _ofac_loader = OFACDataLoader()
    try:
        _ofac_loader.load()
        app.state.ofac_data = _ofac_loader.data
        app.state.ofac_loader = _ofac_loader
    except Exception as e:
        # Log error but don't crash - app can still serve health endpoint
        app.state.ofac_load_error = str(e)
        app.state.ofac_data = None
        app.state.ofac_loader = None

    yield

    # Shutdown: Cleanup (if needed)
    if _ofac_loader:
        _ofac_loader.clear_cache()


def create_app() -> FastAPI:
    """Create and configure FastAPI application.

    Returns:
        Configured FastAPI application instance.
    """
    app = FastAPI(
        title="OFAC Sanctions Screening API",
        description="API for screening organizations against OFAC sanctions lists",
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        lifespan=lifespan,
    )

    # CORS middleware for local development
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Register routers
    from ofac.api.routes import health, screening

    app.include_router(health.router, tags=["Health"])
    app.include_router(screening.router, tags=["Screening"])

    return app


# Create app instance for uvicorn
app = create_app()


def get_ofac_loader() -> OFACDataLoader | None:
    """Get the global OFAC data loader instance.

    Returns:
        OFACDataLoader instance or None if not loaded.
    """
    return _ofac_loader


__all__ = ["create_app", "app", "get_ofac_loader"]
