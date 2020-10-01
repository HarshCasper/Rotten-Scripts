"""IMDB top 250 movies.
"""
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'http://www.imdb.com/chart/top'
RESPONSE = requests.get(URL)
SOUP = BeautifulSoup(RESPONSE.text, features="lxml")
MOVIES = SOUP.select('td.titleColumn')
STARS = [a.attrs.get('title') for a in SOUP.select('td.titleColumn a')]
RATINGS = []
for b in SOUP.select('td.posterColumn span[name=ir]'):
    RATINGS.append(round(float(b.attrs.get('data-value')), 1))

IMDB = []
# Store each item into dictionary (data), then put those into a list (imdb)
for index in range(0,(MOVIES)):
    movie_string = MOVIES[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index)) + 1:-7]
    year = re.search(r'\((.*?)\)', movie_string).group(1)
    data = {"movie_title": movie_title, "year": year,
            "star_cast": STARS[index], "rating": RATINGS[index]}
    IMDB.append(data)

# CREATING A DATAFRAME
DF = pd.DataFrame(IMDB)
DF.index = DF.index.rename('S.No')
# copy data frame in to CSV file
DF.to_csv('imdb.csv')
print("csv file has been created in current working directory")
