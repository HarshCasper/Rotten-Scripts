import requests
from bs4 import BeautifulSoup

url = "https://www.skiptomylou.org/kids-jokes/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

riddles = []

for i in (soup.find('main' , attrs={"class":"content"}).find('div' , attrs={"class":"entry-content"}).find_all('p')):
  if i != None:
    riddles.append(str(i.text).replace('A' , '\b').replace('Q' ,'').strip(':').replace('\xa0' , '').replace(':' , ''))
    

actualridd = []
for i in (riddles[5:-7]):
    
    p = (i.strip().strip('.').split('? '))
    try:
        actualridd.append(p[0] + '?'  +'\n' + p[1])
    except:
        actualridd.append(p[0])

for i in actualridd:
    print(i)
