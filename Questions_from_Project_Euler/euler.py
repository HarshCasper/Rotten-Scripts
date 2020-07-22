#!/usr/bin/env python3

#Imports and dependencies

import requests
from bs4 import BeautifulSoup
import re
import csv

def Euler():
  
  #The contents are written into a CSV file
  #Each question has a serial number, name of the problem and description of the problem

  with open('Project_Euler.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Problem Number", "Name" , "Description"])
    
    #There are 15 pages in all, the page number is appended to the URL
    start = 1
    pages = 15

    for page in range(start , pages + start):
      
      #Response is got from each page, the questions are then searched for 
      page_url = "https://projecteuler.net/archives;page="+ str(page)
      response = requests.get(page_url)
      soup = BeautifulSoup(response.text,"html.parser")
      
      #All the questions are located within the <table> tag
      #This information can be found out by using inspect element, Ctrl+Shift+I

      for link in soup.find('table' , attrs={"id" : "problems_table"}).find_all('a'):
        
        #The link to the question is located in a <a> tag
        question_url = "https://projecteuler.net/" + link['href']

        #The name and question number are obtained
        question_number = link['href'].split('=')[-1]
        question_name = link.string

        ques_response = requests.get(question_url)
        ques_contents = BeautifulSoup(ques_response.text, "html.parser")
        description = ''
        
        #In each question element, the description is mentioned in the <div> tag

        for content in ques_contents.find("div" , attrs={"class":"problem_content"}).children:  

          #The content between the tags are obtained getting rid of the tag elements

          content = re.sub(r'\<.*?>', r' ', str(content))
          description += content
        
        #Each entry is written into the file

        writer.writerow([question_number, question_name , description])

Euler() 
