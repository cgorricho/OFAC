"""Core Pydantic data models for OFAC screening.

This module provides type-safe data models with:
- Validation of all fields
- JSON serialization with snake_case naming
- Enums for status types

Usage:
    from ofac.core.models import EntityInput, ScreeningResult, MatchStatus

    entity = EntityInput(entity_name="Test Org", country="US")
    result = ScreeningResult(entity_input=entity, match_status=MatchStatus.OK, ...)
"""

from datetime import UTC, datetime
from enum import Enum
from typing import Annotated
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field


class MatchStatus(str, Enum):
    """Classification status for screening results.

    OK: Score < 80 - Entity is cleared
    REVIEW: Score 80-94 - Needs human review
    NOK: Score >= 95 - Blocked, needs escalation
    """

    OK = "OK"
    REVIEW = "REVIEW"
    NOK = "NOK"


class MatchType(str, Enum):
    """Type of match found against OFAC lists.

    EXACT: Perfect name match
    FUZZY: Similar name match (token_sort_ratio)
    ALIAS: Match against alternate name (ALT list)
    """

    EXACT = "EXACT"
    FUZZY = "FUZZY"
    ALIAS = "ALIAS"


class OFACList(str, Enum):
    """OFAC list source for a match.

    SDN: Specially Designated Nationals list
    CONSOLIDATED: Consolidated Sanctions list
    """

    SDN = "SDN"
    CONSOLIDATED = "CONSOLIDATED"


# Type alias for score validation
Score = Annotated[int, Field(ge=0, le=100)]


class EntityInput(BaseModel):
    """Input entity for screening.

    Attributes:
        entity_name: Name of the organization to screen (required)
        country: ISO country code or name (optional, boosts score if matches)
        description: Project or organization description (optional, for humanitarian detection)
    """

    entity_name: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="Name of the organization to screen",
    )
    country: str | None = Field(
        default=None,
        max_length=100,
        description="Country code or name for country-aware scoring",
    )
    description: str | None = Field(
        default=None,
        max_length=2000,
        description="Project description for humanitarian context detection",
    )

    model_config = ConfigDict(
        populate_by_name=True,
        str_strip_whitespace=True,
    )


class MatchResult(BaseModel):
    """A single match result from OFAC screening.

    Represents one potential match found in the OFAC lists.

    Attributes:
        sdn_name: Name from the OFAC SDN/Consolidated list
        sdn_type: Entity type (Individual, Entity, Vessel, Aircraft)
        match_score: Similarity score (0-100)
        match_type: Type of match (EXACT, FUZZY, ALIAS)
        ofac_list: Source list (SDN or CONSOLIDATED)
        programs: Sanctions programs (e.g., "SDGT", "IRAN")
        ent_num: OFAC entity number for reference
        country: Country associated with the SDN entry
        remarks: Additional OFAC remarks
    """

    sdn_name: str = Field(..., description="Name from OFAC list")
    sdn_type: str = Field(..., description="Entity type (Individual, Entity, etc.)")
    match_score: Score = Field(..., description="Similarity score 0-100")
    match_type: MatchType = Field(..., description="Type of match found")
    ofac_list: OFACList = Field(..., description="Source OFAC list")
    programs: list[str] = Field(
        default_factory=list,
        description="Sanctions programs (e.g., SDGT, IRAN)",
    )
    ent_num: int = Field(..., description="OFAC entity number")
    country: str | None = Field(default=None, description="SDN entry country")
    remarks: str | None = Field(default=None, description="OFAC remarks")
    country_match: bool = Field(
        default=False,
        description="Whether entity country matches SDN country",
    )

    model_config = ConfigDict(
        populate_by_name=True,
    )


class ScreeningResult(BaseModel):
    """Complete screening result for an entity.

    Contains the input entity, classification status, and all matches found.

    Attributes:
        screening_id: Unique identifier for this screening
        entity_input: The input entity that was screened
        match_status: Classification result (OK, REVIEW, NOK)
        matches: List of all matches found (may be empty for OK status)
        highest_score: Highest match score found (0 if no matches)
        ofac_version: Version/date of OFAC data used
        timestamp: When the screening was performed
        humanitarian_flag: Whether humanitarian context was detected
        general_license_note: Applicable General License if any
    """

    screening_id: str = Field(
        default_factory=lambda: str(uuid4()),
        description="Unique screening identifier",
    )
    entity_input: EntityInput = Field(..., description="Input entity screened")
    match_status: MatchStatus = Field(..., description="Classification result")
    matches: list[MatchResult] = Field(
        default_factory=list,
        description="List of matches found",
    )
    highest_score: Score = Field(
        default=0,
        description="Highest match score (0 if no matches)",
    )
    ofac_version: str = Field(
        default="",
        description="OFAC data version used",
    )
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="Screening timestamp (UTC)",
    )
    humanitarian_flag: bool = Field(
        default=False,
        description="Whether humanitarian context was detected",
    )
    general_license_note: str | None = Field(
        default=None,
        description="Applicable General License (e.g., GL-21)",
    )

    model_config = ConfigDict(
        populate_by_name=True,
    )


class BatchScreeningRequest(BaseModel):
    """Request for batch screening multiple entities.

    Attributes:
        entities: List of entities to screen
        include_ok: Whether to include OK results in response
    """

    entities: list[EntityInput] = Field(
        ...,
        min_length=1,
        max_length=10000,
        description="List of entities to screen",
    )
    include_ok: bool = Field(
        default=True,
        description="Include OK results in response",
    )

    model_config = ConfigDict(
        populate_by_name=True,
    )


class BatchScreeningResponse(BaseModel):
    """Response for batch screening.

    Attributes:
        results: List of screening results
        total_screened: Total number of entities screened
        ok_count: Number of OK results
        review_count: Number of REVIEW results
        nok_count: Number of NOK results
        ofac_version: OFAC data version used
        processing_time_ms: Processing time in milliseconds
    """

    results: list[ScreeningResult] = Field(..., description="Screening results")
    total_screened: int = Field(..., ge=0, description="Total entities screened")
    ok_count: int = Field(default=0, ge=0, description="OK count")
    review_count: int = Field(default=0, ge=0, description="REVIEW count")
    nok_count: int = Field(default=0, ge=0, description="NOK count")
    ofac_version: str = Field(default="", description="OFAC data version")
    processing_time_ms: int = Field(
        default=0,
        ge=0,
        description="Processing time in milliseconds",
    )

    model_config = ConfigDict(
        populate_by_name=True,
    )


__all__ = [
    "MatchStatus",
    "MatchType",
    "OFACList",
    "EntityInput",
    "MatchResult",
    "ScreeningResult",
    "BatchScreeningRequest",
    "BatchScreeningResponse",
]

