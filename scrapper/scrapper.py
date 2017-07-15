#! /usr/bin/env python
import requests 
import time

from bs4 import BeautifulSoup
"""pull superpac info into page object"""
page = requests.get("https://www.opensecrets.org/pacs/superpacs.php")

print "contents of page object... fresh from the internets"
print page.content

"""parse the contents using BeautifulSoup, store in soup instance, parse using html)"""
soup = BeautifulSoup(page.content, 'html.parser')

print "**************"
print soup.content
help('BeautifulSoup')

time.sleep(1)
print (soup.prettify())
time.sleep(5)
print "soup children"
list(soup.children)

time.sleep(5)

print [type(item) for item in list(soup.children)]

