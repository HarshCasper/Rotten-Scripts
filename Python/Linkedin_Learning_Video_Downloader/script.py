from selenium import webdriver
from dotenv import load_dotenv
from pathlib import Path
import os
from requests import get
from tqdm import tqdm
import time
from bs4 import BeautifulSoup

env_path = Path(".", ".env")
load_dotenv(dotenv_path=env_path)


def read_creds():

    """This function reads the environmental variables."""

    credentials = {"username": os.getenv("username"), "password": os.getenv("password")}
    return credentials


def videos_downloader_main(browser, course_url):
    """
    Main function for execution for downloading videos
    Arguments:-
    browser: browser where task run
    course_url: url of the linkedin learning course
    """
    login(browser, "https://www.linkedin.com/learning/")
    time.sleep(1)
    video_urls = []
    browser.get(course_url)
    time.sleep(2)

    # add urls of the vides in the video_urld list
    video_elements = browser.find_elements_by_css_selector(".classroom-toc-item a")
    for video_element in video_elements:
        video_url = video_element.get_attribute("href")
        video_urls.append(video_url)

    # Dictionary will store name of courses and their source url
    video_srcs_wth_name = {}

    # loop through the video urls to find the source of videos
    for video_url in video_urls:
        video_name = video_url.split("/")[-1]
        browser.get(video_url)
        time.sleep(2)
        pagesource = browser.page_source
        soup = BeautifulSoup(pagesource, "html.parser")
        if soup.select_one("video#vjs_video_3_html5_api.vjs-tech") is not None:
            video_element = browser.find_element_by_css_selector("video#vjs_video_3_html5_api.vjs-tech")
            video_src = video_element.get_attribute("src")
            video_srcs_wth_name[video_name] = video_src
    browser.close()

    # loop through video source to download videos
    for name, url in video_srcs_wth_name.items():
        download_video(url, name)


def download_video(url, name):
    """
    Function to download video
    Arguments:
    url: source url of the video
    name: name of the file with which video file to download video
    """
    block_size = 1024  # 1kB
    r = get(url, stream=True)
    total_size = int(r.headers.get("content-length"))
    video_name = name + ".mp4"
    progress_bar = tqdm(total=total_size, unit="iB", unit_scale=True)
    with open(video_name, "wb") as file:
        for data in r.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    print("Video Downloaded")
    if total_size != 0 and progress_bar.n != total_size:
        print("ERROR, something went wrong")


def login(browser, linkedin_url):
    """
    Function to login to linkedin Learning
    Arguments:
    browser: where task runs
    linkedin_url: URL of linkedin learning plateform
    """
    creds = read_creds()
    browser.get(linkedin_url)
    signin_btn = browser.find_element_by_css_selector(
        "a[data-tracking-control-name='homepage-learning_nav-header-signin']"
    )
    signin_btn.click()
    email_input = browser.find_element_by_css_selector("input#auth-id-input")
    email_input.send_keys(creds["username"])
    email_input.submit()
    time.sleep(2)
    pass_input = browser.find_element_by_id("password")
    pass_input.send_keys(creds["password"])
    pass_input.submit()


def main():
    """Main function of execution"""
    courseurl = input("Enter the URL of Linkedin Learning Course:- ")
    browser = webdriver.Chrome()
    browser.maximize_window()
    videos_downloader_main(browser, courseurl)


if __name__ == "__main__":
    main()
