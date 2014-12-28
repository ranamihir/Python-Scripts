from bs4 import BeautifulSoup
import re
import urllib

tFile = urllib.urlopen("https://www.torrentz.eu")
tHTML = tFile.read()
tFile.close()

soup = BeautifulSoup(tHTML)
print soup.prettify()
print (soup.get_text())

