from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time
from selenium.webdriver.common.by import By
import csv

browser = webdriver.Chrome()

pageurl = "https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fsearch%2Fresults%2Fpeople%2F%3Fnetwork%3D%255B%2522F%2522%255D%26origin%3DMEMBER_PROFILE_CANNED_SEARCH&fromSignIn=true&trk=cold_join_sign_in"

paginationurl = "https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&page="


# Function to read username and password from file
def read_creds(filename):

    """This function reads username and password from creddentials.json

    Arguments:
    filename: name of the file which stores the credentials

    :return: returns the credentials
    """
    with open(filename) as f:
        credentials = json.load(f)
    return credentials


# function to find skills
def find_skills(url):
    """This function find the skills from the linkedin profile of the connection

    Arguments:
    url: url of the profile

    :return: returns the list contsining skills
    """
    browser.get(url)
    time.sleep(3)
    skill_set = []
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        browser.execute_script("window.scrollTo(0, window.scrollY + 400);")
        time.sleep(2)

        new_height = browser.execute_script("return window.scrollY + 400")

        if new_height == last_height:
            break
        last_height = new_height

    time.sleep(2)

    Skills = browser.find_elements_by_class_name("pv-skill-category-entity")
    if len(Skills) == 0:
        skill_set.append("Any Skill is not mentioned in the Linkedin Profile")
    else:
        show_more_button = browser.find_elements_by_class_name(
            "pv-skills-section__additional-skills"
        )
        if len(show_more_button) > 0:
            browser.execute_script("arguments[0].click();", show_more_button[0])

        pagesource = browser.page_source
        content = BeautifulSoup(pagesource, "html.parser")
        Skills = content.find_all("li", class_="pv-skill-category-entity")
        for skill in Skills:
            skill_text = skill.find(
                "p", class_="pv-skill-category-entity__name"
            ).text.strip()
            skill_set.append(skill_text.split("\n")[0])
    return skill_set


# Function to login
def login_and_npage():
    """This function login to the linkedin page return the number of pages of connection


    :return: number of pages
    """
    creds = read_creds("credentials.json")

    # open login page
    browser.get(pageurl)
    elementID = browser.find_element_by_id("username")
    elementID.send_keys(creds["username"])
    elementID = browser.find_element_by_id("password")
    elementID.send_keys(creds["password"])
    elementID.submit()
    url = browser.current_url

    browser.get(url)

    connectionclass = "mn-connection-card__details"

    numberofpages = 0

    time.sleep(2)
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        elements = browser.find_elements_by_class_name(
            "artdeco-pagination__indicator--number"
        )

        if len(elements) > 0:
            numberofpages = int(elements[-1].text)
            return numberofpages

        # Wait to load page
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height
    return 0


# function to find connection data containing name and profileurl only
def connectiondatahelper(numberofpages):
    """This function returns the data of connections containg name and profile url

    Arguments:
    numberofpages:number of pages of connections

    :return: connectiondata
    """

    connectiondata = []
    for j in range(1, numberofpages + 1):
        browser.get(paginationurl + str(j))
        time.sleep(3)
        pagesource = browser.page_source
        soup = BeautifulSoup(pagesource, "html.parser")
        connections = soup.find_all("div", class_="entity-result__content")

        for connection in connections:
            titlecontainer = connection.find(class_="entity-result__title-text")
            nameelement = titlecontainer.find("a", class_="app-aware-link")
            nametext = nameelement.find("span", {"dir": "ltr"}).text.split("View")[0]
            url = nameelement["href"]
            connectionobj = {"name": nametext, "profileurl": url}
            connectiondata.append(connectionobj)

    return connectiondata


# '''function for finding required data of connection'''
def finalconnectiondata(connectiondata):
    """This function returns the  list containing the data of all connections

    Arguments:
    connectiondata: list containing the name and profileurl of the connections

    :return: finalconnectiondata
    """
    final_connectiondata = []

    for connection in connectiondata:
        skill_set = find_skills(connection["profileurl"])
        browser.get(connection["profileurl"])
        time.sleep(3)

        pagesource = browser.page_source

        soup = BeautifulSoup(pagesource, "html.parser")

        experiencecontainer = soup.find(
            "a", {"data-control-name": "background_details_company"}
        )

        if experiencecontainer is None:
            l_jobtitile = "Don't Have any Job Experience"
        else:
            l_jobtitile = experiencecontainer.find("h3").text.strip()

        last_height = browser.execute_script("return document.body.scrollHeight")

        time.sleep(2)

        linken_connection = {
            "Name": connection["name"],
            "Linkedin_URL": connection["profileurl"],
            "Latest_JOB_Position": l_jobtitile,
            "Skills": skill_set,
        }
        final_connectiondata.append(linken_connection)

    return final_connectiondata


def main():
    """function of execution"""
    browser.maximize_window()
    numberofpages = login_and_npage()
    smalldata_of_connections = connectiondatahelper(numberofpages)
    final_connectiondata = finalconnectiondata(smalldata_of_connections)
    browser.quit()
    keys = final_connectiondata[0].keys()
    with open("output.csv", "w", newline="") as output_file:

        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(final_connectiondata)


if __name__ == "__main__":
    main()
