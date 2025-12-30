#!/usr/bin/env python3

"""

Latin-Lookup: A simple command-line lookup for the Perseus Latin Word Study Tool
    cf. http://www.perseus.tufts.edu/hopper/morph?la=la

Latin-Lookup is a script for looking up Latin words using Perseus and returning a list of available short definitions. Can take multiple words as arguments. Written by @diyclassics 8.15.14.

Examples:
    $ python latin_lookup.py verbum
    verbum > verbum: a word

    $ python latin_lookup.py curas
    curas > cura: trouble, care, attention, pains, industry, diligence, exertion
    curas > curo: to care for, take pains with, be solicitous for, look to, attend to, regard

    $ python latin_lookup.py verbum curas
    verbum > verbum: a word
    curas > cura: trouble, care, attention, pains, industry, diligence, exertion
    curas > curo: to care for, take pains with, be solicitous for, look to, attend to, regard

"""

# imports

import sys
import requests
import re
from bs4 import BeautifulSoup
from typing import Optional, List, Tuple

# constants
URL_BASE = "http://www.perseus.tufts.edu/hopper/morph"


def lookup_word(
    word: str, session: Optional[requests.Session] = None
) -> Optional[BeautifulSoup]:
    """
    Looks up a Latin word using the Perseus Word Study Tool.
    Returns a BeautifulSoup object containing the HTML of the entry for that word,
    or None if the word is not found or an error occurs.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:129.0) Gecko/20100101 Firefox/129.0"
    }
    parameters = {"la": "la", "l": word}
    sess = session or requests
    try:
        response = sess.get(URL_BASE, params=parameters, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        if not soup.find(string=re.compile("no information")):
            return soup
        else:
            return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"Other error occurred: {err}")
        return None


def get_definitions(soup: BeautifulSoup) -> List[Tuple[str, str]]:
    """
    Takes a BeautifulSoup object and returns a list of (lemma, lemma_definition) tuples.
    """
    lemmas = soup.find_all("h4", class_="la")
    lemma_definitions = soup.find_all("span", class_="lemma_definition")
    lemma_list = [lemma.text.strip() for lemma in lemmas]
    lemma_definition_list = [
        " ".join(lemma_definition.text.strip().split())
        for lemma_definition in lemma_definitions
    ]
    return list(zip(lemma_list, lemma_definition_list))


def format_definitions(query: str, definitions: List[Tuple[str, str]]) -> List[str]:
    """
    Formats the definitions for output.
    """
    return [f"{query} > {lemma}: {definition}" for lemma, definition in definitions]


def main(query: str) -> None:
    soup = lookup_word(query)
    if soup is None:
        print(f"No definition found for {query}.")
    else:
        definitions = get_definitions(soup)
        for line in format_definitions(query, definitions):
            print(line)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No argument given.")
    else:
        for item in sys.argv[1:]:
            main(item)
