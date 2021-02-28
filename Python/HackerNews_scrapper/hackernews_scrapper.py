import requests
from bs4 import BeautifulSoup as bs

# Base url for the latest articles on the hackernews website
HACKERNEWS_URL = "https://news.ycombinator.com/newest"

# Number of articles requested by the user
number_of_articles = int(input(
    "Enter the number of articles you want from the hackernews website(1-30): "))
print()

# Response obect to fetch the hackernews url
response = requests.get(HACKERNEWS_URL)

# soup object for easy scrapping
soup = bs(response.content, 'html.parser')

# Finding all the a tags with the class storylink
latest_thirty = soup.find_all('a', attrs={'class': 'storylink'})

# list to track the links of the articles
links = []

# list to keep track of the names of the articles
names = []

# Fetching the links and names from the soup object and storing them in respective lists
for article in latest_thirty:
    links.append(article['href'])
    names.append(article.text)

# Modyfing the links and names as per the user request
user_requested_links = links[:number_of_articles]
user_requested_names = names[:number_of_articles]

# Dictionary to keep names and links together
result_articles = dict(zip(user_requested_links, user_requested_names))

# Clean display of the articles
print("Your requested articles are: \n")

for key, value in result_articles.items():
    print(f"{value}=> {key}\n")
