from os.path import isfile
from json import load
import tweepy
import sys

class DeleteBot:
    """
        Base class which contains methods common to all sub-classes such as connecting to the
        twitter api, fetching tweets and deleting tweets.
    """
    def __init__(self, filename=None):
        """
            Initialize a new DeleteBot Object\n
            KEYWORD ARGUMENTS:\n
            filename -- Name of the file which has stored the credentials in the json format
        """
        try:
            # Validation
            if not isinstance(filename, str):
                raise Exception("Error: Invalid Filename passed")

            if not isfile(filename):
                raise Exception("Error: File '{}' does not exist".format(filename))
    
            self.filename = filename
            self.api = None

            self.connect()

        except Exception as e:
            print(str(e))
            sys.exit(0)

    def connect(self):
        """
        Function to connect to the Twitter API using OAuth based on the credentials given in the 'credentials.json' file.
            # Credentials.json should contain the following keys:
            ## consumer_key
            ## consumer_key_secret
            ## access_token
            ## access_token_secret
        """
        credentials = None
        try:
            # Read the credentials.json file into a python dictionary
            with open(self.filename, "r") as f:
                credentials = load(f)

            auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_key_secret'])
            auth.set_access_token(credentials['access_token'], credentials['access_token_secret'])
            self.api = tweepy.API(auth)
            
        except Exception as e:
            print(str(e))
            sys.exit(0)
        
        print("Status: Connection Established Successfully!")

    def get_tweets(self, user_id=None, count=20):
        """
            Returns the tweets of a specific user authenticated in the 'api' object
            \n Keyword Arguments:\n
            user id -- Defines the user id for which the tweets are to be fetched. 
                       None by default, which will result in the tweets of the account which is authorized\n
            count -- Defines the count of the tweets to be fetched. Default value is 20. 
        """        
        try:
            if not isinstance(count, int):
                raise Exception("Error: Invalid value passed to the argument 'count'")

            if count < 0:
                raise Exception("Error: 'count' value must be greater than 0.")
            
            # Return all the tweets of the user
            if user_id is None:
                return self.api.user_timeline(count=count)

            return self.api.user_timeline(id=user_id, count=count)
        
        except Exception as e:
            print(str(e))
            sys.exit(0)

    def delete_tweet(self, id=None):
        """
            Deletes the tweet status object corresponding to the passed argument 'id'
            \nKeyword Arguments:\n
            id -- ID of the tweet to be deleted
        """
        try:
            # Destroy the status object with the id equal to the passed id
            self.api.destroy_status(id=str(id))

        except Exception as e:
            print(str(e))
            sys.exit(0)
    
    def delete_all(self, tweets=None):
        """
            Deletes all the tweets passed in the argument 'tweets'
        """
        if tweets is None:
            raise Exception("Error: Invalid 'tweets' object passed")
        count = len(tweets)
        if count == 0:
            print("Status: No tweets to delete!!")
            sys.exit(0)
        
        confirmation = input("\n{} tweets will be deleted. Press (y/n) to confirm: ").lower()
        if confirmation == 'n':
            sys.exit(0)
        elif confirmation == 'y':
            for id in tweets.keys():
                self.delete_tweet(id)
                print("Status: Tweet with ID: {} deleted!".format(id))

        print("Status: {} tweets deleted successfully!".format(count))

