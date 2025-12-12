"""Fuzzy matching engine for OFAC sanctions screening.

This module provides the EntityMatcher class for:
- Fuzzy string matching against OFAC SDN entries
- Matching against primary names and aliases
- Country-aware score boosting
- Returning sorted MatchResult objects

Usage:
    from ofac.core.matcher import EntityMatcher
    from ofac.data.loader import OFACDataLoader

    loader = OFACDataLoader()
    data = loader.load()
    matcher = EntityMatcher(data)
    matches = matcher.match("ACME Corporation", country="US")
"""

from typing import TYPE_CHECKING

from rapidfuzz import fuzz

from ofac.core.config import settings
from ofac.core.countries import is_sanctioned_country
from ofac.core.exceptions import OFACNotLoadedError
from ofac.core.models import MatchResult, MatchType, OFACList

if TYPE_CHECKING:
    from ofac.data.loader import OFACData


class EntityMatcher:
    """Fuzzy matching engine for OFAC sanctions screening.

    This class performs fuzzy string matching against OFAC SDN entries
    using RapidFuzz's token_sort_ratio algorithm. It matches against both
    primary names (sdn_name) and aliases, and applies country-aware scoring.

    Attributes:
        data: OFACData containing SDN entries, aliases, and addresses
        min_score: Minimum match score to return (default: 0)

    Example:
        matcher = EntityMatcher(ofac_data)
        matches = matcher.match("BANCO NACIONAL DE CUBA", country="Cuba")
    """

    def __init__(self, data: "OFACData", min_score: int = 0) -> None:
        """Initialize the matcher.

        Args:
            data: OFACData containing loaded SDN entries and lookups.
            min_score: Minimum match score to return (0-100). Defaults to 0.

        Raises:
            OFACNotLoadedError: If data is None or invalid.
        """
        if data is None:
            raise OFACNotLoadedError("OFAC data is required for matching")
        self.data = data
        self.min_score = max(0, min(100, min_score))

    def match(
        self,
        entity_name: str,
        country: str | None = None,
        max_results: int = 10,
    ) -> list[MatchResult]:
        """Match an entity name against OFAC SDN entries.

        Performs fuzzy matching against SDN primary names and aliases,
        applies country-aware scoring, and returns top matches sorted by score.

        Args:
            entity_name: Name of the entity to match.
            country: Optional country code/name for country-aware scoring.
            max_results: Maximum number of results to return. Defaults to 10.

        Returns:
            List of MatchResult objects sorted by score (descending).
            Empty list if no matches above min_score threshold.

        Example:
            matches = matcher.match("ACME Corporation", country="US")
            for match in matches:
                print(f"{match.sdn_name}: {match.match_score}%")
        """
        if not entity_name or not entity_name.strip():
            return []

        entity_name_clean = entity_name.strip()
        matches: list[tuple[int, MatchResult]] = []

        # Match against SDN primary names
        for _, row in self.data.sdn_df.iterrows():
            sdn_name = str(row.get("sdn_name", ""))
            if not sdn_name:
                continue

            # Calculate base match score
            score = fuzz.token_sort_ratio(entity_name_clean, sdn_name)

            # Check for exact match
            match_type = MatchType.EXACT if score == 100 else MatchType.FUZZY

            # Apply country boost if provided and countries match
            country_match = False
            if country:
                ent_num = int(row.get("ent_num", 0))
                ofac_countries = self.data.addresses_by_ent.get(ent_num, [])
                country_match = self._check_country_match(country, ofac_countries)
                if country_match:
                    score = min(100, score + settings.country_match_boost)

            # Only include matches above minimum threshold
            if score >= self.min_score:
                ent_num = int(row.get("ent_num", 0))
                sdn_type = str(row.get("sdn_type", "")) or "Unknown"
                countries = self.data.addresses_by_ent.get(ent_num, [])
                country = countries[0] if countries else None

                match_result = MatchResult(
                    sdn_name=sdn_name,
                    sdn_type=sdn_type,
                    match_score=int(score),
                    match_type=match_type,
                    ofac_list=OFACList.SDN,
                    programs=self._parse_programs(row.get("programs")),
                    ent_num=ent_num,
                    country=country,
                    country_match=country_match,
                    remarks=str(row.get("remarks", "")) or None,
                )
                matches.append((int(score), match_result))

            # Also match against aliases for this entity
            ent_num = int(row.get("ent_num", 0))
            aliases = self.data.aliases_by_ent.get(ent_num, [])
            for alias_name in aliases:
                alias_score = fuzz.token_sort_ratio(entity_name_clean, alias_name)

                # Apply country boost if provided and countries match
                alias_country_match = False
                if country:
                    ofac_countries = self.data.addresses_by_ent.get(ent_num, [])
                    alias_country_match = self._check_country_match(
                        country, ofac_countries
                    )
                    if alias_country_match:
                        alias_score = min(
                            100, alias_score + settings.country_match_boost
                        )

                if alias_score >= self.min_score:
                    ent_num = int(row.get("ent_num", 0))
                    sdn_type = str(row.get("sdn_type", "")) or "Unknown"
                    countries = self.data.addresses_by_ent.get(ent_num, [])
                    country = countries[0] if countries else None

                    match_result = MatchResult(
                        sdn_name=sdn_name,  # Keep original SDN name
                        sdn_type=sdn_type,
                        match_score=int(alias_score),
                        match_type=MatchType.ALIAS,
                        ofac_list=OFACList.SDN,
                        programs=self._parse_programs(row.get("programs")),
                        ent_num=ent_num,
                        country=country,
                        country_match=alias_country_match,
                        remarks=f"Matched alias: {alias_name}",
                    )
                    matches.append((int(alias_score), match_result))

        # Sort by score descending and return top N
        matches.sort(key=lambda x: x[0], reverse=True)
        return [match for _, match in matches[:max_results]]

    def _check_country_match(
        self, entity_country: str, ofac_countries: list[str]
    ) -> bool:
        """Check if entity country matches any OFAC entry country.

        Performs case-insensitive matching and handles country name variations.
        Also checks if country codes match (e.g., "SY" matches "Syria").

        Args:
            entity_country: Entity's country (name or ISO code).
            ofac_countries: List of countries from OFAC address data.

        Returns:
            True if countries match, False otherwise.
        """
        if not entity_country or not ofac_countries:
            return False

        entity_country_lower = entity_country.lower().strip()

        # Check for direct match or substring match
        for ofac_country in ofac_countries:
            if not ofac_country:
                continue
            ofac_country_lower = ofac_country.lower().strip()

            # Direct match
            if entity_country_lower == ofac_country_lower:
                return True

            # Substring match (e.g., "Syria" in "Syrian Arab Republic")
            if (
                entity_country_lower in ofac_country_lower
                or ofac_country_lower in entity_country_lower
            ):
                return True

            # Check if both are sanctioned countries (country code matching)
            if is_sanctioned_country(entity_country) and is_sanctioned_country(
                ofac_country
            ):
                # If both are sanctioned, consider it a match if they're the same country
                # This handles cases where country names vary but codes match
                entity_code = (
                    entity_country.upper()[:2] if len(entity_country) >= 2 else None
                )
                ofac_code = ofac_country.upper()[:2] if len(ofac_country) >= 2 else None
                if entity_code and ofac_code and entity_code == ofac_code:
                    return True

        return False

    def _parse_programs(self, programs: str | None) -> list[str]:
        """Parse programs string into list.

        Args:
            programs: Programs string (e.g., "SDGT; IRAN; CUBA").

        Returns:
            List of program codes.
        """
        if not programs or programs == "-0-":
            return []
        return [p.strip() for p in str(programs).split(";") if p.strip()]

    def match_entity(
        self,
        entity_name: str,
        country: str | None = None,
        max_results: int = 10,
    ) -> list[MatchResult]:
        """Match an entity name (alias for match() for consistency).

        This is an alias for match() to provide a more explicit API.

        Args:
            entity_name: Name of the entity to match.
            country: Optional country code/name for country-aware scoring.
            max_results: Maximum number of results to return.

        Returns:
            List of MatchResult objects sorted by score (descending).
        """
        return self.match(entity_name, country, max_results)


__all__ = ["EntityMatcher"]
