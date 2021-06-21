import os
import requests
from dotenv import load_dotenv

load_dotenv()


def news_from_bbc():
    # BBC news api
    main_url = os.getenv("BBC_API")
    open_bbc_page = requests.get(main_url).json()
    articles = open_bbc_page["articles"]
    headlines = []
    links = []

    for article in articles:
        headlines.append(article["title"])
        links.append(article["url"])

    for i in range(len(headlines)):
        print(i + 1, headlines[i])
        print("Link to the full article : " + links[i] + "\n")


if __name__ == "__main__":
    news_from_bbc()
