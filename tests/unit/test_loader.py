"""Unit tests for OFAC data loader."""

from pathlib import Path

import pandas as pd
import pytest

from ofac.core.exceptions import OFACNotLoadedError, OFACParseError
from ofac.data.loader import OFACData, OFACDataLoader


@pytest.fixture
def mock_ofac_data_path(mock_ofac_data_dir: Path) -> Path:
    """Return path to mock OFAC data directory."""
    return mock_ofac_data_dir


@pytest.fixture
def loader(mock_ofac_data_path: Path) -> OFACDataLoader:
    """Create a loader with mock data path."""
    return OFACDataLoader(data_path=mock_ofac_data_path)


class TestOFACDataLoader:
    """Tests for OFACDataLoader class."""

    def test_create_loader_default_path(self) -> None:
        """Loader uses settings.ofac_data_path by default."""
        loader = OFACDataLoader()
        assert loader.data_path is not None

    def test_create_loader_custom_path(self, mock_ofac_data_path: Path) -> None:
        """Loader can use custom data path."""
        loader = OFACDataLoader(data_path=mock_ofac_data_path)
        assert loader.data_path == mock_ofac_data_path

    def test_is_loaded_false_before_load(self, loader: OFACDataLoader) -> None:
        """is_loaded returns False before load() is called."""
        assert loader.is_loaded is False

    def test_is_loaded_true_after_load(self, loader: OFACDataLoader) -> None:
        """is_loaded returns True after load() is called."""
        loader.load()
        assert loader.is_loaded is True

    def test_data_raises_before_load(self, loader: OFACDataLoader) -> None:
        """Accessing data property before load() raises OFACNotLoadedError."""
        with pytest.raises(OFACNotLoadedError) as exc_info:
            _ = loader.data
        assert exc_info.value.code == "OFAC_NOT_LOADED"

    def test_clear_cache(self, loader: OFACDataLoader) -> None:
        """clear_cache() resets is_loaded to False."""
        loader.load()
        assert loader.is_loaded is True
        loader.clear_cache()
        assert loader.is_loaded is False


class TestLoadMethod:
    """Tests for the load() method."""

    def test_load_returns_ofac_data(self, loader: OFACDataLoader) -> None:
        """load() returns OFACData named tuple."""
        data = loader.load()
        assert isinstance(data, OFACData)

    def test_load_parses_sdn_csv(self, loader: OFACDataLoader) -> None:
        """load() parses SDN.CSV into DataFrame."""
        data = loader.load()
        assert isinstance(data.sdn_df, pd.DataFrame)
        assert len(data.sdn_df) == 4  # 4 entries in mock data

    def test_load_parses_alt_csv(self, loader: OFACDataLoader) -> None:
        """load() parses ALT.CSV into DataFrame."""
        data = loader.load()
        assert isinstance(data.alt_df, pd.DataFrame)
        assert len(data.alt_df) == 6  # 6 aliases in mock data

    def test_load_parses_add_csv(self, loader: OFACDataLoader) -> None:
        """load() parses ADD.CSV into DataFrame."""
        data = loader.load()
        assert isinstance(data.add_df, pd.DataFrame)
        assert len(data.add_df) == 5  # 5 addresses in mock data

    def test_load_converts_ent_num_to_int(self, loader: OFACDataLoader) -> None:
        """load() converts ent_num column to integer."""
        data = loader.load()
        assert data.sdn_df["ent_num"].dtype.name == "Int64"

    def test_load_builds_aliases_lookup(self, loader: OFACDataLoader) -> None:
        """load() builds aliases_by_ent dictionary."""
        data = loader.load()
        assert isinstance(data.aliases_by_ent, dict)
        # Entity 306 has 2 aliases
        assert 306 in data.aliases_by_ent
        assert len(data.aliases_by_ent[306]) == 2

    def test_load_builds_addresses_lookup(self, loader: OFACDataLoader) -> None:
        """load() builds addresses_by_ent dictionary."""
        data = loader.load()
        assert isinstance(data.addresses_by_ent, dict)
        # Entity 306 has 2 countries (Switzerland, Cuba)
        assert 306 in data.addresses_by_ent
        assert len(data.addresses_by_ent[306]) == 2

    def test_load_creates_version_info(self, loader: OFACDataLoader) -> None:
        """load() creates OFACDataVersion with counts."""
        data = loader.load()
        assert data.version.sdn_count == 4
        assert data.version.alt_count == 6
        assert data.version.add_count == 5
        assert data.version.source == "SDN"
        assert data.version.loaded_at is not None

    def test_load_caches_data(self, loader: OFACDataLoader) -> None:
        """load() caches data for subsequent calls."""
        data1 = loader.load()
        data2 = loader.load()
        assert data1 is data2  # Same object

    def test_load_force_reload(self, loader: OFACDataLoader) -> None:
        """load(force_reload=True) reloads data."""
        data1 = loader.load()
        data2 = loader.load(force_reload=True)
        # Different objects but same content
        assert data1 is not data2
        assert len(data1.sdn_df) == len(data2.sdn_df)


