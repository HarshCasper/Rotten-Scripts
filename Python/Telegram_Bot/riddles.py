# Imports
import requests
from bs4 import BeautifulSoup
import random

# The concept of webscraping is used here.
# From the URL mentioned below, riddles are scraped and stored.
# A random riddles is retrieved


def get_riddles():
    url = "https://www.skiptomylou.org/kids-jokes/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    riddles = []

    for i in (
        soup.find("main", attrs={"class": "content"})
        .find("div", attrs={"class": "entry-content"})
        .find_all("p")
    ):
        if i is not None:
            riddles.append(
                str(i.text)
                .replace("A", "\b")
                .replace("Q", "")
                .strip(":")
                .replace("\xa0", "")
                .replace(":", "")
                .replace("\x08", "")
            )

    actualridd = []
    for i in riddles[5:-7]:

        p = i.strip().strip(".").split("? ")
        try:
            actualridd.append(p[0] + "?" + p[1])
        except:
            actualridd.append(p[0])
    return random.choice(actualridd)


if __name__ == "__main__":
    print(get_riddles())
