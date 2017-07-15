#! /usr/bin/env python
import requests 
import time

from bs4 import BeautifulSoup
"""pull superpac info into page object"""
page = requests.get("https://www.opensecrets.org/pacs/superpacs.php")

print ("Hello World!")
print ("contents of page object... fresh from the interwebs")
time.sleep(10)
print (page.content)

"""parse the contents using BeautifulSoup, store in soup instance, parse using html)"""
soup = BeautifulSoup(page.content, 'html.parser')

print ("**************")
print ("soup.prettify")
time.sleep(10)
print (soup.prettify())


print ("soup children")
time.sleep(10)
list(soup.children)
print ([type(item) for item in list(soup.children)])

