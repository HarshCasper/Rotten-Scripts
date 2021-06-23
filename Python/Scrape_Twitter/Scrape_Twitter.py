import tweepy
import pymongo
from pymongo import MongoClient

client = MongoClient()


# Enter Tweepy credentials
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


# Edit according to needs, here is localhost
client = MongoClient("localhost", 27017)
db = client["scrapped_tweets"]
tweets = db.tweets


# Change to the number of tweets required
MAX_TWEETS = 5000

# Change q to get relevant tag
for tweet in tweepy.Cursor(api.search, q="#blacklivesmatter", rpp=100).items(
    MAX_TWEETS
):
    print(tweet)
    result = tweets.insert_one(tweet._json)
print("Scrapped!")
