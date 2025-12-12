"""OFAC data loader for CSV triplet files.

This module provides the OFACDataLoader class for:
- Loading SDN.CSV, ALT.CSV, ADD.CSV triplets
- Merging data by ent_num for efficient lookups
- Handling encoding issues (UTF-8 with Latin-1 fallback)
- Caching loaded data in memory

Usage:
    from ofac.data.loader import OFACDataLoader

    loader = OFACDataLoader()
    data = loader.load()
    # data.sdn_df, data.aliases_by_ent, data.addresses_by_ent
"""

from datetime import UTC, datetime
from pathlib import Path
from typing import NamedTuple

import pandas as pd

from ofac.core.config import settings
from ofac.core.exceptions import OFACNotLoadedError, OFACParseError
from ofac.data.schemas import (
    ADD_CSV_COLUMNS,
    ALT_CSV_COLUMNS,
    SDN_CSV_COLUMNS,
    OFACDataVersion,
)


class OFACData(NamedTuple):
    """Container for loaded OFAC data.

    Attributes:
        sdn_df: DataFrame with SDN entries
        alt_df: DataFrame with alternate names
        add_df: DataFrame with addresses
        aliases_by_ent: Dict mapping ent_num to list of alias names
        addresses_by_ent: Dict mapping ent_num to list of countries
        version: Metadata about the loaded data
    """

    sdn_df: pd.DataFrame
    alt_df: pd.DataFrame
    add_df: pd.DataFrame
    aliases_by_ent: dict[int, list[str]]
    addresses_by_ent: dict[int, list[str]]
    version: OFACDataVersion


