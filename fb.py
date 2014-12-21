from bs4 import BeautifulSoup
import urllib2
fbfile = urllib2.urlopen("https://www.facebook.com")
fbHTML = fbfile.read()
fbfile.close()
 
soup = BeautifulSoup(fbHTML)
fbAll = soup.find_all("a")
for links in fbAll:
	print (links.get('href'))