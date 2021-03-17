# Tweet scraper using a particular hashtag without the intervention of twitter API

- Here, we make use of snscrape to scrape tweets associated with a particular hashtag. Snscrape is a python library that scrapes twitter without the use of API keys.

- In this script, we take the input of a hashtag and generate details associated with it (Eg., id, username, date, time, the tweet content, number of replies, likes, retweets, quotes and also its URL) tracing upto the desired number of tweets. 

- We store all this information in a .csv file with the selected file name.

## Setup Instructions

### Requirements

1. snscrape library:

```console
computer@computer:~$ pip install snscrape
```

2. csv module:
It comes built in with python

## Working

The inputs user has to give: 

![image](https://i.imgur.com/9aK1bhi.png)

```.csv``` file generated accordingly:

![image](https://i.imgur.com/Oxh5xmi.png)

## Author

[Rohini Rao](https://github.com/RohiniRG)
