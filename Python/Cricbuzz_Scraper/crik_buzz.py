''' Python script to get live cricket score
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

URL = 'http://www.cricbuzz.com/cricket-match/live-scores'
PAGE = urlopen(URL)
SOUP = BeautifulSoup(PAGE, 'html.parser')

UPDATE = []

for score in SOUP.find_all('div', attrs={'class': 'cb-col cb-col-100 cb-lv-main'}):
    s = score.text.strip()
    UPDATE.append(s)

for i in enumerate(UPDATE):
    print(i + 1, UPDATE[i])
