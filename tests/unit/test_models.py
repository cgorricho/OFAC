"""Unit tests for core data models."""

import json
from datetime import datetime

import pytest
from pydantic import ValidationError

from ofac.core.models import (
    BatchScreeningRequest,
    BatchScreeningResponse,
    EntityInput,
    MatchResult,
    MatchStatus,
    MatchType,
    OFACList,
    ScreeningResult,
)


class TestEntityInput:
    """Tests for EntityInput model."""

    def test_create_with_name_only(self) -> None:
        """EntityInput can be created with just entity_name."""
        entity = EntityInput(entity_name="Test Organization")
        assert entity.entity_name == "Test Organization"
        assert entity.country is None
        assert entity.description is None

    def test_create_with_all_fields(self) -> None:
        """EntityInput can be created with all fields."""
        entity = EntityInput(
            entity_name="Test Org",
            country="US",
            description="Humanitarian aid project",
        )
        assert entity.entity_name == "Test Org"
        assert entity.country == "US"
        assert entity.description == "Humanitarian aid project"

    def test_entity_name_required(self) -> None:
        """EntityInput requires entity_name."""
        with pytest.raises(ValidationError):
            EntityInput()  # type: ignore[call-arg]

    def test_entity_name_cannot_be_empty(self) -> None:
        """EntityInput entity_name cannot be empty string."""
        with pytest.raises(ValidationError):
            EntityInput(entity_name="")

    def test_entity_name_whitespace_stripped(self) -> None:
        """EntityInput strips whitespace from entity_name."""
        entity = EntityInput(entity_name="  Test Org  ")
        assert entity.entity_name == "Test Org"

    def test_json_serialization_snake_case(self) -> None:
        """EntityInput serializes to JSON with snake_case."""
        entity = EntityInput(entity_name="Test Org", country="US")
        data = json.loads(entity.model_dump_json())
        assert "entity_name" in data
        assert "country" in data
        assert "entityName" not in data


class TestMatchStatus:
    """Tests for MatchStatus enum."""

    def test_ok_status(self) -> None:
        """MatchStatus.OK has value 'OK'."""
        assert MatchStatus.OK.value == "OK"

    def test_review_status(self) -> None:
        """MatchStatus.REVIEW has value 'REVIEW'."""
        assert MatchStatus.REVIEW.value == "REVIEW"

    def test_nok_status(self) -> None:
        """MatchStatus.NOK has value 'NOK'."""
        assert MatchStatus.NOK.value == "NOK"

    def test_status_is_string(self) -> None:
        """MatchStatus values are strings."""
        assert isinstance(MatchStatus.OK.value, str)


class TestMatchType:
    """Tests for MatchType enum."""

    def test_exact_type(self) -> None:
        """MatchType.EXACT has value 'EXACT'."""
        assert MatchType.EXACT.value == "EXACT"

    def test_fuzzy_type(self) -> None:
        """MatchType.FUZZY has value 'FUZZY'."""
        assert MatchType.FUZZY.value == "FUZZY"

    def test_alias_type(self) -> None:
        """MatchType.ALIAS has value 'ALIAS'."""
        assert MatchType.ALIAS.value == "ALIAS"


class TestOFACList:
    """Tests for OFACList enum."""

    def test_sdn_list(self) -> None:
        """OFACList.SDN has value 'SDN'."""
        assert OFACList.SDN.value == "SDN"

    def test_consolidated_list(self) -> None:
        """OFACList.CONSOLIDATED has value 'CONSOLIDATED'."""
        assert OFACList.CONSOLIDATED.value == "CONSOLIDATED"


class TestMatchResult:
    """Tests for MatchResult model."""

    def test_create_match_result(self) -> None:
        """MatchResult can be created with required fields."""
        result = MatchResult(
            sdn_name="Test SDN Entity",
            sdn_type="Entity",
            match_score=85,
            match_type=MatchType.FUZZY,
            ofac_list=OFACList.SDN,
            ent_num=12345,
        )
        assert result.sdn_name == "Test SDN Entity"
        assert result.match_score == 85
        assert result.match_type == MatchType.FUZZY

    def test_match_score_validation_min(self) -> None:
        """MatchResult score cannot be below 0."""
        with pytest.raises(ValidationError):
            MatchResult(
                sdn_name="Test",
                sdn_type="Entity",
                match_score=-1,
                match_type=MatchType.EXACT,
                ofac_list=OFACList.SDN,
                ent_num=1,
            )

    def test_match_score_validation_max(self) -> None:
        """MatchResult score cannot be above 100."""
        with pytest.raises(ValidationError):
            MatchResult(
                sdn_name="Test",
                sdn_type="Entity",
                match_score=101,
                match_type=MatchType.EXACT,
                ofac_list=OFACList.SDN,
                ent_num=1,
            )

    def test_match_score_boundary_valid(self) -> None:
        """MatchResult score 0 and 100 are valid."""
        result_0 = MatchResult(
            sdn_name="Test",
            sdn_type="Entity",
            match_score=0,
            match_type=MatchType.EXACT,
            ofac_list=OFACList.SDN,
            ent_num=1,
        )
        result_100 = MatchResult(
            sdn_name="Test",
            sdn_type="Entity",
            match_score=100,
            match_type=MatchType.EXACT,
            ofac_list=OFACList.SDN,
            ent_num=1,
        )
        assert result_0.match_score == 0
        assert result_100.match_score == 100

    def test_programs_default_empty(self) -> None:
        """MatchResult programs defaults to empty list."""
        result = MatchResult(
            sdn_name="Test",
            sdn_type="Entity",
            match_score=90,
            match_type=MatchType.EXACT,
            ofac_list=OFACList.SDN,
            ent_num=1,
        )
        assert result.programs == []

    def test_country_match_default_false(self) -> None:
        """MatchResult country_match defaults to False."""
        result = MatchResult(
            sdn_name="Test",
            sdn_type="Entity",
            match_score=90,
            match_type=MatchType.EXACT,
            ofac_list=OFACList.SDN,
            ent_num=1,
        )
        assert result.country_match is False


