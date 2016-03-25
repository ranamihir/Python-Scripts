# This is a script checks for new episodes of TV Shows and opens their download page in browser
import requests
import webbrowser
import os
from bs4 import BeautifulSoup
from datetime import datetime

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

for show in tv_shows:
    url = tv_shows[show]
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    for dates in soup.findAll('span', {'class': 'meta_date'}):
        if datetime.strptime(dates.text, '%B %d, %Y').date() == datetime.today().date():
            os.system('notify-send \"' + show + ' is here!\" --urgency=critical')
            episode_url = dates.find_previous("a")['href']
            episode_source_code = requests.get(episode_url)
            episode_plain_text = episode_source_code.text
            episode_soup = BeautifulSoup(episode_plain_text, "lxml")
            download_url = episode_soup.find("a", text="Mega")['href']
            webbrowser.open(download_url[download_url.index("https")::])