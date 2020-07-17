#/usr/bin/env python3

#Imports
import requests
from bs4 import BeautifulSoup
import random

#The concept of webscraping is used here.
#From the URL mentioned below, jokes are scraped and stored.
#A random joke is retrieved

def get_jokes():
    
    jokes = []
    url = "https://www.boredpanda.com/funny-pun-jokes/?utm_source=google&utm_medium=organic&utm_campaign=organic"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")

    for i in (soup.find('div' , attrs={"class":"left-content-column" , "data-role":"swipe"}).find('div',attrs={"class" :"open-list-items clearfix"}).find_all('div',attrs={"class":"open-list-item open-list-block clearfix"})):
        jokes.append((i.find('p').find('span').string))
    return(random.choice(jokes))

if __name__ == "__main__":
    print(get_jokes())
