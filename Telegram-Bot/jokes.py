#/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

url = "https://www.boredpanda.com/funny-pun-jokes/?utm_source=google&utm_medium=organic&utm_campaign=organic"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

for i in (soup.find('div' , attrs={"class":"left-content-column" , "data-role":"swipe"}).find('div',attrs={"class" :"open-list-items clearfix"}).find_all('div',attrs={"class":"open-list-item open-list-block clearfix"})):
  print(i.find('p').find('span').string)
