import tweepy


# Function to search for tweet
def search_tweet(s_user, s_tweet):
    # Enter the tweet you want to search for here
    for following in api.friends(id=s_user.screen_name):
        print("Searching ", following.screen_name)
        tweets = api.user_timeline(screen_name=following.screen_name)
        for tweet in tweets:
            if tweet.text.lower() == s_tweet.lower():
                link = "https://twitter.com/{}/status/{}"
                print("Found! Link", link.format(tweet.user.screen_name, tweet.id))
                print(" by: ", following.screen_name, "id: ", tweet.id)
                return
    print("Tweet not found!")


# Enter your keys here
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Enter tweet to be searched
get_tweet = ""


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

user = api.me()
search_tweet(user, get_tweet)
