import requests, time
from bs4 import BeautifulSoup

baseurl = "https://en.wikipedia.org/wiki/"
clublist=[]
name=[]
res=0

def getname():
    print("Please enter the footballer's commonly known name:-")
    print("(E.G. cristiano ronaldo, wayne rooney, david de gea, lionel messi, etc.)")
    print("Do not worry about uppercase / lowercase\n")
    inp=str(input(""))
    print("")
    names = inp.split(sep=" ")
    return list(names)

def getclubcareer(headlines):
    clubs=[]
    text=0
    for idx, item in enumerate(headlines):
        text=item.getText()
        if(text=="Club career"):
            for item2 in headlines[idx+1:]:
                if item2.getText()!="International career":
                    clubs.append(item2.getText())
                else:
                    break
            break
    return clubs


def prettify_list(clublist):
    pretty_list=[]
    for item in clublist:
        if len(str(item))>=5:
            if ((item[:4].isnumeric())): #and (item[4]=="–" or item[4]=="-" or item[4]=="/")):
                item="  Notable: " + str(item)
                pretty_list.append(item)
            else:
                pretty_list.append(item)
        else:
            pretty_list.append(item)
    return pretty_list

def generate_url(names):
    superstring=""
    for individual in names:
        superstring+= (str(individual) + "_")
    superstring=superstring[:(len(superstring)-1)]
    superurl=baseurl + superstring
    #print(superurl)
    return str(superurl)

def main():
    print("WELCOME TO FOOTBALLER CLUB WIKI!")
    print("Get information about a footballer's Club History, according to Wikipedia.")
    print("")
    while(True):
        name=getname()
        for idx in range(len(name)):
            name[idx] = str((name[idx].lower()).capitalize())
            if not (name[idx][0].isalpha()):
                name[idx]=name[idx][0] + name[idx][1:].lower().capitalize()
            if not (name[idx][len(name[idx])-1].isalpha()):
                name[idx]=name[idx][0].lower() + name[idx][1:]
        url = generate_url(name)
        try:
            res=requests.get(url)
        except:
            print("An Error Occurred. Please check your internet connection.")
            print("\n\n")
        else:
            if(res.status_code!=404):
                soup=BeautifulSoup(res.text, "html.parser")
                headlines=soup.select(".mw-headline")
                clublist = getclubcareer(headlines)
                clublist = prettify_list(clublist)
                if(len(clublist)):
                    print("CLUB CAREER:-\n")
                    for clubname in clublist:
                        print(clubname)
                else:
                    print("No club history available")
            else:
                print("Page not found. Player spelling may be incorrect.")
            print("\n\n")


if __name__ == "__main__":
    main()

    
