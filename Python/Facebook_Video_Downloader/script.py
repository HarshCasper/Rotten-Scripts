# ALL Imports
import sys

from tqdm import tqdm
from requests import get, HTTPError, ConnectionError
from re import findall
from urllib.parse import unquote


def Invalid_Url():
    print("Invalid URL , Please Enter Correct URL")


def get_video_downloadlink(url):

    url = url.replace("www", "mbasic")
    try:
        r = get(url, timeout=5, allow_redirects=True)
        if r.status_code != 200:
            raise HTTPError
        a = findall("/video_redirect/", r.text)
        if len(a) == 0:
            print("[!] Video Not Found...")
            sys.exit(0)
        else:
            return unquote(r.text.split("?src=")[1].split('"')[0])
    except (HTTPError, ConnectionError):
        print("[x] Invalid URL")
        sys.exit(1)


def download_video(url):

    block_size = 1024  # 1kB
    r = get(url, stream=True)
    total_size = int(r.headers.get("content-length"))
    progress_bar = tqdm(total=total_size, unit="iB", unit_scale=True)
    with open("video.mp4", "wb") as file:
        for data in r.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    print("Video Downloaded")
    if total_size != 0 and progress_bar.n != total_size:
        print("ERROR, something went wrong")


def main():
    url = input("Enter the URL of Facebook Video you want to download:- ")
    if not "www.facebook.com" in url:
        Invalid_Url()
        return

    link = get_video_downloadlink(url)
    download_video(link)


if __name__ == "__main__":
    main()
