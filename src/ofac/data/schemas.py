"""OFAC data schemas for CSV triplet parsing.

This module provides Pydantic models for parsing OFAC CSV files:
- SDNEntry: Specially Designated Nationals (SDN.CSV)
- AltEntry: Alternate names/aliases (ALT.CSV)
- AddressEntry: Addresses (ADD.CSV)

The schemas match OFAC CSV column headers and handle:
- Nullable fields (marked with "-0-" in OFAC data)
- Type coercion (strings to integers for IDs)
- Unicode/encoding variations

Usage:
    from ofac.data.schemas import SDNEntry, AltEntry, AddressEntry

    # Parse a row from SDN.CSV
    sdn = SDNEntry.from_csv_row(row_dict)
"""

from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, field_validator


class SDNType(str, Enum):
    """OFAC entity types.

    Individual: Natural person
    Entity: Organization/company
    Vessel: Ship
    Aircraft: Airplane/helicopter
    """

    INDIVIDUAL = "individual"
    ENTITY = "entity"
    VESSEL = "vessel"
    AIRCRAFT = "aircraft"


class AltType(str, Enum):
    """Alternate name types.

    AKA: Also Known As (current alias)
    FKA: Formerly Known As (previous name)
    NKA: Now Known As (current name after change)
    """

    AKA = "aka"
    FKA = "fka"
    NKA = "nka"


class SDNEntry(BaseModel):
    """OFAC SDN (Specially Designated Nationals) entry from SDN.CSV.

    Represents a sanctioned entity with all associated metadata.

    Attributes:
        ent_num: Unique OFAC entity number (primary key)
        sdn_name: Entity name (primary name for matching)
        sdn_type: Entity type (individual, entity, vessel, aircraft)
        programs: Sanctions programs (e.g., "SDGT", "IRAN")
        title: Title or position (for individuals)
        call_sign: Vessel/aircraft call sign
        vess_type: Vessel type
        tonnage: Vessel tonnage
        grt: Gross registered tonnage
        vess_flag: Vessel flag country
        vess_owner: Vessel owner
        remarks: Additional information (DOB, POB, nationalities, etc.)
    """

    ent_num: int = Field(..., description="OFAC entity number (primary key)")
    sdn_name: str = Field(..., min_length=1, description="Entity name")
    sdn_type: str | None = Field(default=None, description="Entity type")
    programs: str | None = Field(default=None, description="Sanctions programs")
    title: str | None = Field(default=None, description="Title/position")
    call_sign: str | None = Field(default=None, description="Call sign")
    vess_type: str | None = Field(default=None, description="Vessel type")
    tonnage: str | None = Field(default=None, description="Tonnage")
    grt: str | None = Field(default=None, description="Gross registered tonnage")
    vess_flag: str | None = Field(default=None, description="Vessel flag country")
    vess_owner: str | None = Field(default=None, description="Vessel owner")
    remarks: str | None = Field(default=None, description="Additional remarks")

    model_config = ConfigDict(
        populate_by_name=True,
        str_strip_whitespace=True,
    )

    @field_validator("*", mode="before")
    @classmethod
    def convert_ofac_null(cls, v: str | int | None) -> str | int | None:
        """Convert OFAC null marker '-0-' to None."""
        if isinstance(v, str) and v.strip() == "-0-":
            return None
        return v

    @field_validator("ent_num", mode="before")
    @classmethod
    def coerce_ent_num(cls, v: str | int) -> int:
        """Coerce ent_num to integer."""
        if isinstance(v, str):
            return int(v.strip())
        return v

    @property
    def programs_list(self) -> list[str]:
        """Parse programs field into list.

        OFAC programs are typically separated by "; ".

        Returns:
            List of program codes (e.g., ["SDGT", "IRAN"])
        """
        if not self.programs:
            return []
        return [p.strip() for p in self.programs.split(";") if p.strip()]


