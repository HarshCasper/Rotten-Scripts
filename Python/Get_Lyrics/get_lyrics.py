import requests
import argparse
from bs4 import BeautifulSoup
from urllib.parse import urljoin

my_parser = argparse.ArgumentParser()
my_parser.add_argument(
    "--artist",
    action="store",
    type=str,
    required=True,
    help="Enter the name of the artist/ band",
)
my_parser.add_argument(
    "--song", action="store", type=str, required=True, help="Enter the name of the song"
)

args = my_parser.parse_args()
artist = args.artist
song = args.song


def get_lyrics(artist, song):
    artist = "".join(artist.lower().split())
    song = "".join(song.lower().split())
    base_url = "http://www.azlyrics.com/"
    song_url = "http://www.azlyrics.com/lyrics/" + artist + "/" + song + ".html"

    # Use requests library to get html from artist's page
    response = requests.get(song_url)

    # Make the html soup object
    soup = BeautifulSoup(response.content, "html.parser")
    lyrics = (
        soup.find("div", class_="col-xs-12 col-lg-8 text-center")
        .find_all("div")[5]
        .text
    )

    print(lyrics)


get_lyrics(artist, song)
