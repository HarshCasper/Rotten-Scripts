# Linkedin Posts Scrapper
# Written by XZANATOL
from optparse import OptionParser
from selenium import webdriver
import pandas as pd
import time
import sys
import re

pattern_head = "<span>(.*)</span></span>"
pattern_reactions = """aria-label="(\d+) """

# Help menu
usage = """
<Script> [Options]

[Options]
    -h, --help        Show this help message and exit.
    -e, --email       Enter login email
    -p, --password    Enter login password
    -n, --number      Number of posts to be scrapped
"""

# Load args
parser = OptionParser()
parser.add_option("-e", "--email", dest="email", help="Enter login email")
parser.add_option("-p", "--password", dest="password", help="Enter login password")
parser.add_option("-n", "--number", dest="count", help="Number of posts to be scrapped")


def login(email, password):
    """LinkedIn automated login function"""
    # Get LinkedIn login page
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.linkedin.com")
    # Locate Username field and fill it
    session_key = driver.find_element_by_name("session_key")
    session_key.send_keys(email)
    # Locate Password field and fill it
    session_password = driver.find_element_by_name("session_password")
    session_password.send_keys(password)
    # Locate Submit button and click it
    submit = driver.find_element_by_class_name("sign-in-form__submit-button")
    submit.click()
    # Check credentials output
    if driver.title != "LinkedIn":
        print("Provided E-mail/Password is wrong!")
        driver.quit()
        sys.exit()
    # Return session
    return driver


def get_to_endpoint(driver):
    """Loads /detail/recent-activity/shares/ endpoint"""
    time.sleep(5) # wait for the whole page to load
    profile_link = driver.find_elements_by_tag_name('a')  # Scrap endpoint link
    for i in profile_link:
        link = i.get_attribute("href")
        if "/detail/recent-activity/shares/" in link:
            break
    driver.get(link)  # Connect to the endpoint
    return driver


def post_scrap(driver, count):
    """Returns a list of scrapped posts"""
    time_to_wait = 3
    for n in range(count):  # Load Ajax calls according to the required number of scraps
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(time_to_wait)
        # Scrolling throught the whole page to make sure that all posts are loaded
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*3/4);")
        time.sleep(time_to_wait)
        driver.execute_script("window.scrollTo(0, 0);")

    time.sleep(time_to_wait)  # Make sure all the Ajax calls are finished
    cards = driver.find_elements_by_class_name("feed-shared-update-v2--minimal-padding")
    headings = []
    reactions = []
    for card in cards:
        card = card.get_attribute("innerHTML")   
        try:  # Append headings
            headings.append(re.search(pattern_head, card)[1])
        except:
            headings.append("None")
        # Append reactions
        reactions.append(re.findall(pattern_reactions, card))

    # Validate reactions lenghts
    for num in range(len(reactions)):
        reaction = reactions[num]
        while len(reaction) != 2:
            reactions[num].append("None")

    return driver, headings[:count], reactions[:count]


def to_csv(headings, reactions):
    """Save inputs to a CSV file"""
    # Make a dataframe and append data to it
    df = pd.DataFrame()
    for i in range(len(headings)):
        df = df.append({"Heading": headings[i], "Reactions": reactions[i][0], "Comments": reactions[i][1]}, ignore_index=True)
    # Save to CSV
    df.to_csv("Scrap.csv", index=False, columns=["Heading", "Reactions", "Comments"])


# Start checkpoint
if __name__ == "__main__":
    (options, args) = parser.parse_args()

    # Inputs
    email = options.email
    password = options.password
    count = int(options.count)

    driver = login(email, password)  # Login Phase
    print("Successfull Login!")
    print("Connectiong to '/detail/recent-activity/shares/' endpoint...")
    driver = get_to_endpoint(driver)  # Get to required endpoint
    print("Success!!")
    print("Commencing post scrap...")
    driver, headings, reactions = post_scrap(driver, count)
    print("Done!!")
    to_csv(headings, reactions)
    print("Saved file to 'Scrap.csv'.")
    input("Press any key to exit...")
    driver.quit()
    sys.exit()
