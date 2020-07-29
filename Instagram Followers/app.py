from bs4 import BeautifulSoup 
import requests 
  
# instagram URL 
URL = "https://www.instagram.com/{}/"
  
# parse function 
def parse_data(s): 
    data = {} 
    s = s.split("-")[0]  
    s = s.split(" ") 
    # assigning the values 
    data['Followers'] = s[0] 
    data['Following'] = s[2] 
    data['Posts'] = s[4] 
    return data 
  
# scrape function 
def scrape_data(username): 
    r = requests.get(URL.format(username)) 
    # converting the text 
    s = BeautifulSoup(r.text, "html.parser")  
    # finding meta info 
    meta = s.find("meta", property ="og:description")  
    # calling parse method 
    return parse_data(meta.attrs['content']) 
  
# main function 
if __name__=="__main__":     
    # user name 
    username = "kagrawal61" 
    # calling scrape function 
    data = scrape_data(username) 
    print(data) 