from bs4 import BeautifulSoup
import re
import urllib

gFile = urllib.urlopen("https://www.google.com")
gHTML = gFile.read()
gFile.close()

soup = BeautifulSoup(gHTML)
for tag in soup.find_all(re.compile("^b")):
    print (tag.name)