class DeleteMinRetweet(DeleteBot):


    def __init__(self, filename=None, min_retweet=-1, max_retweet=sys.maxsize):
        """
            Class to delete the tweets based on the minimum and maximum number of retweets\n
            Keyword Arguments: \n
            min_retweet: Minimum threshold for retweets, below which the tweets will be deleted
            max_retweet: Maximum threshold for retweets, above which the tweets will be deleted
        """
        super().__init__(filename=filename)
        try:
            if not isinstance(min_retweet, int):
                raise Exception("Error: Invalid value passed to argument 'min_retweet'")
            
            if min_retweet < 0:
                raise Exception("Error: Value of 'min_retweet' argument must be greater than 0")

            if not isinstance(max_retweet, int):
                raise Exception("Error: Invalid value passed to argument 'max_retweet'")
            
            if max_retweet < 0:
                raise Exception("Error: Value of 'max_retweet' argument must be greater than 0")
        except Exception as e:
            print(str(e))
            sys.exit(0)

        self.min_retweet = min_retweet
        self.max_retweet = max_retweet
        print("Status: Parameters set successfully")
        print("Min Retweet Count: {}".format(min_retweet if min_retweet > 0 else "-"))
        print("Max Retweet Count: {}".format(max_retweet if max_retweet < sys.maxsize else "-"))

    def filter(self, user_id=None, count=20, tweet_timeline=None):
        """
            Filters the tweets based on minimum and maximum no of retweets.\n
            Keyword arguments:\n
            user id -- User for which the tweets are to be filtered\n
            count -- Specifies the number of tweets to be considered. 20 by default.
            tweet_timeline -- If not provided, the super() class method to fetch tweets will be called.
        """
        try:
            timeline = None
            if tweet_timeline is not None:
                timeline = tweet_timeline
            else:
                timeline = self.get_tweets(user_id=user_id, count=count)

            if timeline is None:
                raise Exception("Error: Could not fetch the tweets")

            filtered_tweets = {}
            for tweets in timeline:
                tweet = tweets._json
                if tweet["retweet_count"] > self.min_retweet and tweet["retweet_count"] < self.max_retweet:
                    temp_tweet = {"text": tweet["text"], "retweet_count": tweet["retweet_count"]}
                    filtered_tweets[tweet["id"]] = temp_tweet

            print("Status: Filtered {} tweets with the given criteria".format(len(filtered_tweets)))
            return filtered_tweets

        except Exception as e:
            print(str(e))
            sys.exit(0)


class DeleteMinFavorite(DeleteBot):


    def __init__(self, filename=None, min_favorite=-1, max_favorite=sys.maxsize):
        """
            Class to delete the tweets based on the minimum and maximum number of likes\n
            Keyword Arguments: \n
            min_favorite: Minimum threshold for likes, above which the tweets will be deleted
            max_favorite: Maximum threshold for likes, below which the tweets will be deleted
        """
        super().__init__(filename=filename)
        try:
            if not isinstance(min_favorite, int):
                raise Exception("Error: Invalid value passed to argument 'min_favorite'")
            
            if min_favorite < 0:
                raise Exception("Error: Value of 'min_favorite' argument must be greater than 0")

            if not isinstance(max_favorite, int):
                raise Exception("Error: Invalid value passed to argument 'max_favorite'")
            
            if max_favorite < 0:
                raise Exception("Error: Value of 'max_favorite' argument must be greater than 0")
        except Exception as e:
            print(str(e))
            sys.exit(0)

        self.min_favorite = min_favorite
        self.max_favorite = max_favorite
        print("Status: Parameters set successfully")
        print("Min Likes Count: {}".format(min_favorite if min_favorite >= 0 else "-"))
        print("Max Likes Count: {}".format(max_favorite if max_favorite < sys.maxsize else "-"))

    def filter(self, user_id=None, count=20, tweet_timeline=None):
        """
            Filters the tweets based on minimum and maximum no of likes.\n
            Keyword arguments:\n
            user id -- User for which the tweets are to be filtered\n
            count -- Specifies the number of tweets to be considered. 20 by default.
            tweet_timeline -- If not provided, the super() class method to fetch tweets will be called.
        """
        try:
            timeline = None
            if tweet_timeline is not None:
                timeline = tweet_timeline
            else:
                timeline = self.get_tweets(user_id=user_id, count=count)

            if timeline is None:
                raise Exception("Error: Could not fetch the tweets")

            filtered_tweets = {}
            for tweets in timeline:
                tweet = tweets._json

                if tweet["favorite_count"] > self.min_favorite and \
                    tweet["favorite_count"] < self.max_favorite:
                    
                    temp_tweet = {"text": tweet["text"], "favorite_count": tweet["favorite_count"]}
                    filtered_tweets[tweet["id"]] = temp_tweet

            print("Status: Filtered {} tweets with the given criteria".format(len(filtered_tweets)))
            return filtered_tweets

        except Exception as e:
            print(str(e))
            sys.exit(0)