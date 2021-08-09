import tweepy
import ssl
from dotenv import load_dotenv
from pathlib import Path
import os
import time
import logging
from random import shuffle

env_path = Path(".", ".env")
load_dotenv(dotenv_path=env_path)

ssl._create_default_https_context = ssl._create_unverified_context

# Oauth keys
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def main():
    tweet_url = input("Enter the Giveway Tweet URL:- ")
    num = int(input("How many winners you want? "))
    tweet_id = int(tweet_url.split("/")[-1])
    tweet_user = tweet_url.split("/")[-3]

    user_for_selection = []
    replies = tweepy.Cursor(api.search, q="to:" + tweet_user, since_id=tweet_id, tweet_mode="extended").items()

    while True:
        try:
            reply = replies.next()
            if not hasattr(reply, "in_reply_to_status_id_str"):
                continue
            if reply.in_reply_to_status_id == tweet_id:
                user_for_selection.append(reply.user.screen_name)

        except tweepy.RateLimitError as e:
            logging.error("Twitter api rate limit reached {}".format(e))
            time.sleep(60 * 15)
            continue
        except tweepy.TweepError as e:
            logging.error("Tweepy error occured:{}".format(e))
            break
        except StopIteration:
            break
        except Exception as e:
            logging.error("Failed while fetching replies {}".format(e))
            break

    retweets = tweepy.Cursor(api.retweeters, id=tweet_id).items()

    while True:
        try:
            user_id = retweets.next()
            user = api.get_user(user_id)
            user_for_selection.append(user.screen_name)

        except tweepy.RateLimitError as e:
            logging.error("Twitter api rate limit reached {}".format(e))
            time.sleep(60 * 15)
            continue
        except tweepy.TweepError as e:
            logging.error("Tweepy error occured:{}".format(e))
            break
        except StopIteration:
            break
        except Exception as e:
            logging.error("Failed while fetching retweets {}".format(e))
            break

    all_users = list(user_for_selection)
    shuffle(all_users)
    winners = all_users[:num]
    print("------------Winners-----------")
    for i in winners:
        print("@%s" % i)


if __name__ == "__main__":
    main()
