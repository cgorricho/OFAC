"""Basic package tests to verify setup is working."""


def test_ofac_package_imports() -> None:
    """Verify that the ofac package can be imported."""
    import ofac

    assert ofac.__version__ == "0.1.0"


def test_ofac_core_module_imports() -> None:
    """Verify that core module can be imported."""
    from ofac import core  # noqa: F401

    assert True


def test_ofac_data_module_imports() -> None:
    """Verify that data module can be imported."""
    from ofac import data  # noqa: F401

    assert True


def test_ofac_api_module_imports() -> None:
    """Verify that api module can be imported."""
    from ofac import api  # noqa: F401

    assert True


def test_ofac_streamlit_module_imports() -> None:
    """Verify that streamlit module can be imported."""
    from ofac import streamlit  # noqa: F401

    assert True
