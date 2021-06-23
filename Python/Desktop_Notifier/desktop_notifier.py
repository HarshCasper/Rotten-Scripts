# pip install and import the packages & modules

import feedparser
import notify2
import time
import os
from pygame import mixer

# initialize the mixer module
mixer.init()

# load the notification sound
mixer.music.load("alarm.mp3")


def Parsefeed():

    # parsing news data from the feed URL
    f = feedparser.parse("http://timesofindia.indiatimes.com/rssfeedstopstories.cms")
    # set any icon for the notification
    ICON_PATH = os.getcwd() + "/icon.ico"
    # initalize the notify2 using init method and initializing the D-bus connection
    notify2.init("News Notify")

    # Looping from the parsed data to get the relevant information and setting the notification icon using notify2 lib

    for newsitem in f["items"]:
        print(newsitem["title"])
        print(newsitem["summary"])
        print("\n")

        # create Notification object
        n = notify2.Notification(newsitem["title"], newsitem["summary"], icon=ICON_PATH)
        # set urgency level
        n.set_urgency(notify2.URGENCY_NORMAL)
        # show notification on screen
        n.show()

        # set timeout for a notification
        n.set_timeout(100)
        # short delay between notifications
        time.sleep(10)


if __name__ == "__main__":

    # call the functions
    try:
        Parsefeed()
        mixer.music.play()  # start producing sound while showing notification
        time.sleep(10)  # short delay
        mixer.music.pause()  # pause the sound
    except:
        print("Error")
