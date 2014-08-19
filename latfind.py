#! /usr/bin/env python
"""
Latfind: A simple command-Line lookup for the Perseus Latin Word Study Tool
    cf. http://www.perseus.tufts.edu/hopper/morph?la=la

Latfind is a script for looking up Latin word using Perseus and return a list of available short definitions. Can take multiple words as arguments. Written by @diyclassics 8.15.14.

e.g.
$ python latfind.py verbum
$ verbum > verbum: a word 

$ python latfind.py curas
$ curas > cura: trouble, care, attention, pains, industry, diligence, exertion
$ curas > curo: to care for, take pains with, be solicitous for, look to, attend to, regard

$python latfind.py verbum curas
$ verbum > verbum: a word 
$
$ curas > cura: trouble, care, attention, pains, industry, diligence, exertion
$ curas > curo: to care for, take pains with, be solicitous for, look to, attend to, 
"""

# imports
import sys
import requests
import re
from bs4 import BeautifulSoup

# constants
URL_BASE = "http://www.perseus.tufts.edu/hopper/morph?la=la&l="

def lookup_word(word):
    # Takes string
    # Returns a BeautifulSoup object containing the html of the 
    # Perseus Word Study Tool entry for that word; or
    # if the word is not found, returns -1

    # Get html using Requests and Beautiful Soup
    url = URL_BASE + word
    response = requests.get(url)
    soup = BeautifulSoup(response.text)

    # Check to see if the Perseus Word Study Tool page is valid before returning
    if len(soup.findAll(text=re.compile("no information"))) == 0:
        return soup
    else:
        return -1

def get_definitions(soup):
    # Take BeautifulSoup object
    # Returns a list of tuples with the structure (lemma, lemma_definition)
    
    lemmas = soup.find_all('h4',attrs={'class':'la'})
    lemma_definitions = soup.find_all('span', attrs={'class':'lemma_definition'})

    lemma_list, lemma_definition_list = [], []
    
    for lemma in lemmas:
        lemma_list.append(lemma.text.strip())
            
    for lemma_definition in lemma_definitions:
        lemma_definition_list.append(lemma_definition.text.strip())
    
    definitions = zip(lemma_list,lemma_definition_list)
    
    return definitions
    
def main(query):
    soup = lookup_word(query)
    
    if soup == -1:
        print "No definition found for " + query + "."
    else:
        definitions = get_definitions(soup)
        for definition in definitions:
            print query + " > "+definition[0]+": "+definition[1]
        
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print "No argument given."
    else:
        for item in sys.argv[1:]:
            main(item)
            print "\n",