import tweepy
import time

# Authenticate to Twitter
CONSUMER_KEY = "<your-consumer-or-API-key-goes-here>"
CONSUMER_SECRET = "<your-consumer-or-API-secret-goes-here>"
ACCESS_KEY = "<your-access-key-goes-here>"
ACESS_SECRET = "<your-access-secret-goes-here>"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACESS_SECRET)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
search = "#python3"
numTweet = 500
for tweet in tweepy.Cursor(api.search, search).items(numTweet):
    try:
        print("Tweet Liked")
        tweet.favorite()
        print("Retweet done")
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
