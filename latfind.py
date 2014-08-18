#! /usr/bin/env python

"""
Script to look up Latin word using Perseus and return a list of available short definitions. Written by @diyclassics 8.15.14.
"""

import sys
import requests
from bs4 import BeautifulSoup

def get_short_def(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)

    spans = soup.find_all('span', attrs={'class':'lemma_definition'})
    
    if len(spans) == 0:
        print "No results."
    else:    
        for span in spans:
            print "- ", span.text.strip()
    
def main(query):
    URL = "http://www.perseus.tufts.edu/hopper/morph?la=la&l=" + query
    get_short_def(URL)
    
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print "No argument given."
    else:
        for item in sys.argv[1:]:
            print item
            main(item)
            print '\n',