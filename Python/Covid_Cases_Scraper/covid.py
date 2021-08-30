import bs4
import requests

try:
    print(
        "For which region you want to see the COVID-19 cases?\nPlease write below!\n"
        "Example:\noverall/total/worldwide/all - for overall cases in the world\ncountry/COunTRY/COUNTRY/Country - for any specific country"
    )

    # getting the input from user, for which region the user want to see the cases
    c_query = input().lower()
    print()

    # checking the first conditon, if c_query contains one of these word then this block will be executed
    if (
        "overall" in c_query
        or "over all" in c_query
        or "world" in c_query
        or "total" in c_query
        or "worldwide" in c_query
        or "all" in c_query
    ):

        def world_cases():

            # fetching the worldwide cases data from the website
            url = "https://www.worldometers.info/coronavirus/"

            # fetching the data from website to the console using get() function of requests library
            info_html = requests.get(url)

            # parsing the html data into text using lxml parser with the help of bs4 library
            info = bs4.BeautifulSoup(info_html.text, "lxml")

            # searching for div tag inside the html content to get the desired data
            info2 = info.find("div", class_="content-inner")

            # searching for all the tags having id maincounter-wrap inside the html content to get the desired data
            new_info = info2.findAll("div", id="maincounter-wrap")

            print("Worldwide Covid-19 information--")

            # printing the desired data from the new_info variable
            for i in new_info:
                head = i.find("h1", class_=None).get_text()
                counting = i.find("span", class_=None).get_text()
                print(head, "", counting)

        world_cases()

    # checking the second conditon if first one fails, if c_query contains one of these word then this block will be executed
    elif "country" in c_query or "specific country" in c_query:

        def country_cases():

            print("Write the country name?")

            # taking the country name as input from user and converting it into lowercase
            c_name = input().lower()
            print()

            # fetching the data for particular country from the website
            c_url = f"https://www.worldometers.info/coronavirus/country/{c_name}/"

            # fetching the data for the country from website to the console using get() function of requests library
            data_html = requests.get(c_url)

            # parsing the html data into text using lxml parser with the help of bs4 library
            c_data = bs4.BeautifulSoup(data_html.text, "lxml")

            # searching for div tag with class content-inner and then all div tags having id maincounter-wrap inside the html content to get the desired data
            new_data = c_data.find("div", class_="content-inner").findAll(
                "div", id="maincounter-wrap"
            )
            print(f"Covid-19 information for {c_name.capitalize()}--")

            # printing the desired data from the new_data variable
            for j in new_data:
                c_head = j.find("h1", class_=None).get_text()
                c_counting = j.find("span", class_=None).get_text()
                print(c_head, "", c_counting)

        country_cases()

    # this will be executed if the above conditons fails and this message will be displayed
    else:
        print("There is something wrong. Please try again.")

except Exception as e:
    pass
