import pytest
import sys
import os
from typing import Optional

# Ensure the parent directory is in sys.path for imports
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from greek_lookup import lookup_word, get_definitions
from latin_lookup import (
    lookup_word as lookup_word_lat,
    get_definitions as get_definitions_lat,
)


# Note: These tests use real HTTP requests. For true unit tests, mock requests.get and BeautifulSoup.


def test_greek_lookup_valid() -> None:
    soup = lookup_word("logos")
    assert soup is not None
    defs = get_definitions(soup)
    assert any("λόγος" in d[0] for d in defs)


def test_greek_lookup_invalid() -> None:
    soup = lookup_word("notarealgreekword")
    assert soup is None


def test_latin_lookup_valid() -> None:
    soup = lookup_word_lat("verbum")
    assert soup is not None
    defs = get_definitions_lat(soup)
    assert any("verbum" in d[0] for d in defs)


def test_latin_lookup_invalid() -> None:
    soup = lookup_word_lat("notareallatinword")
    assert soup is None
