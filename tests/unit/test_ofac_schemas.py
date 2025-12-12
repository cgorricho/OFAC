"""Unit tests for OFAC data schemas."""

import pytest
from pydantic import ValidationError

from ofac.data.schemas import (
    ADD_CSV_COLUMNS,
    ALT_CSV_COLUMNS,
    SDN_CSV_COLUMNS,
    AddressEntry,
    AltEntry,
    AltType,
    OFACDataVersion,
    SDNEntry,
    SDNType,
)


class TestSDNType:
    """Tests for SDNType enum."""

    def test_individual_type(self) -> None:
        """SDNType.INDIVIDUAL has correct value."""
        assert SDNType.INDIVIDUAL.value == "individual"

    def test_entity_type(self) -> None:
        """SDNType.ENTITY has correct value."""
        assert SDNType.ENTITY.value == "entity"

    def test_vessel_type(self) -> None:
        """SDNType.VESSEL has correct value."""
        assert SDNType.VESSEL.value == "vessel"

    def test_aircraft_type(self) -> None:
        """SDNType.AIRCRAFT has correct value."""
        assert SDNType.AIRCRAFT.value == "aircraft"


class TestAltType:
    """Tests for AltType enum."""

    def test_aka_type(self) -> None:
        """AltType.AKA has correct value."""
        assert AltType.AKA.value == "aka"

    def test_fka_type(self) -> None:
        """AltType.FKA has correct value."""
        assert AltType.FKA.value == "fka"

    def test_nka_type(self) -> None:
        """AltType.NKA has correct value."""
        assert AltType.NKA.value == "nka"


class TestSDNEntry:
    """Tests for SDNEntry model."""

    def test_create_sdn_entry(self) -> None:
        """SDNEntry can be created with required fields."""
        sdn = SDNEntry(ent_num=306, sdn_name="BANCO NACIONAL DE CUBA")
        assert sdn.ent_num == 306
        assert sdn.sdn_name == "BANCO NACIONAL DE CUBA"

    def test_sdn_entry_with_all_fields(self) -> None:
        """SDNEntry can be created with all fields."""
        sdn = SDNEntry(
            ent_num=306,
            sdn_name="BANCO NACIONAL DE CUBA",
            sdn_type="entity",
            programs="CUBA",
            title=None,
            call_sign=None,
            vess_type=None,
            tonnage=None,
            grt=None,
            vess_flag=None,
            vess_owner=None,
            remarks="a.k.a. 'BNC'.",
        )
        assert sdn.ent_num == 306
        assert sdn.programs == "CUBA"
        assert sdn.remarks == "a.k.a. 'BNC'."

    def test_sdn_entry_converts_ofac_null(self) -> None:
        """SDNEntry converts '-0-' to None."""
        sdn = SDNEntry(
            ent_num=306,
            sdn_name="TEST ENTITY",
            sdn_type="-0-",  # type: ignore[arg-type]
            programs="-0-",  # type: ignore[arg-type]
            remarks="-0-",  # type: ignore[arg-type]
        )
        assert sdn.sdn_type is None
        assert sdn.programs is None
        assert sdn.remarks is None

    def test_sdn_entry_coerces_ent_num_string(self) -> None:
        """SDNEntry coerces string ent_num to int."""
        sdn = SDNEntry(ent_num="306", sdn_name="TEST")  # type: ignore[arg-type]
        assert sdn.ent_num == 306
        assert isinstance(sdn.ent_num, int)

    def test_sdn_entry_strips_whitespace(self) -> None:
        """SDNEntry strips whitespace from strings."""
        sdn = SDNEntry(ent_num=306, sdn_name="  TEST ENTITY  ")
        assert sdn.sdn_name == "TEST ENTITY"

    def test_sdn_entry_programs_list_property(self) -> None:
        """SDNEntry.programs_list parses semicolon-separated programs."""
        sdn = SDNEntry(ent_num=306, sdn_name="TEST", programs="SDGT; IRAN; CUBA")
        assert sdn.programs_list == ["SDGT", "IRAN", "CUBA"]

    def test_sdn_entry_programs_list_empty(self) -> None:
        """SDNEntry.programs_list returns empty list for None."""
        sdn = SDNEntry(ent_num=306, sdn_name="TEST")
        assert sdn.programs_list == []

    def test_sdn_entry_requires_ent_num(self) -> None:
        """SDNEntry requires ent_num."""
        with pytest.raises(ValidationError):
            SDNEntry(sdn_name="TEST")  # type: ignore[call-arg]

    def test_sdn_entry_requires_sdn_name(self) -> None:
        """SDNEntry requires sdn_name."""
        with pytest.raises(ValidationError):
            SDNEntry(ent_num=306)  # type: ignore[call-arg]

    def test_sdn_entry_name_not_empty(self) -> None:
        """SDNEntry sdn_name cannot be empty."""
        with pytest.raises(ValidationError):
            SDNEntry(ent_num=306, sdn_name="")


