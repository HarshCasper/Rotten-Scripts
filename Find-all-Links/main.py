import re
import sys
import requests

from bs4 import BeautifulSoup

def help():
  print("Usage: python main.py <url>")

if len(sys.argv) < 2:
  help()
  exit(0)

url = sys.argv[1]

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

links = re.findall("http.?://[^\s\"\']+", str(soup))

if len(links) == 0:
  print("No links on {}".format(url))

for link in links:
  print(link)
