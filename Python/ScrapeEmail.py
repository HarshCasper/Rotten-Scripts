import requests
from bs4 import BeautifulSoup

#sampler="<a href=\"mailto:someone@example.com\">Send email</a>"

def main():
    print("Please paste the link for the website:- ")
    base_url=str(input())
    try:
        res=requests.get(base_url)
    except:
        print("An Error Ocurred. Please check your internet connection.\n\n")
    else:
        if(res.status_code!=404):
            soup=BeautifulSoup(res.text, "html.parser")
            for links in soup.find_all('a', href=True):
                email=(links['href'])
                if(str(email[:6])=="mailto"):
                    print(email[7:])
        else:
            print("Page Not Found.\n\n")

if (__name__=="__main__"):
    main()