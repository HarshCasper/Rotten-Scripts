

def imgflip():

    from bs4 import BeautifulSoup
    import requests
    e = 1
    tenpages = []
    for i in range(10):
        url = "https://imgflip.com/tag/memes?page=" + str(e)
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"html.parser")
        for d in (soup.find('div', attrs={"id":"page" , "class":"base clearfix"}).find('div', attrs={"id":"base-left"}).find_all("div" , attrs={"class":"base-unit clearfix"})):
            p = (d.find("div" , attrs = {"class":"base-img-wrap-wrap"}).find('img'))
            try:
                tenpages.append("https:" + str(p['src']))
            except:
                pass
        e += 1
    return(tenpages)

tenpages = imgflip()
print(tenpages)
