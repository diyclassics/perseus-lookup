#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Greek-Lookup: A simple command-Line lookup for the Perseus Greek Word Study Tool
    cf. http://www.perseus.tufts.edu/hopper/morph?la=gr

Greek-Lookup is a script for looking up Greek word using Perseus and return a list of available short definitions. Can take multiple words as arguments. Written by @diyclassics 8.15.14.

e.g.
$ python greek-lookup.py logos
$ logos > λόγος: computation, reckoning


$ python greek-lookup.py dew
$ dew > δέω: bind, tie, fetter,
$ dew > δέω2: lack, miss, stand in need of,
$ dew > δεῖ: there is need

$python greek-lookup.py verbum curas
$ logos > λόγος: computation, reckoning
$
$ dew > δέω: bind, tie, fetter,
$ dew > δέω2: lack, miss, stand in need of,
$ dew > δεῖ: there is need
"""

# imports
import sys
import requests
import re
from bs4 import BeautifulSoup

# constants
URL_BASE = "http://www.perseus.tufts.edu/hopper/morph"


def lookup_word(word):
    # Takes string
    # Returns a BeautifulSoup object containing the html of the
    # Perseus Word Study Tool entry for that word; or
    # if the word is not found, returns -1

    # Custom headers to mimic a browser request, change as necessary
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:129.0) Gecko/20100101 Firefox/129.0"
    }

    # Get html using Requests and Beautiful Soup
    parameters = {"la": "gr", "l": word}
    try:
        response = requests.get(URL_BASE, params=parameters, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses
        soup = BeautifulSoup(response.text, "html.parser")

        # Check to see if the Perseus Word Study Tool page is valid before returning
        if len(soup.findAll(string=re.compile("no information"))) == 0:
            return soup
        else:
            return -1
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 405:
            print(f"HTTP error 405: Method Not Allowed for URL {response.url}")
        else:
            print(f"HTTP error occurred: {http_err}")
        return -1
    except Exception as err:
        print(f"Other error occurred: {err}")
        return -1


def get_definitions(soup):
    # Take BeautifulSoup object
    # Returns a list of tuples with the structure (lemma, lemma_definition)

    lemmas = soup.find_all("h4", class_="greek")
    lemma_definitions = soup.find_all("span", class_="lemma_definition")

    lemma_list, lemma_definition_list = [], []

    for lemma in lemmas:
        lemma_list.append(lemma.text.strip())

    for lemma_definition in lemma_definitions:
        lemma_definition_list.append(lemma_definition.text.strip())

    definitions = zip(lemma_list, lemma_definition_list)

    return definitions


def main(query):
    soup = lookup_word(query)

    if soup == -1:
        print("No definition found for " + query + ".")
    else:
        definitions = get_definitions(soup)
        for definition in definitions:
            print(query + " > " + definition[0] + ": " + definition[1])


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No argument given.")
    else:
        for item in sys.argv[1:]:
            main(item)
