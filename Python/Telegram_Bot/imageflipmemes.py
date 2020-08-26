import random
from bs4 import BeautifulSoup
import requests

#The imageflip website is used to scrape the urls of memes.
#A random url is returned

def memes():
    page_no = 1
    tenpages = []
    for i in range(10):
        url = "https://imgflip.com/tag/memes?page=" + str(page_no)
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"html.parser")
        for d in (soup.find('div', attrs={"id":"page" , "class":"base clearfix"}).find('div', attrs={"id":"base-left"}).find_all("div" , attrs={"class":"base-unit clearfix"})):
            p = (d.find("div" , attrs = {"class":"base-img-wrap-wrap"}).find('img'))
            try:
                tenpages.append("https:" + str(p['src']))
            except:
                pass
        page_no += 1
    return(random.choice(tenpages))

if __name__ == "__main__":
    print(memes())