class TestAltEntry:
    """Tests for AltEntry model."""

    def test_create_alt_entry(self) -> None:
        """AltEntry can be created with required fields."""
        alt = AltEntry(ent_num=306, alt_num=220, alt_name="NATIONAL BANK OF CUBA")
        assert alt.ent_num == 306
        assert alt.alt_num == 220
        assert alt.alt_name == "NATIONAL BANK OF CUBA"

    def test_alt_entry_with_type(self) -> None:
        """AltEntry can include alt_type."""
        alt = AltEntry(
            ent_num=306, alt_num=220, alt_type="aka", alt_name="NATIONAL BANK OF CUBA"
        )
        assert alt.alt_type == "aka"

    def test_alt_entry_converts_ofac_null(self) -> None:
        """AltEntry converts '-0-' to None for optional fields."""
        alt = AltEntry(
            ent_num=306,
            alt_num=220,
            alt_type="-0-",  # type: ignore[arg-type]
            alt_name="TEST NAME",
            alt_remarks="-0-",  # type: ignore[arg-type]
        )
        assert alt.alt_type is None
        assert alt.alt_remarks is None

    def test_alt_entry_coerces_ids_to_int(self) -> None:
        """AltEntry coerces string IDs to integers."""
        alt = AltEntry(
            ent_num="306",  # type: ignore[arg-type]
            alt_num="220",  # type: ignore[arg-type]
            alt_name="TEST",
        )
        assert alt.ent_num == 306
        assert alt.alt_num == 220

    def test_alt_entry_requires_alt_name(self) -> None:
        """AltEntry requires alt_name."""
        with pytest.raises(ValidationError):
            AltEntry(ent_num=306, alt_num=220)  # type: ignore[call-arg]


class TestAddressEntry:
    """Tests for AddressEntry model."""

    def test_create_address_entry(self) -> None:
        """AddressEntry can be created with required fields."""
        addr = AddressEntry(ent_num=306, add_num=199)
        assert addr.ent_num == 306
        assert addr.add_num == 199

    def test_address_entry_with_all_fields(self) -> None:
        """AddressEntry can include all fields."""
        addr = AddressEntry(
            ent_num=306,
            add_num=199,
            address="Zweierstrasse 35",
            city_state_zip="Zurich CH-8022",
            country="Switzerland",
            add_remarks=None,
        )
        assert addr.address == "Zweierstrasse 35"
        assert addr.city_state_zip == "Zurich CH-8022"
        assert addr.country == "Switzerland"

    def test_address_entry_converts_ofac_null(self) -> None:
        """AddressEntry converts '-0-' to None."""
        addr = AddressEntry(
            ent_num=306,
            add_num=199,
            address="-0-",  # type: ignore[arg-type]
            country="-0-",  # type: ignore[arg-type]
        )
        assert addr.address is None
        assert addr.country is None

    def test_address_entry_coerces_ids_to_int(self) -> None:
        """AddressEntry coerces string IDs to integers."""
        addr = AddressEntry(
            ent_num="306",  # type: ignore[arg-type]
            add_num="199",  # type: ignore[arg-type]
        )
        assert addr.ent_num == 306
        assert addr.add_num == 199


