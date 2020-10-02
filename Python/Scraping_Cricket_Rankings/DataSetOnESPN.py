from bs4 import BeautifulSoup
from urllib.request import urlopen

pg=urlopen('https://www.espncricinfo.com/rankings/content/page/211271.html')
soup=BeautifulSoup(pg,'html.parser')

body=soup.find('div',{'class':'ciPhotoContainer'})
head=soup.findAll('h3')

name=[]
for i in head:
    j=i.text
    name.append(j)
#print(name)

import pandas as pd
columns=['pos','team','matches','points','rating']
df=pd.DataFrame(columns=columns)
print(df)

tr_list=soup.findAll('tr')

n=0
for i in tr_list:
    row=[]
    td_list=i.findAll('td')
    for j in td_list:
        a=j.text
        row.append(a)
        dic={}
    try:
        for k in range(len(df.columns)):
            dic[df.columns[k]] = row[k]
        df = df.append(dic, ignore_index=True)
    except:
        df=pd.DataFrame(columns= columns)
        table_name=name[n]
        n=n+1
    df.to_csv('C:\\Users\\hp\\Desktop\\Cricinfo'+table_name+'.csv', index = False)


print("Done")