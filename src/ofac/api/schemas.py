"""API request and response schemas.

This module provides Pydantic models for API request/response serialization.
These models wrap the core models with API-specific metadata.

Usage:
    from ofac.api.schemas import SingleScreeningRequest, SingleScreeningResponse
"""

from pydantic import BaseModel, Field

from ofac.core.models import EntityInput, ScreeningResult


class SingleScreeningRequest(BaseModel):
    """Request model for single entity screening.

    Attributes:
        entity_name: Name of the entity to screen (required)
        country: Optional country code/name
        description: Optional description for humanitarian context
    """

    entity_name: str
    country: str | None = None
    description: str | None = None

    def to_entity_input(self) -> EntityInput:
        """Convert to EntityInput model."""
        return EntityInput(
            entity_name=self.entity_name,
            country=self.country,
            description=self.description,
        )


class SingleScreeningResponse(BaseModel):
    """Response model for single entity screening.

    Follows the API response wrapper pattern:
    {"data": {...}, "meta": {...}}

    Attributes:
        data: Screening result data
        meta: Metadata about the screening (OFAC version, duration)
    """

    data: ScreeningResult
    meta: dict[str, str | int] = Field(
        default_factory=dict,
        description="Metadata (ofac_version, duration_ms)",
    )


__all__ = ["SingleScreeningRequest", "SingleScreeningResponse"]
