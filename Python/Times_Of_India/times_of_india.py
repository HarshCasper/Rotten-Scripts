import urllib
import datetime
from BeautifulSoup import BeautifulSoup

sock = urllib.urlopen("http://timesofindia.indiatimes.com/")
htmlSrc = sock.read()
soup = BeautifulSoup(htmlSrc)
print("The Times of India\n")
today = datetime.date.today()
print(today.strftime("The date %d, %b %Y"))
print("\t\t****Flash news****")
for div in soup.findAll("div", attrs={"id": "featuredstory"}):

    # for data in div.findNextSibling('div', attrs={'class':'data'}):
    for a in div.findAll("a"):
        print(a.text)
print("\n")
print("\t\t**** News in Bulletin ****")
print("\n")

for div in soup.findAll("div", attrs={"class": "top-story"}):
    for a in div.findAll("a"):
        print(a.text)


print("\n")
print("\t\t**** Entertainment ****\t")
print("\n")


for div in soup.findAll("div", attrs={"class": "entrmnt-wdgt-outer"}):
    # for data in div.findNextSibling('div', attrs={'class':'data'}):
    for a in div.findAll("a"):
        print(a.text)


print("\n")
print("\t\t**** Latest News ****\t")
print("\n")

for div in soup.findAll("div", attrs={"id": "lateststories"}):
    # for data in div.findNextSibling('div', attrs={'class':'data'}):
    for a in div.findAll("a"):
        print(a.text)