class TestMissingFiles:
    """Tests for missing file handling."""

    def test_load_raises_on_missing_files(self, tmp_path: Path) -> None:
        """load() raises OFACParseError when files are missing."""
        loader = OFACDataLoader(data_path=tmp_path)
        with pytest.raises(OFACParseError) as exc_info:
            loader.load()
        assert exc_info.value.code == "OFAC_DATA_NOT_FOUND"
        assert "missing_files" in exc_info.value.details

    def test_error_lists_all_missing_files(self, tmp_path: Path) -> None:
        """Error details list all missing files."""
        loader = OFACDataLoader(data_path=tmp_path)
        with pytest.raises(OFACParseError) as exc_info:
            loader.load()
        missing = exc_info.value.details["missing_files"]
        assert "sdn.csv" in missing
        assert "alt.csv" in missing
        assert "add.csv" in missing


class TestAliasLookup:
    """Tests for get_aliases() method."""

    def test_get_aliases_for_entity(self, loader: OFACDataLoader) -> None:
        """get_aliases() returns list of aliases for entity."""
        loader.load()
        aliases = loader.get_aliases(306)
        assert "NATIONAL BANK OF CUBA" in aliases
        assert "CUBAN NATIONAL BANK" in aliases

    def test_get_aliases_returns_empty_for_unknown(
        self, loader: OFACDataLoader
    ) -> None:
        """get_aliases() returns empty list for unknown entity."""
        loader.load()
        aliases = loader.get_aliases(99999)
        assert aliases == []

    def test_get_aliases_raises_before_load(self, loader: OFACDataLoader) -> None:
        """get_aliases() raises OFACNotLoadedError before load()."""
        with pytest.raises(OFACNotLoadedError):
            loader.get_aliases(306)


class TestCountryLookup:
    """Tests for get_countries() method."""

    def test_get_countries_for_entity(self, loader: OFACDataLoader) -> None:
        """get_countries() returns list of countries for entity."""
        loader.load()
        countries = loader.get_countries(306)
        assert "Switzerland" in countries
        assert "Cuba" in countries

    def test_get_countries_returns_empty_for_unknown(
        self, loader: OFACDataLoader
    ) -> None:
        """get_countries() returns empty list for unknown entity."""
        loader.load()
        countries = loader.get_countries(99999)
        assert countries == []

    def test_get_countries_raises_before_load(self, loader: OFACDataLoader) -> None:
        """get_countries() raises OFACNotLoadedError before load()."""
        with pytest.raises(OFACNotLoadedError):
            loader.get_countries(306)


class TestDataContent:
    """Tests for actual data content from mock files."""

    def test_sdn_banco_nacional(self, loader: OFACDataLoader) -> None:
        """Verify BANCO NACIONAL DE CUBA entry is parsed correctly."""
        data = loader.load()
        banco = data.sdn_df[data.sdn_df["ent_num"] == 306].iloc[0]
        assert banco["sdn_name"] == "BANCO NACIONAL DE CUBA"
        assert banco["programs"] == "CUBA"
        assert "BNC" in banco["remarks"]

    def test_sdn_al_qaida(self, loader: OFACDataLoader) -> None:
        """Verify AL-QAIDA entry is parsed correctly."""
        data = loader.load()
        aq = data.sdn_df[data.sdn_df["ent_num"] == 1000].iloc[0]
        assert aq["sdn_name"] == "AL-QAIDA"
        assert aq["programs"] == "SDGT"

    def test_aliases_content(self, loader: OFACDataLoader) -> None:
        """Verify alias content is correct."""
        loader.load()
        aq_aliases = loader.get_aliases(1000)
        assert "AL QAEDA" in aq_aliases
        assert "THE BASE" in aq_aliases


class TestLoaderImports:
    """Tests for loader imports."""

    def test_import_from_loader(self) -> None:
        """OFACDataLoader can be imported from ofac.data.loader."""
        from ofac.data.loader import OFACData, OFACDataLoader

        assert OFACDataLoader is not None
        assert OFACData is not None
