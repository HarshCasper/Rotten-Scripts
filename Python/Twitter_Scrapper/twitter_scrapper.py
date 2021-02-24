"""
This script extracts all Tweets, Retweets, Images, Videos, Hashtags,
Likes and Pinned tweet of a specific user in a .csv file.
"""

import csv
import random
import time
from itertools import zip_longest

import tweepy
from bs4 import BeautifulSoup
from decouple import config
from selenium import webdriver

# Authenticate to Twitter
CONSUMER_KEY = config("CONSUMER_KEY")
CONSUMER_SECRET = config("CONSUMER_SECRET")
ACCESS_KEY = config("ACCESS_KEY")
ACESS_SECRET = config("ACESS_SECRET")

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACESS_SECRET)
api = tweepy.API(auth)

URL = "https://twitter.com"
PATH_CHROME_DRIVER = config("PATH_CHROME_DRIVER")
random_time_2_to_5 = random.randint(2, 5)
random_time_5_to_10 = random.randint(5, 10)


def login(driver, username, password):
    """
    Function to log in to Twitter with Selenium
    """
    try:
        # Phone, email or user
        driver.find_element_by_name(
            "session[username_or_email]").send_keys(username)
        # Password
        driver.find_element_by_name("session[password]").send_keys(password)
        # Login Button
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div'
        ).click()

        time.sleep(random_time_2_to_5)
        print("Login Successful...!")

    except Exception as error:
        print("login function failed.")
        print("Error details: " + error)


def extract_pinned_tweet(driver, user_to_scrape):
    """
    Function to save pinned tweet
    """
    try:
        pinned_tweet = []

        print("Extracting pinned tweet...!")

        driver.get(URL + "/" + user_to_scrape)
        time.sleep(random_time_5_to_10)

        # Select the user's first Tweet
        driver.find_elements_by_css_selector(
            '[data-testid="tweet"]')[0].click()
        time.sleep(random_time_5_to_10)

        soup = BeautifulSoup(driver.page_source, "lxml")

        # Find pinned tweet image
        pinned = soup.find_all(
            "svg",
            attrs={
                "class": "r-m0bqgq r-4qtqp9 r-yyyyoo r-1xvli5t "
                + "r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-meisx5"
            },
        )

        # If exists
        if len(pinned) > 0:
            print("Pinned Tweet: True")
            pinned_tweet.append(driver.current_url)
        else:
            print("Pinned Tweet: False")

        return pinned_tweet

    except Exception as error:
        print("extract_pinned_tweet function failed.")
        print("Error details: " + error)


def extract_tweets(user_to_scrape):
    """
    Function to extract the Tweets of a user
    """
    try:
        print("Extracting Tweets, Retweets, Media and Hashtags, please wait...!")

        tweets = None

        try:
            tweets = api.user_timeline(
                screen_name=user_to_scrape,
                # 200 is the maximum allowed count
                count=200,
            )
        except tweepy.TweepError as error:
            print(error.args[0][0]["message"])
            time.sleep(2)
            main()

        all_tweets = []
        url_tweets = []
        url_retweets = []
        url_images = []
        url_videos = []
        hashtags = []
        all_tweets.extend(tweets)
        oldest_id = tweets[-1].id

        while True:
            tweets = api.user_timeline(
                screen_name=user_to_scrape,
                # 200 is the maximum allowed count
                count=200,
                max_id=oldest_id - 1,
            )
            if len(tweets) == 0:
                break
            oldest_id = tweets[-1].id
            all_tweets.extend(tweets)

        for tweet in all_tweets:

            hashtags_list = tweet.entities.get("hashtags")
            for hashtag in hashtags_list:
                if hashtag not in hashtags:
                    hashtags.append("#" + hashtag["text"])

            # Extract Media
            media = tweet.entities.get("media", [])
            try:
                # If it's a video
                extended_entities = tweet.extended_entities.get("media", [])
                url_videos.append(
                    extended_entities[0]["video_info"]["variants"][0]["url"]
                )
            except Exception:
                pass

            # If image exists
            if len(media) > 0:
                url_images.append(media[0]["media_url"])

            # Check if Retweet
            if hasattr(tweet, "retweeted_status"):
                try:
                    url_retweets.append(
                        "https://twitter.com/i/web/status/" + tweet.id_str
                    )
                except AttributeError:
                    pass
            else:
                try:
                    url_tweets.append(
                        "https://twitter.com/i/web/status/" + tweet.id_str
                    )
                except AttributeError:
                    pass

        print("Tweets: " + str(len(url_tweets)))
        print("Retweets: " + str(len(url_retweets)))
        print("Images: " + str(len(url_images)))
        print("Videos: " + str(len(url_videos)))
        print("Hashtags: " + str(len(hashtags)))

        time.sleep(random_time_2_to_5)

        return url_tweets, url_retweets, url_images, url_videos, hashtags

    except Exception as error:
        print("extract_tweets function failed.")
        print("Error details: " + error)


def extract_likes(user_to_scrape):
    """
    Function to extract likes of a user
    """
    try:

        url_favorites = []

        print("Extracting Likes, please wait...!")

        favorites = tweepy.Cursor(
            api.favorites, user_to_scrape, count=200).items()

        for tweet in favorites:
            url_favorites.append(
                "https://twitter.com/i/web/status/" + tweet.id_str)

        print("Likes: " + str(len(url_favorites)))
        return url_favorites

    except Exception as error:
        print("extract_likes function failed.")
        print("Error details: " + error)


def save_to_csv(
    user_to_scrape, tweets, retweets, images, videos, hashtags, likes, pinned_tweet
):
    """
    Function to save result from CSV
    """
    try:
        full_list = [tweets, retweets, images,
                     videos, hashtags, likes, pinned_tweet]
        file_name = user_to_scrape + ".csv"

        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    "Tweets",
                    "Retweets",
                    "Images",
                    "Videos",
                    "Hashtags",
                    "Likes",
                    "Pinned",
                )
            )
            for values in zip_longest(*full_list):
                writer.writerow(values)

    except Exception as error:
        print("save_to_csv function failed.")
        print("Error details: " + error)


def main():
    """
    Principal function
    """
    try:

        # Choose a user
        user_to_scrape = input("User to scrape: ")

        # Extract Tweets, Retweets and Media
        tweets, retweets, images, videos, hashtags = extract_tweets(
            user_to_scrape)

        # Extract Likes
        likes = extract_likes(user_to_scrape)

        print("\n")
        print("############################################################")
        print("# To extract a pinned Tweet we must do it with Selenium    #")
        print("# because the Twitter api does not return this information #")
        print("# at the moment.                                           #")
        print("############################################################")
        print("\n")

        print("Login to Twitter")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Open Browser
        driver = webdriver.Chrome(PATH_CHROME_DRIVER)
        driver.get(URL + "/login")
        driver.maximize_window()
        print("Twitter Open Succesfully...!")
        time.sleep(5)

        # Login in Twitter
        login(driver, username, password)

        # Extract pinned Tweet
        pinned_tweet = extract_pinned_tweet(driver, user_to_scrape)

        # Exit Driver
        driver.close()

        # Save and export to C
        save_to_csv(
            user_to_scrape,
            tweets,
            retweets,
            images,
            videos,
            hashtags,
            likes,
            pinned_tweet,
        )

        print("Scrap Finish...!")

    except Exception as error:
        print("Something Went Wrong...!")
        print("Error details: " + error)


if __name__ == "__main__":
    main()
