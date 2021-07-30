import tweepy
import requests
import csv
from pathlib import Path
from decouple import config

# Authenticate to Twitter
CONSUMER_KEY = config("CONSUMER_KEY")
CONSUMER_SECRET = config("CONSUMER_SECRET")

# Authenticate to Twitter with OAuth 2.0
auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

api = tweepy.API(auth)


def download_img(url):
    '''Downloads an image from the given url and saves it to the downloads folder'''
    img_path = './downloads/' + url.split('/')[-1]
    print(f"Downloading image: {url}")
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(img_path, 'wb') as image:
            for chunk in r:
                image.write(chunk)
    else:
        print(f"Failed to download image {url}")


def main():
    twitterHandle = input("Enter twitter handle: @")
    amount = int(
        input("Enter amount of tweets to look for images (default 20): ") or 20)
    downloaded = 0

    print("Downloading images from {}'s tweets...".format(twitterHandle))

    try:
        # Create the 'downloads' directory if it doesn't exist
        Path("./downloads").mkdir(exist_ok=True)

        # Open a csv file to store the information about downloaded images
        csvFile = open('./downloads/downloaded_images.csv', 'w')
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(['Tweet URL', 'Image ID', 'Image URL'])

        for tweet in tweepy.Cursor(api.user_timeline, screen_name=twitterHandle).items(amount):
            tweet_url = 'https://twitter.com/' + \
                twitterHandle + '/status/' + tweet.id_str
            images = tweet.entities.get("media", [])
            images_len = len(images)
            if images_len > 0:
                for image in images:
                    if image["type"] == "photo":
                        csvWriter.writerow(
                            [tweet_url, image["id"], image["media_url"]])
                        download_img(image["media_url"])
                        downloaded += 1

        csvFile.close()

    except tweepy.TweepError as e:
        if e.response.status_code == 400:
            print("Invalid or expired token.")
        elif e.response.status_code == 404:
            print("Invalid twitter handle.")
        elif e.response.status_code == 420:
            print("Rate limit exceeded. Please wait 15 minutes and try again.")
        else:
            print("Error: ", e)

    except IOError as e:
        print("Error: ", e)

    if downloaded == 0:
        print("No images found")
    else:
        print(
            f"Downloaded {downloaded} image(s) and written info in ./downloaded_images.csv")


if __name__ == '__main__':
    main()

