def test_valid_units():
    """
    Tests tools.valid_units function
    """
    try:
        import pytest
        from tools import valid_units
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    assert valid_units("day") is True
    assert valid_units("week") is True
    assert valid_units("month") is True
    assert valid_units("year") is True
    assert valid_units("second") is False
    assert valid_units("none") is False
    assert valid_units(0) is False
    assert valid_units(None) is False
