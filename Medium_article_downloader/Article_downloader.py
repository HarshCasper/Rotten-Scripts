#!/usr/bin/env python3

#Imports and dependencies

import requests
from bs4 import BeautifulSoup

#The content is written into a text file

file = open("Medium_article_content.txt", "w")

#The URL of the article is entered here
page_url = input("Enter the URL of the Medium Article ")

#Based on the response got from the URL, the content is loaded into response

response = requests.get(page_url)

#Beautiful soup is a library used for web scraping and parsing the contents of a web page
#Here a html parser is used to parse through the content embedded in the html tags

soup = BeautifulSoup(response.text,"html.parser")

#The content of the article is stored in the <article> tag

for line in soup.find('article').find('div'):
  
  #All the content is essentially stored between <p> tags
  
  for content in line.find_all('p'):

    #contents are written into a file
    
    file.write(content.text + '\n')

file.close()
