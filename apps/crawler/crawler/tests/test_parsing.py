from decimal import Decimal

from crawler.utils.parsing import normalize_whitespace, parse_decimal, parse_int


def test_normalize_whitespace():
    assert normalize_whitespace("  hello   world \n") == "hello world"
    assert normalize_whitespace(None) == ""


def test_parse_decimal():
    assert parse_decimal("R$ 1.234,56") == Decimal("1234.56")
    assert parse_decimal("$9.99") == Decimal("9.99")
    assert parse_decimal("not a number") is None


def test_parse_int():
    assert parse_int("1.234") == 1234
    assert parse_int("nope") is None
