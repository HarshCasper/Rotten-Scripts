import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

t = PrettyTable(["Name", "Start","Link"])  # to create table

url = "https://www.codechef.com/"

page = requests.get(url).text  # send request to cc srver and returns the page

soup = BeautifulSoup(page, "lxml")  # store html content in soup

table = soup.findAll('div',class_='l-card-3 m-other-event-card')

for i in table:
    nm = i.h3.text
    dt = i.find('p',class_= 'm-card-3__day').text + i.find('p',class_= 'm-card-3__month').text + i.find('span',class_='m-card-3__time-clock').text
    lnk =i.find('a',class_='m-card-3__dtl-btn')['href']
    t.add_row([nm,dt,lnk])

print(t)
