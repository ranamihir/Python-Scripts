# This is a script checks for new episodes of TV Shows, opens their download page in browser and starts downloading them automatically
from bs4 import BeautifulSoup
from datetime import datetime
from rarfile import RarFile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import os
import glob

# List TV Shows
tv_shows = {
    "Arrow": 'http://awesomedl.ru/tag/arrow/',
    "Elementary": 'http://awesomedl.ru/tag/elementary/',
    "House of Cards": 'http://awesomedl.ru/?s=house+of+cards&x=0&y=0',
    "Marvel's Agents of S.H.I.E.L.D": 'http://awesomedl.ru/?s=marvel%27s+agents+of+s.h.i.e.l.d.&x=0&y=0',
    "Marvel's Daredevil": 'http://awesomedl.ru/?s=marvel%27s+daredevil&x=0&y=0',
    "Sherlock": 'http://awesomedl.ru/tag/sherlock/',
    "Suits": 'http://awesomedl.ru/tag/suits/',
    "Silicon Valley": 'http://awesomedl.ru/?s=silicon+valley&x=0&y=0',
    "BBT": 'http://awesomedl.ru/tag/the-big-bang-theory/',
    "The Flash": 'http://awesomedl.ru/?s=the+flash&x=0&y=0'
}

# Declare global variable browser
global browser

# Check for new episodes, download them if not downloaded already, and extract the RAR file. Move the video file to E: and delete the RAR file.
for show in tv_shows:
    print('Checking for ' + show + '...')
    url = tv_shows[show]
    try:
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html5lib")
        for dates in soup.findAll('span', {'class': 'meta_date'}):
            if datetime.strptime(dates.text, '%B %d, %Y').date() == datetime.today().date():
                print('\n' + show + ' is here!')
                episode_url = dates.find_previous('a')['href']
                episode_source_code = requests.get(episode_url)
                episode_plain_text = episode_source_code.text
                episode_soup = BeautifulSoup(episode_plain_text, "html5lib")
                download_url = episode_soup.find('a', text='Mega')['href']
                try:
                    browser.get(download_url[download_url.index('https')::])
                except:
                    browser = webdriver.Chrome('C:/Python34/chromedriver.exe')
                    browser.get(download_url[download_url.index('https')::])
                finally:
                    filename = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'filename'))).get_attribute('title')
                    if not glob.glob('E:/' + filename.replace('.rar', '') + '*'):
                        download_button = browser.find_element_by_class_name('throught-browser')
                        download_button.click()
                        print('Downloading ' + filename + '...')
                        while 1:
                            download_percent = browser.find_element_by_class_name('percents-txt').text
                            print('\r' + download_percent + ' completed.', end='')
                            if download_percent == '100 %':
                                time.sleep(30)
                                with RarFile('C:/Users/ranamihir/Downloads/' + filename) as rf:
                                    for f in rf.infolist():
                                        if not f.filename.endswith('.txt'):
                                            with open('E:/' + f.filename, 'wb') as of:
                                                of.write(rf.read(f))
                                            break
                                os.remove('C:/Users/ranamihir/Downloads/' + filename)
                                break
                        print()
    except Exception as e:
        print('\nError :' + str(e))
        pass

# Safely quit browser
try:
    browser.quit()
except:
    pass