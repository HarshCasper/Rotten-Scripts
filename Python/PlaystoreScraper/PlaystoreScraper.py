import time
from selenium import webdriver
import csv


def write_to_csv(row_array):
    """
    The function stores the scraped info in a .csv file
    """
    # Headings for the first row of the file
    header_list = [
        "URL",
        "NAME",
        "RATING",
        "REVIEW",
        "INSTALLS",
        "CURRENT VERSION",
        "LAST UPDATED",
        "COMPANY",
        "CONTACT",
    ]
    file_name = input("\nEnter the name of file to store the info: ")

    # Adding info into the rows of the file
    with open(file_name + ".csv", "a", encoding="utf-8") as csv_f:
        csv_pointer = csv.writer(csv_f, delimiter=",")
        csv_pointer.writerow(header_list)
        csv_pointer.writerows(row_array)

    print(f"Done! Check your directory for {file_name}.csv file!")


def scraper():
    """
    The function makes use of Selenium to scrape the required information
    which is later stored in a .csv file
    """
    driver = webdriver.Chrome()
    while 1:
        # Takes user input for query
        query = input("\nEnter search query: ")

        # Getting the URL for the search
        driver.get(f"https://play.google.com/store/search?q={query}&c=apps")

        print(f"\nCollecting information for {query}...\n")

        # Time for the page to load
        time.sleep(5)

        # Inorder to enable scrolling to collect all the necessary information
        last_height = driver.execute_script("return document.body.scrollHeight")
        time.sleep(5)

        # Scrolling till the end of the page
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(5)

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Storing all the URLS of the apps shown throughout the page
        store_urls = []
        elems = driver.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            if "details?id" in elem.get_attribute("href"):
                store_urls.append((elem.get_attribute("href")))

        # Removing duplicates
        store_urls = list(dict.fromkeys(store_urls))

        all_info = []
        # Going into each URL to gather the details we require
        for every in store_urls:
            try:
                each_info = []
                # get URL
                driver.get(every)
                each_info.append(every)
                time.sleep(3)

                # get app name
                header1 = driver.find_element_by_tag_name("h1")
                each_info.append(header1.text)

                # get the star rating
                star = driver.find_element_by_class_name("BHMmbe")
                each_info.append(star.text)

                # get the number of comments
                comments = driver.find_element_by_class_name("EymY4b")
                each_info.append(comments.text.split()[0])

                # get the footer information like installs, version, email, etc.
                stat_info_table = driver.find_elements_by_class_name("htlgb")
                stats = []
                for x in range(len(stat_info_table)):
                    if x % 2 == 0:
                        stats.append(stat_info_table[x].text)

                stat_header = driver.find_elements_by_class_name("BgcNfc")
                for x in range(len(stat_header)):
                    if stat_header[x].text == "Installs":
                        each_info.append(stats[x])

                    if stat_header[x].text == "Current Version":
                        each_info.append(stats[x])

                    if stat_header[x].text == "Updated":
                        each_info.append(stats[x])

                    if stat_header[x].text == "Offered By":
                        each_info.append(stats[x])

                    if stat_header[x].text == "Developer":
                        for y in stats[x].split("\n"):
                            if "@" in y:
                                each_info.append(y)
                                break

                all_info.append(each_info)

            except Exception as e:
                continue

        print("\nAll info collected successfully!!\n")
        print("\nDONE!\n")

        # Writing the collected info in a csv file
        write_to_csv(all_info)

        ans = input("Press (y) to continue or any other key to exit: ").lower()
        if ans == "y":
            continue
        print("Exiting..")
        break


if __name__ == "__main__":
    scraper()
