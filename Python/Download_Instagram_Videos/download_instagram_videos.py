import urllib.request
import requests
import json
import re
import sys


def downloadVideo(postId):
    multiplePosts = False
    videos = []

    # sending get request and saving the response in the variable url
    url = requests.get("https://instagram.com/p/" + str(postId))

    # checking if the post exists
    if url.status_code == 404:
        print("Specified post not found")
        sys.exit()

    # extracting data in json format
    jsonData = json.loads(
        re.findall(r"window._sharedData\s=\s(\{.*\});</script>", url.text)[0]
    )
    data = jsonData["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]

    # checking if there are multiple posts in the given post ID
    if "edge_sidecar_to_children" in data.keys():
        multiplePosts = True

    # checking if the post is a video or not
    isVideo = data["is_video"]
    if not isVideo and not multiplePosts:
        print("No Videos found")
        sys.exit()

    # adding valid videos to the list named videos
    if isVideo:
        videos.append(data["video_url"])
    if multiplePosts:
        for post in data["edge_sidecar_to_children"]["edges"]:
            if post["node"]["is_video"]:
                videos.append(post["node"]["video_url"])

    # shows the total number of vidoes in the post
    print("Found " + str(len(videos)) + " videos")

    for number, video in zip(list(range(len(videos))), videos):
        print("Downloading video " + str(number + 1))
        urllib.request.urlretrieve(video, (postId + "_" + str(number + 1) + ".mp4"))


if len(sys.argv) == 1:
    print("Please enter the ID of the video")
else:
    downloadVideo(sys.argv[1])
