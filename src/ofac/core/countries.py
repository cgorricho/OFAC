"""Sanctioned countries registry and General License mappings.

This module provides utilities for checking if countries are OFAC-sanctioned
and retrieving applicable General Licenses for humanitarian operations.

Usage:
    from ofac.core.countries import is_sanctioned_country, get_general_license

    if is_sanctioned_country("SY"):
        gl = get_general_license("SY")  # Returns GL-21 info
"""

from typing import NamedTuple


class GeneralLicense(NamedTuple):
    """General License information.

    Attributes:
        code: General License code (e.g., "GL-21")
        description: Human-readable description
        applicable_countries: List of ISO country codes this GL applies to
    """

    code: str
    description: str
    applicable_countries: list[str]


# OFAC-sanctioned countries (ISO 3166-1 alpha-2 codes)
SANCTIONED_COUNTRIES: set[str] = {
    "SY",  # Syria
    "IR",  # Iran
    "CU",  # Cuba
    "KP",  # North Korea (Democratic People's Republic of Korea)
    "VE",  # Venezuela
    "BY",  # Belarus
    "RU",  # Russia (partial sanctions)
    "MM",  # Myanmar (Burma)
    "SD",  # Sudan
    "LY",  # Libya (partial sanctions)
}

# General License mappings
GENERAL_LICENSES: dict[str, GeneralLicense] = {
    "SY": GeneralLicense(
        code="GL-21",
        description="Syria Humanitarian License - Authorizes certain humanitarian activities",
        applicable_countries=["SY"],
    ),
    "IR": GeneralLicense(
        code="GL D-1",
        description="Iran Humanitarian License - Authorizes certain humanitarian transactions",
        applicable_countries=["IR"],
    ),
    "VE": GeneralLicense(
        code="GL-41",
        description="Venezuela Humanitarian License - Authorizes certain humanitarian activities",
        applicable_countries=["VE"],
    ),
    "CU": GeneralLicense(
        code="GL-21",
        description="Cuba Humanitarian License - Authorizes certain humanitarian activities",
        applicable_countries=["CU"],
    ),
}


def is_sanctioned_country(country_code: str) -> bool:
    """Check if a country is OFAC-sanctioned.

    Args:
        country_code: ISO 3166-1 alpha-2 country code (e.g., "SY", "IR").

    Returns:
        True if the country is sanctioned, False otherwise.

    Example:
        is_sanctioned_country("SY")  # Returns True
        is_sanctioned_country("US")  # Returns False
    """
    if not country_code:
        return False
    return country_code.upper() in SANCTIONED_COUNTRIES


def get_general_license(country_code: str) -> GeneralLicense | None:
    """Get General License information for a sanctioned country.

    Args:
        country_code: ISO 3166-1 alpha-2 country code.

    Returns:
        GeneralLicense if available, None otherwise.

    Example:
        gl = get_general_license("SY")  # Returns GL-21 info
        gl = get_general_license("US")  # Returns None
    """
    if not country_code:
        return None
    return GENERAL_LICENSES.get(country_code.upper())


def get_all_sanctioned_countries() -> set[str]:
    """Get all sanctioned country codes.

    Returns:
        Set of ISO country codes for sanctioned countries.
    """
    return SANCTIONED_COUNTRIES.copy()


def get_countries_with_gl() -> list[str]:
    """Get list of countries that have General Licenses available.

    Returns:
        List of ISO country codes with available General Licenses.
    """
    return list(GENERAL_LICENSES.keys())


__all__ = [
    "is_sanctioned_country",
    "get_general_license",
    "get_all_sanctioned_countries",
    "get_countries_with_gl",
    "GeneralLicense",
    "SANCTIONED_COUNTRIES",
]