class TestScreeningResult:
    """Tests for ScreeningResult model."""

    def test_create_screening_result(self) -> None:
        """ScreeningResult can be created with required fields."""
        entity = EntityInput(entity_name="Test Org")
        result = ScreeningResult(
            entity_input=entity,
            match_status=MatchStatus.OK,
        )
        assert result.entity_input.entity_name == "Test Org"
        assert result.match_status == MatchStatus.OK

    def test_screening_id_auto_generated(self) -> None:
        """ScreeningResult generates unique screening_id."""
        entity = EntityInput(entity_name="Test Org")
        result1 = ScreeningResult(entity_input=entity, match_status=MatchStatus.OK)
        result2 = ScreeningResult(entity_input=entity, match_status=MatchStatus.OK)
        assert result1.screening_id != result2.screening_id
        assert len(result1.screening_id) == 36  # UUID format

    def test_timestamp_auto_generated(self) -> None:
        """ScreeningResult generates timestamp automatically."""
        entity = EntityInput(entity_name="Test Org")
        result = ScreeningResult(entity_input=entity, match_status=MatchStatus.OK)
        assert isinstance(result.timestamp, datetime)

    def test_matches_default_empty(self) -> None:
        """ScreeningResult matches defaults to empty list."""
        entity = EntityInput(entity_name="Test Org")
        result = ScreeningResult(entity_input=entity, match_status=MatchStatus.OK)
        assert result.matches == []

    def test_highest_score_default_zero(self) -> None:
        """ScreeningResult highest_score defaults to 0."""
        entity = EntityInput(entity_name="Test Org")
        result = ScreeningResult(entity_input=entity, match_status=MatchStatus.OK)
        assert result.highest_score == 0

    def test_humanitarian_flag_default_false(self) -> None:
        """ScreeningResult humanitarian_flag defaults to False."""
        entity = EntityInput(entity_name="Test Org")
        result = ScreeningResult(entity_input=entity, match_status=MatchStatus.OK)
        assert result.humanitarian_flag is False

    def test_json_serialization_snake_case(self) -> None:
        """ScreeningResult serializes with snake_case field names."""
        entity = EntityInput(entity_name="Test Org")
        result = ScreeningResult(entity_input=entity, match_status=MatchStatus.OK)
        data = json.loads(result.model_dump_json())
        assert "entity_input" in data
        assert "match_status" in data
        assert "screening_id" in data
        assert "highest_score" in data
        assert "entityInput" not in data
        assert "matchStatus" not in data


class TestBatchScreeningRequest:
    """Tests for BatchScreeningRequest model."""

    def test_create_batch_request(self) -> None:
        """BatchScreeningRequest can be created with entity list."""
        entities = [
            EntityInput(entity_name="Org 1"),
            EntityInput(entity_name="Org 2"),
        ]
        request = BatchScreeningRequest(entities=entities)
        assert len(request.entities) == 2
        assert request.include_ok is True

    def test_entities_required(self) -> None:
        """BatchScreeningRequest requires entities list."""
        with pytest.raises(ValidationError):
            BatchScreeningRequest()  # type: ignore[call-arg]

    def test_entities_cannot_be_empty(self) -> None:
        """BatchScreeningRequest entities cannot be empty."""
        with pytest.raises(ValidationError):
            BatchScreeningRequest(entities=[])


class TestBatchScreeningResponse:
    """Tests for BatchScreeningResponse model."""

    def test_create_batch_response(self) -> None:
        """BatchScreeningResponse can be created with results."""
        entity = EntityInput(entity_name="Test Org")
        result = ScreeningResult(entity_input=entity, match_status=MatchStatus.OK)
        response = BatchScreeningResponse(
            results=[result],
            total_screened=1,
            ok_count=1,
        )
        assert len(response.results) == 1
        assert response.total_screened == 1
        assert response.ok_count == 1

    def test_counts_default_zero(self) -> None:
        """BatchScreeningResponse counts default to 0."""
        entity = EntityInput(entity_name="Test Org")
        result = ScreeningResult(entity_input=entity, match_status=MatchStatus.OK)
        response = BatchScreeningResponse(results=[result], total_screened=1)
        assert response.ok_count == 0
        assert response.review_count == 0
        assert response.nok_count == 0


class TestModelsImport:
    """Tests for model imports from ofac.core."""

    def test_import_from_models(self) -> None:
        """Models can be imported from ofac.core.models."""
        from ofac.core.models import EntityInput, MatchStatus, ScreeningResult

        assert EntityInput is not None
        assert MatchStatus is not None
        assert ScreeningResult is not None

    def test_import_from_core(self) -> None:
        """Models can be imported from ofac.core."""
        from ofac.core import EntityInput, MatchStatus, ScreeningResult

        assert EntityInput is not None
        assert MatchStatus is not None
        assert ScreeningResult is not None

