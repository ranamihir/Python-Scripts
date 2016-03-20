#This is a script checks for new episodes of TV Shows
import requests
import time
import webbrowser
from bs4 import BeautifulSoup
from datetime import datetime
import os

tv_shows = {
    "Arrow": 'http://awesomedl.ru/tag/arrow/',
    "Better Caul Saul": 'http://awesomedl.ru/?s=better+call+saul&x=0&y=0',
    "Castle": 'http://awesomedl.ru/tag/castle/',
    "Elementary": 'http://awesomedl.ru/tag/elemetary/',
    "House of Cards": 'http://awesomedl.ru/?s=house+of+cards&x=0&y=0',
    "Marvel's Agents of S.H.I.E.L.D": 'http://awesomedl.ru/?s=marvel%27s+agents+of+s.h.i.e.l.d.&x=0&y=0',
    "Marvel's Daredevil": 'http://awesomedl.ru/?s=marvel%27s+daredevil&x=0&y=0',
    "Sherlock": 'http://awesomedl.ru/tag/sherlock/',
    "Suits": 'http://awesomedl.ru/tag/suits/',
    "BBT": 'http://awesomedl.ru/tag/the-big-bang-theory/',
    "The Flash": 'http://awesomedl.ru/?s=the+flash&x=0&y=0'
}

target = open("TV Shows.txt", 'w')

for show in tv_shows:
    url = tv_shows[show]
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for dates in soup.findAll('span', {'class': 'meta_date'}):
        if datetime.strptime(dates.text, '%B %d, %Y').date() == datetime.today().date():
            target.write(show + " is here!\n")
target.close()
if os.stat("C:/Users/ranamihir/Desktop/TV Shows.txt").st_size:
    webbrowser.open("TV Shows.txt")
else:
    os.remove("C:/Users/ranamihir/Desktop/TV Shows.txt")