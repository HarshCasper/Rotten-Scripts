#!/usr/bin/env python3

from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP


def main(emotion):
    """
    The Main function, for parsing the emotion according to IMDB recommendation.
    |___________________________|
    |   Emotion     |   Genre   |
    |Sad            |Drama      |
    |Anger          |Family     |
    |Anticipation   |Thriller   |
    |Disgust        |Musical    |
    |Fear           |Sport      |
    |Joy            |Thriller   |
    |Sad            |Drama      |
    |Surprise       |Noir       |
    |Trust          |Western    |
    |---------------------------|
    :param emotion: Name of Emotion
    :return: Titles of Movies
    """

    if emotion == "Sad":
        linked_url = "http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc"

    elif emotion == "Disgust":
        linked_url = "http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc"

    elif emotion == "Anger":
        linked_url = "http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc"

    elif emotion == "Anticipation":
        linked_url = "http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc"

    elif emotion == "Fear":
        linked_url = "http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc"

    elif emotion == "Joy":
        linked_url = "http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc"

    elif emotion == "Trust":
        linked_url = "http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc"

    elif emotion == "Surprise":
        linked_url = "http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc"

    response = HTTP.get(linked_url)
    data = response.text
    soup = SOUP(data, "lxml")

    title = soup.find_all("a", attrs={"href": re.compile(r"\/title\/tt+\d*\/")})
    return title


# Driver Function
if __name__ == "__main__":

    print(
        "Select Your Emotion:"
        "\n 1. Anger"
        "\n 2. Anticipation"
        "\n 3. Disgust"
        "\n 4. Fear"
        "\n 5. Joy"
        "\n 6. Sad"
        "\n 7. Surprise"
        "\n 8. Trust"
    )
    emotion = input("Enter the emotion: ")
    a = main(emotion)
    count = 0

    if emotion == "Disgust" or emotion == "Anger" or emotion == "Surprise":

        for i in a:
            tmp = str(i).split(">;")
            if len(tmp) == 3:
                print(tmp[1][:-3])
            if count > 13:
                break
            count += 1
    else:
        for i in a:
            tmp = str(i).split(">")
            if len(tmp) == 3:
                print(tmp[1][:-3])
            if count > 11:
                break
            count += 1
