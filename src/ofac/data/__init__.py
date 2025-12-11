"""OFAC data management layer.

This module contains:
- loader: CSV triplet parsing and DataFrame construction
- updater: Download, version tracking, and atomic swap
- schemas: OFAC data schemas (SDN, Address, Alias)
"""

from ofac.data.loader import OFACData, OFACDataLoader
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
from ofac.data.updater import OFACUpdater

__all__ = [
    # Loader
    "OFACDataLoader",
    "OFACData",
    # Updater
    "OFACUpdater",
    # Schemas
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