class TestOFACDataVersion:
    """Tests for OFACDataVersion model."""

    def test_create_version(self) -> None:
        """OFACDataVersion can be created with defaults."""
        version = OFACDataVersion()
        assert version.sdn_count == 0
        assert version.source == "SDN"

    def test_version_with_counts(self) -> None:
        """OFACDataVersion can track counts."""
        version = OFACDataVersion(
            publish_date="2024-12-01",
            sdn_count=18422,
            alt_count=20104,
            add_count=24170,
            source="SDN",
        )
        assert version.sdn_count == 18422
        assert version.alt_count == 20104
        assert version.add_count == 24170

    def test_version_counts_non_negative(self) -> None:
        """OFACDataVersion counts must be non-negative."""
        with pytest.raises(ValidationError):
            OFACDataVersion(sdn_count=-1)


class TestCSVColumns:
    """Tests for CSV column definitions."""

    def test_sdn_csv_columns(self) -> None:
        """SDN_CSV_COLUMNS has expected columns."""
        assert "ent_num" in SDN_CSV_COLUMNS
        assert "sdn_name" in SDN_CSV_COLUMNS
        assert "programs" in SDN_CSV_COLUMNS
        assert len(SDN_CSV_COLUMNS) == 12

    def test_alt_csv_columns(self) -> None:
        """ALT_CSV_COLUMNS has expected columns."""
        assert "ent_num" in ALT_CSV_COLUMNS
        assert "alt_name" in ALT_CSV_COLUMNS
        assert len(ALT_CSV_COLUMNS) == 5

    def test_add_csv_columns(self) -> None:
        """ADD_CSV_COLUMNS has expected columns."""
        assert "ent_num" in ADD_CSV_COLUMNS
        assert "country" in ADD_CSV_COLUMNS
        assert len(ADD_CSV_COLUMNS) == 6


class TestSchemaImports:
    """Tests for schema imports."""

    def test_import_from_schemas(self) -> None:
        """Schemas can be imported from ofac.data.schemas."""
        from ofac.data.schemas import AddressEntry, AltEntry, SDNEntry

        assert SDNEntry is not None
        assert AltEntry is not None
        assert AddressEntry is not None

    def test_import_from_data(self) -> None:
        """Schemas can be imported from ofac.data."""
        from ofac.data import AddressEntry, AltEntry, SDNEntry

        assert SDNEntry is not None
        assert AltEntry is not None
        assert AddressEntry is not None


class TestRealWorldExamples:
    """Tests using real OFAC data examples from documentation."""

    def test_banco_nacional_de_cuba(self) -> None:
        """Parse real SDN entry: BANCO NACIONAL DE CUBA."""
        sdn = SDNEntry(
            ent_num=306,
            sdn_name="BANCO NACIONAL DE CUBA",
            sdn_type="-0-",  # type: ignore[arg-type]
            programs="CUBA",
            title="-0-",  # type: ignore[arg-type]
            call_sign="-0-",  # type: ignore[arg-type]
            vess_type="-0-",  # type: ignore[arg-type]
            tonnage="-0-",  # type: ignore[arg-type]
            grt="-0-",  # type: ignore[arg-type]
            vess_flag="-0-",  # type: ignore[arg-type]
            vess_owner="-0-",  # type: ignore[arg-type]
            remarks="a.k.a. 'BNC'.",
        )
        assert sdn.ent_num == 306
        assert sdn.sdn_name == "BANCO NACIONAL DE CUBA"
        assert sdn.sdn_type is None  # Converted from -0-
        assert sdn.programs == "CUBA"

    def test_banco_nacional_alias(self) -> None:
        """Parse real ALT entry: NATIONAL BANK OF CUBA."""
        alt = AltEntry(
            ent_num=306,
            alt_num=220,
            alt_type="aka",
            alt_name="NATIONAL BANK OF CUBA",
            alt_remarks="-0-",  # type: ignore[arg-type]
        )
        assert alt.ent_num == 306
        assert alt.alt_name == "NATIONAL BANK OF CUBA"
        assert alt.alt_type == "aka"
        assert alt.alt_remarks is None

    def test_banco_nacional_address(self) -> None:
        """Parse real ADD entry: Zurich address."""
        addr = AddressEntry(
            ent_num=306,
            add_num=199,
            address="Zweierstrasse 35",
            city_state_zip="Zurich CH-8022",
            country="Switzerland",
            add_remarks="-0-",  # type: ignore[arg-type]
        )
        assert addr.ent_num == 306
        assert addr.country == "Switzerland"
        assert addr.add_remarks is None

