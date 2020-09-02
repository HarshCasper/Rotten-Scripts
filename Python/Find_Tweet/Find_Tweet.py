import tweepy


#Function to search for tweet
def search_tweet(user,s_tweet):
    # Enter the tweet you want to search for here
    for following in api.friends(id=user.screen_name):
        tweets = api.user_timeline(screen_name=following.screen_name)
        for tweet in tweets:
            if tweet.text.lower() == s_tweet.lower():
                link="https://twitter.com/{}/status/{}"
                print('Found! Link', link.format(tweet.user.screen_name,tweet.id), ' by: ',following.screen_name, 'id: ',tweet.id)
                return
    print('Tweet not found!')


# Enter your keys here
consumer_key = "wgqHpBVO6MBnw8DaRhS61dSOP"
consumer_secret = "xiTc6iR5CvHnefNqSQbcUOkyE4c9tTYUZTCC6rN1NTFhYePoo8"
access_token = "1214908048969363456-AmFJs13jaZxVtamuc8QeSMDWigO1vj"
access_token_secret = "Jmmlzg9534VIFYg54IKrPtqjYaZLQdXPM6LTt3zVQFcBY"

#Enter tweet to be searched
s_tweet = "This could be heaven if we made it such."


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

user = api.me()
search_tweet(user,s_tweet)

