import urllib.request
import json
import sys
import ctypes
import time
import os

subredditName = sys.argv[1]


def setBackgroundFromSubreddit(subredditName):
    topImagePost = getTopImageFromSubreddit(subredditName)
    imageFilename = storeImageInStoredBackgroundsFolder(topImagePost)
    setImageAsBackground(imageFilename)
    return topImagePost


def getTopImageFromSubreddit(subredditName):
    topImagePosts = getTopImagePostsFromSubreddit(subredditName)
    topPost = topImagePosts[0]["data"]
    return topPost


def getTopImagePostsFromSubreddit(subredditName):
    # this URL gives the top images of the last 24 hours in .jpg or .png format, as JSON text
    subredditPostsUrl = (
        "https://www.reddit.com/r/"
        + subredditName
        + "/search.json?q=url%3A.jpg+OR+url%3A.png&sort=top&restrict_sr=on&t=day"
    )

    while True:
        try:
            # this returns the text of the address above as a string
            postsAsJsonRawText = urllib.request.urlopen(subredditPostsUrl).read()
            break
        except urllib.error.HTTPError as err:
            time.sleep(5)

    # this takes the JSON text as parameter and returns a Python object
    decodedJson = json.loads(postsAsJsonRawText.decode("utf-8"))
    # in the reddit API, the individual posts are known as children
    # so we use "data" node and then go to "children"
    posts = decodedJson["data"]["children"]
    # this will return the list of all children retreived from JSON
    return posts


def storeImageInStoredBackgroundsFolder(image):
    createStoredBackgroundsFolderIfNotExists()
    imageSuffix = int(round(time.time() * 1000))
    # stores the image with the specified URL on your computer with the specified filename
    imageFilename = "bg_" + str(imageSuffix) + ".jpg"
    open("stored_backgrounds/" + imageFilename, "wb").write(
        urllib.request.urlopen(image["url"]).read()
    )
    return imageFilename


def createStoredBackgroundsFolderIfNotExists():
    if not os.path.exists("stored_backgrounds"):
        os.makedirs("stored_backgrounds")


def setImageAsBackground(imageFilename):
    # sets the downloaded image as desktop wallpaper
    # Python2 uses SystemParametersInfoA and Python3 uses SystemParametersInfoW
    ctypes.windll.user32.SystemParametersInfoW(
        20, 0, getFullPathOfImage(imageFilename), 0
    )


def getFullPathOfImage(imageFilename):
    return (
        os.path.dirname(os.path.realpath("stored_backgrounds/" + imageFilename))
        + "\\"
        + imageFilename
    )


setBackground = setBackgroundFromSubreddit(subredditName)
