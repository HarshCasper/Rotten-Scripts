from plyer import notification
import praw
import time
import os
import random

print("----------Set your preferences---------") 
client_id = input("Enter your client ID: ")
client_secret = input("Enter your client secret: ")
user_agent = input("Enter your user agent: ")
subreddit = input("Enter which subreddit updates you want: ")
timing = int(input("Enter the time interval in seconds: "))
print("Now sit back and enjoy...")

reddit = praw.Reddit(client_id=client_id, 
                    client_secret=client_secret,
                    user_agent=user_agent)  # Reddit instance
 

def new_posts(subreddit):
    posts = reddit.subreddit(subreddit).new(limit=10)  # New post from Subreddits
    posts_list = [i.title for i in posts]
    return posts_list


def notifyUser(message,title):
    notification.notify(
        title = title,
        message = message,
        app_icon = os.path.dirname(os.path.realpath(__file__))+ '\icon\inform.ico',
        timeout = 15
    )  # Sending out notifications


while True:
    index = random.randint(0,9)  # Selecting a random index 
    notifyUser(message=new_posts(subreddit=subreddit)[index][:256], 
               title=subreddit)  # Max Message length supported is 256
    time.sleep(timing)
