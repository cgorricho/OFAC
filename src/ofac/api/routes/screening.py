"""Screening endpoints for single and batch entity screening."""

import time
from datetime import UTC, datetime

from fastapi import APIRouter, Depends, HTTPException, status

from ofac.api.deps import get_matcher
from ofac.api.schemas import SingleScreeningRequest, SingleScreeningResponse
from ofac.core.classifier import classify_screening_result
from ofac.core.matcher import EntityMatcher
from ofac.core.models import ScreeningResult

router = APIRouter(prefix="/screenings", tags=["Screening"])


@router.post("/single", response_model=SingleScreeningResponse)
async def screen_single_entity(
    request: SingleScreeningRequest,
    matcher: EntityMatcher = Depends(get_matcher),
) -> SingleScreeningResponse:
    """Screen a single entity against OFAC lists.

    Args:
        request: SingleScreeningRequest with entity details.
        matcher: EntityMatcher instance (injected).

    Returns:
        SingleScreeningResponse with screening results and metadata.

    Raises:
        HTTPException: If screening fails or OFAC data not available.
    """
    start_time = time.time()

    try:
        # Convert request to EntityInput
        entity_input = request.to_entity_input()

        # Perform matching
        matches = matcher.match(
            entity_name=entity_input.entity_name,
            country=entity_input.country,
            max_results=10,
        )

        # Classify result (OK/REVIEW/NOK)
        highest_score = matches[0].match_score if matches else 0
        match_status = classify_screening_result(highest_score, matches)

        # Get OFAC version
        ofac_version = matcher.data.version.loaded_at or "unknown"

        # Create screening result
        screening_result = ScreeningResult(
            entity_input=entity_input,
            match_status=match_status,
            matches=matches,
            highest_score=highest_score,
            ofac_version=ofac_version,
            timestamp=datetime.now(UTC),
        )

        # Calculate duration
        duration_ms = int((time.time() - start_time) * 1000)

        return SingleScreeningResponse(
            data=screening_result,
            meta={
                "ofac_version": ofac_version,
                "duration_ms": duration_ms,
            },
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "code": "SCREENING_ERROR",
                "message": f"Screening failed: {str(e)}",
            },
        ) from e


__all__ = ["router"]
