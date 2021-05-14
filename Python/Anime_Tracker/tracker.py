try:
    import requests
    from bs4 import BeautifulSoup
    import urllib.parse as parse
    import re
except ImportError:
    print('Some modules are not installed! ')
    
def details(soup):
    """
     BS4 Library is being used to extract HTML from the Webpages
      In this  function we will basically select some HTML elements using parsed HTML (soup).
    """
    info = soup.find('div', {'class': 'pure-1 md-3-5'})  
    # now extracting the text for p tag of the div 
    print("\nAbout the Anime : \n", "\t\t", info.find('p').getText(), "\n")                              
    total_episodes = soup.find('div', {'class': 'pure-1 md-1-5'})
     # using regex for only selecting numbers
    print("\nTotal number of episodes :\t",re.sub("[^0-9]", "", total_episodes.find('span').getText()))     
    Active_years = soup.find('span', {'class': 'iconYear'})
    print("\n Years Active (From-To)\t:\t",
          Active_years.getText(), "-\n")
    rating = soup.find('div', {'class': 'avgRating'})
    print("Rating : ", rating.find('span').getText())
    tags = soup.find('div', {'class': 'tags'})
    list = []
    for _ in range(4):
        list.append(tags.find('ul').getText())
    print("\nTags : \n")
    print((list[0].replace("\n", "  ")))   
def entry():
    """
    In this function we will take input .
    And parse HTML using Beautifulsoup
    """
    print("\nType complete name>>\n")
    anime_name = input("[+] Enter the name of the Anime : ").strip().title().replace(" ", "-")
    print("\n")
    print(anime_name)
    search_url = ("https://www.anime-planet.com/anime/" + anime_name)
    source_code = requests.get(search_url)
    content = source_code.content
    global soup
    # to parse the selected HTML
    soup = BeautifulSoup(content, features="html.parser")    
    try:
        details(soup)
    except AttributeError:
        print("Anime info not found")
if __name__ == "__main__":
    entry()
