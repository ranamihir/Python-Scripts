# This is a script that scrapes all the data from espncricinfo.com, based on user's input of class (Tests, ODI's, T20's,
# etc.) and type (Batting, Bowling, Fielding, etc.), and dumps all the data into a CSV file.
import requests
from bs4 import BeautifulSoup

classes = {
    'tests': 1,
    'odis': 2,
    't20s': 3,
    'all': 11,
    'womens tests': 8,
    'womens odis': 9,
    'womens t20s': 10,
    'youth tests': 20,
    'youth odis': 21
}

def maximum_pages(url):
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for row in soup.findAll('tr', {'class': 'data2'}):
            for cell in row.findAll('td'):
                text = cell.text
                if 'Page' in text:
                    return int(text.split()[-1])

def spider(class_type, type):
    url = 'http://stats.espncricinfo.com/ci/engine/stats/index.html?template=results;type=' + type + ';class=' + str(classes[class_type])
    max_pages = 1
    max = maximum_pages(url)
    if max:
        max_pages = max
    page = 1
    f = open(class_type + '_' + type + '.csv', 'w+')
    while page <= max_pages:
        print('\rDownloading page ' + str(page) + ' of ' + str(max_pages) + '...', end='')
        url += ';page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for row in soup.findAll('tr', {'class': 'data1'}):
            for cell in row.findAll('td'):
                if row.td['class'] != 'padDD':
                    try:
                        f.write(cell.text + ',')
                    except:
                        pass
            f.write('\n')
        page+=1
    f.close()

class_type = input('Enter class:\n').lower().replace('\'', '')
type = input('Enter type:\n').lower()

spider(class_type, type)
