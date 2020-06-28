import re
import requests

from bs4 import BeautifulSoup

url = "https://github.com/HarshCasper/Rotten-Scripts/issues/19"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

links = re.findall("http.?://[^\s\"\']+", str(soup))

for link in links:
  print(link)
