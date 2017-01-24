#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse
import urllib
import re
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Content check verification.')
parser.add_argument('-l','--link', help='Link to site', required=True)
parser.add_argument('-p','--phrase', help='Phrase to search', required=True)
args = vars(parser.parse_args())

def main():

   	html = urllib.urlopen(args['link']).read()
   	soup = BeautifulSoup(html, "lxml")

   	search = soup.body.findAll(text=re.compile(args['phrase']))
   	if search:
   		print ("OK: Phrase at site")
   		return 1

   	print ("Error: Phrase is not at site")
   	return 2

if __name__ == "__main__":
	main()