class OFACDataLoader:
    """Loads and manages OFAC CSV triplet data.

    This class handles loading SDN, ALT, and ADD CSV files from disk,
    parsing them into DataFrames, and building lookup structures for
    efficient matching operations.

    Attributes:
        data_path: Path to directory containing OFAC CSV files
        _cached_data: Cached OFACData after first load

    Example:
        loader = OFACDataLoader()
        data = loader.load()
        print(f"Loaded {len(data.sdn_df)} SDN entries")
    """

    def __init__(self, data_path: Path | None = None) -> None:
        """Initialize the loader.

        Args:
            data_path: Path to OFAC data directory. Defaults to settings.ofac_data_path.
        """
        self.data_path = data_path or settings.ofac_data_path
        self._cached_data: OFACData | None = None

    @property
    def is_loaded(self) -> bool:
        """Check if data has been loaded."""
        return self._cached_data is not None

    @property
    def data(self) -> OFACData:
        """Get loaded data, raising if not loaded.

        Raises:
            OFACNotLoadedError: If load() has not been called.
        """
        if self._cached_data is None:
            raise OFACNotLoadedError(
                "OFAC data not loaded. Call load() first.",
                details={"data_path": str(self.data_path)},
            )
        return self._cached_data

    def load(self, force_reload: bool = False) -> OFACData:
        """Load OFAC CSV triplets from disk.

        Reads SDN.CSV, ALT.CSV, and ADD.CSV files, parses them into
        DataFrames, and builds lookup dictionaries for aliases and
        addresses by entity number.

        Args:
            force_reload: If True, reload even if data is cached.

        Returns:
            OFACData containing all loaded data and lookups.

        Raises:
            OFACParseError: If CSV files cannot be found or parsed.
        """
        if self._cached_data is not None and not force_reload:
            return self._cached_data

        # Build file paths
        sdn_path = self.data_path / "sdn.csv"
        alt_path = self.data_path / "alt.csv"
        add_path = self.data_path / "add.csv"

        # Check files exist
        missing_files = []
        for path in [sdn_path, alt_path, add_path]:
            if not path.exists():
                missing_files.append(path.name)

        if missing_files:
            raise OFACParseError(
                f"OFAC data files not found: {', '.join(missing_files)}",
                code="OFAC_DATA_NOT_FOUND",
                details={
                    "data_path": str(self.data_path),
                    "missing_files": missing_files,
                },
            )

        # Load CSV files
        sdn_df = self._read_csv(sdn_path, SDN_CSV_COLUMNS)
        alt_df = self._read_csv(alt_path, ALT_CSV_COLUMNS)
        add_df = self._read_csv(add_path, ADD_CSV_COLUMNS)

        # Build lookup dictionaries
        aliases_by_ent = self._build_aliases_lookup(alt_df)
        addresses_by_ent = self._build_addresses_lookup(add_df)

        # Create version info
        version = OFACDataVersion(
            sdn_count=len(sdn_df),
            alt_count=len(alt_df),
            add_count=len(add_df),
            source="SDN",
            loaded_at=datetime.now(UTC).isoformat(),
        )

        self._cached_data = OFACData(
            sdn_df=sdn_df,
            alt_df=alt_df,
            add_df=add_df,
            aliases_by_ent=aliases_by_ent,
            addresses_by_ent=addresses_by_ent,
            version=version,
        )

        return self._cached_data

    def _read_csv(self, path: Path, columns: list[str]) -> pd.DataFrame:
        """Read a CSV file with encoding fallback.

        Tries UTF-8 first, falls back to Latin-1 for encoding issues.

        Args:
            path: Path to CSV file.
            columns: Expected column names.

        Returns:
            DataFrame with parsed CSV data.

        Raises:
            OFACParseError: If CSV cannot be parsed.
        """
        try:
            # Try UTF-8 first
            df = pd.read_csv(
                path,
                names=columns,
                header=None,
                dtype=str,
                na_values=["-0-"],
                keep_default_na=True,
                encoding="utf-8",
            )
        except UnicodeDecodeError:
            # Fallback to Latin-1
            df = pd.read_csv(
                path,
                names=columns,
                header=None,
                dtype=str,
                na_values=["-0-"],
                keep_default_na=True,
                encoding="latin-1",
            )
        except Exception as e:
            raise OFACParseError(
                f"Failed to parse CSV file: {path.name}",
                details={"path": str(path), "error": str(e)},
            ) from e

        # Convert ent_num to int
        if "ent_num" in df.columns:
            df["ent_num"] = pd.to_numeric(df["ent_num"], errors="coerce").astype(
                "Int64"
            )

        # Convert other ID columns to int
        for col in ["alt_num", "add_num"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

        return df

    def _build_aliases_lookup(self, alt_df: pd.DataFrame) -> dict[int, list[str]]:
        """Build a lookup dictionary for aliases by entity number.

        Args:
            alt_df: DataFrame with alternate names.

        Returns:
            Dict mapping ent_num to list of alias names.
        """
        aliases: dict[int, list[str]] = {}

        for _, row in alt_df.iterrows():
            ent_num = row.get("ent_num")
            alt_name = row.get("alt_name")

            if pd.notna(ent_num) and pd.notna(alt_name):
                ent_num_int = int(ent_num)
                if ent_num_int not in aliases:
                    aliases[ent_num_int] = []
                aliases[ent_num_int].append(str(alt_name))

        return aliases

    def _build_addresses_lookup(self, add_df: pd.DataFrame) -> dict[int, list[str]]:
        """Build a lookup dictionary for countries by entity number.

        Args:
            add_df: DataFrame with addresses.

        Returns:
            Dict mapping ent_num to list of country names.
        """
        addresses: dict[int, list[str]] = {}

        for _, row in add_df.iterrows():
            ent_num = row.get("ent_num")
            country = row.get("country")

            if pd.notna(ent_num) and pd.notna(country):
                ent_num_int = int(ent_num)
                if ent_num_int not in addresses:
                    addresses[ent_num_int] = []
                country_str = str(country).strip()
                if country_str and country_str not in addresses[ent_num_int]:
                    addresses[ent_num_int].append(country_str)

        return addresses

    def get_aliases(self, ent_num: int) -> list[str]:
        """Get all aliases for an entity.

        Args:
            ent_num: OFAC entity number.

        Returns:
            List of alias names, or empty list if none found.

        Raises:
            OFACNotLoadedError: If load() has not been called.
        """
        return self.data.aliases_by_ent.get(ent_num, [])

    def get_countries(self, ent_num: int) -> list[str]:
        """Get all countries for an entity.

        Args:
            ent_num: OFAC entity number.

        Returns:
            List of country names, or empty list if none found.

        Raises:
            OFACNotLoadedError: If load() has not been called.
        """
        return self.data.addresses_by_ent.get(ent_num, [])

    def clear_cache(self) -> None:
        """Clear cached data, forcing reload on next access."""
        self._cached_data = None


__all__ = ["OFACData", "OFACDataLoader"]