class AltEntry(BaseModel):
    """OFAC alternate name entry from ALT.CSV.

    Represents an alias or alternate name for an SDN entity.
    Critical for fuzzy matching - captures spelling variations,
    transliterations, and name changes.

    Attributes:
        ent_num: OFAC entity number (foreign key to SDNEntry)
        alt_num: Alternate name number (unique within entity)
        alt_type: Type of alternate name (aka, fka, nka)
        alt_name: The alternate name string
        alt_remarks: Additional remarks about this alias
    """

    ent_num: int = Field(..., description="OFAC entity number (FK to SDN)")
    alt_num: int = Field(..., description="Alternate name number")
    alt_type: str | None = Field(default=None, description="Alt type (aka/fka/nka)")
    alt_name: str = Field(..., min_length=1, description="Alternate name")
    alt_remarks: str | None = Field(default=None, description="Remarks")

    model_config = ConfigDict(
        populate_by_name=True,
        str_strip_whitespace=True,
    )

    @field_validator("*", mode="before")
    @classmethod
    def convert_ofac_null(cls, v: str | int | None) -> str | int | None:
        """Convert OFAC null marker '-0-' to None."""
        if isinstance(v, str) and v.strip() == "-0-":
            return None
        return v

    @field_validator("ent_num", "alt_num", mode="before")
    @classmethod
    def coerce_to_int(cls, v: str | int) -> int:
        """Coerce ID fields to integer."""
        if isinstance(v, str):
            return int(v.strip())
        return v

    @field_validator("alt_name", mode="before")
    @classmethod
    def ensure_alt_name(cls, v: str | None) -> str:
        """Ensure alt_name is not null (it's required)."""
        if v is None or (isinstance(v, str) and v.strip() == "-0-"):
            return ""
        return v


class AddressEntry(BaseModel):
    """OFAC address entry from ADD.CSV.

    Represents a known address for an SDN entity.
    Used for country-based score boosting/de-boosting.

    Attributes:
        ent_num: OFAC entity number (foreign key to SDNEntry)
        add_num: Address number (unique within entity)
        address: Street address
        city_state_zip: City, state, and postal code
        country: Country name
        add_remarks: Additional remarks
    """

    ent_num: int = Field(..., description="OFAC entity number (FK to SDN)")
    add_num: int = Field(..., description="Address number")
    address: str | None = Field(default=None, description="Street address")
    city_state_zip: str | None = Field(
        default=None, description="City, state, postal code"
    )
    country: str | None = Field(default=None, description="Country name")
    add_remarks: str | None = Field(default=None, description="Remarks")

    model_config = ConfigDict(
        populate_by_name=True,
        str_strip_whitespace=True,
    )

    @field_validator("*", mode="before")
    @classmethod
    def convert_ofac_null(cls, v: str | int | None) -> str | int | None:
        """Convert OFAC null marker '-0-' to None."""
        if isinstance(v, str) and v.strip() == "-0-":
            return None
        return v

    @field_validator("ent_num", "add_num", mode="before")
    @classmethod
    def coerce_to_int(cls, v: str | int) -> int:
        """Coerce ID fields to integer."""
        if isinstance(v, str):
            return int(v.strip())
        return v


class OFACDataVersion(BaseModel):
    """Metadata about loaded OFAC data.

    Tracks version and statistics of loaded OFAC data
    for audit trail and freshness display.

    Attributes:
        publish_date: OFAC data publication date
        sdn_count: Number of SDN entries
        alt_count: Number of alternate name entries
        add_count: Number of address entries
        source: Data source (SDN, CONSOLIDATED, or BOTH)
        loaded_at: When data was loaded into memory
    """

    publish_date: str | None = Field(default=None, description="OFAC publish date")
    sdn_count: int = Field(default=0, ge=0, description="SDN entry count")
    alt_count: int = Field(default=0, ge=0, description="Alt name count")
    add_count: int = Field(default=0, ge=0, description="Address count")
    source: str = Field(default="SDN", description="Data source")
    loaded_at: str | None = Field(default=None, description="Load timestamp")

    model_config = ConfigDict(
        populate_by_name=True,
    )


# CSV column name mappings (OFAC uses these exact headers)
SDN_CSV_COLUMNS = [
    "ent_num",
    "sdn_name",
    "sdn_type",
    "programs",
    "title",
    "call_sign",
    "vess_type",
    "tonnage",
    "grt",
    "vess_flag",
    "vess_owner",
    "remarks",
]

ALT_CSV_COLUMNS = [
    "ent_num",
    "alt_num",
    "alt_type",
    "alt_name",
    "alt_remarks",
]

ADD_CSV_COLUMNS = [
    "ent_num",
    "add_num",
    "address",
    "city_state_zip",
    "country",
    "add_remarks",
]


__all__ = [
    "SDNType",
    "AltType",
    "SDNEntry",
    "AltEntry",
    "AddressEntry",
    "OFACDataVersion",
    "SDN_CSV_COLUMNS",
    "ALT_CSV_COLUMNS",
    "ADD_CSV_COLUMNS",
]
