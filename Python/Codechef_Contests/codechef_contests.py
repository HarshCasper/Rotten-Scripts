import requests 
from bs4 import BeautifulSoup
from prettytable import PrettyTable

t = PrettyTable(['Code', 'Name', 'Start']) #to create table

#print (t)

url = 'https://www.codechef.com/contests'

page = requests.get(url)   #send request to cc srver and returns the page 

soup = BeautifulSoup(page.content,'html.parser') # store html content in soup

#print (soup.prettify()) #prettify() to print the html code in well intended form

table = soup.findAll('table', class_ = "dataTable")  #return the tables with class=dataTable

#print (len(table))

req_table = table[1]

tr = req_table.tbody.findAll('tr') #tr from all tbody tag

#print (len(tr))

#td = tr[0].findAll('td') #find all td from tr[0]

#print (len(td))
#print (td[0].text)

for i in range(len(tr)):
  td = tr[i].findAll('td')
  t.add_row([td[0].text, td[1].text, td[2].text]) #add_row takes a 'list' of data
  
print (t)
