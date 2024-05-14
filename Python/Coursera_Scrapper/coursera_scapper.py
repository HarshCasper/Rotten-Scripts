#!/usr/bin/env python3
"""
This module is used to scrape the Coursera website to get course data.
"""
import csv
import os
import requests
import bs4

BASE_URL = "https://www.coursera.org"
SEARCH_BASE_URL = "https://www.coursera.org/search?query="

# pylint: disable=W0621
def get_soup(url: str, query: str, page: int = None) -> bs4.BeautifulSoup:
    """
    This function takes the query, URL to parse it into and returns the soup object.
    """
    try:
        if page is None:
            url = url + query
        else:
            url = url + query + f'&page={page}'

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        return soup
    except requests.exceptions.RequestException as error:
        print(f"Error occurred while making the request: {error}")
        return None
    except bs4.FeatureNotFound as error:
        print(f"\nError occurred while parsing the HTML: {error}\tSkipping...\n")
        return None


def get_course_links(soup: bs4.BeautifulSoup) -> list[str]:
    """
    This function takes the soup object and returns the course links.
    """
    try:
        if soup.select_one('div[data-e2e="NumberOfResultsSection"] span') is not None:
            result_text = soup.select_one('div[data-e2e="NumberOfResultsSection"] span').text
            if result_text.startswith('No results found for'):
                return None

        course_links = soup.select('a[id*=product-card-title]')
        courses_links = [link.get('href') for link in course_links]
        return courses_links
    except (AttributeError, ValueError, IndexError) as error:
        print(f"\nError occurred while getting course links: {error}\tSkipping...\n")
        return None


def get_title(soup: bs4.BeautifulSoup) -> str:
    """
    Given the soup object, this function returns the course title.
    """
    try:
        title = soup.select_one('h1[data-e2e=hero-title]').text
        return title
    except (AttributeError, ValueError) as error:
        print(f"\nError occurred while getting course title: {error}\tSkipping...\n")
        return None


def get_course_ratings_reviews(soup: bs4.BeautifulSoup) -> str:
    """
    Given the soup object, this function returns the course ratings and reviews.
    """
    ratings = None
    try:
        tags = soup.select('div.cds-119.cds-Typography-base.css-h1jogs.cds-121')
        for tag in tags:
            try:
                rating = float(tag.text.strip())
                ratings = rating
                break
            except ValueError:
                continue
    except (AttributeError, ValueError) as error:
        print(f"\nError occurred while getting ratings: {error}\tSkipping...\n")
    try:
        reviews = soup.select_one('p.css-vac8rf:-soup-contains("review")').text
    except requests.exceptions.RequestException as error:
        print(f"\nError occurred while making the request: {error}\tSkipping...\n")
        reviews = None
    except (bs4.FeatureNotFound, AttributeError, ValueError) as error:
        print(f"\nError occurred while parsing the HTML: {error}\tSkipping...\n")
        reviews = None

    result = f"{ratings} {reviews}"
    return result


def get_start_date(soup: bs4.BeautifulSoup) -> str:
    """
    Given the soup object, this function returns the start date of the course.
    """
    try:
        start_date = soup.select_one('div.startdate').text
        start_date = start_date.replace('Starts', '').strip()
        return start_date
    except requests.exceptions.RequestException as error:
        print(f"\nError occurred while making the request: {error}\tSkipping...\n")
        return None
    except (AttributeError, ValueError, bs4.FeatureNotFound) as error:
        print(f"\nError occurred while parsing the HTML: {error}\tSkipping...\n")
        return None


def get_course_duration(soup: bs4.BeautifulSoup) -> str:
    """
    Given the soup object, this function returns the course duration.
    """
    try:
        tags = soup.select('div.cds-119.cds-Typography-base.css-h1jogs.cds-121')
        for tag in tags:
            text = tag.text.strip()
            if 'month' in text or 'week' in text or 'hours' in text or 'minutes' in text:
                course_duration = text
                break
        return course_duration
    except (AttributeError, ValueError, UnboundLocalError) as error:
        print(f"\nError occurred while getting course duration: {error}\tSkipping...\n")
        return None


def get_difficulty(soup: bs4.BeautifulSoup) -> str:
    """
    Given the soup object, this function returns the course difficulty.
    """
    try:
        tags = soup.select('div.cds-119.cds-Typography-base.css-h1jogs.cds-121')
        for tag in tags:
            text = tag.text.strip()
            if 'level' in text and len(text.split()) < 4:
                difficulty = text
                break
        return difficulty
    except (AttributeError, ValueError, UnboundLocalError) as error:
        print(f"\nError occurred while getting difficulty: {error}\tSkipping...\n")
        return None


def get_skills(soup: bs4.BeautifulSoup) -> str:
    """
    Given the soup object, this function returns the skills you'll gain.
    """
    try:
        skills_list = []
        ul_tag = soup.find('ul', class_='css-yk0mzy')
        if ul_tag:
            li_tags = ul_tag.find_all('li')
            skills_list = [li.text for li in li_tags]
        return '; '.join(skills_list)
    except (AttributeError, ValueError, UnboundLocalError) as error:
        print(f"\nError occurred while getting skills: {error}\tSkipping...\n")
        return None


def append_to_csv(query: str, line: str) -> None:
    """
    Append the line to the CSV file.
    """
    filename = f"{query}.csv"
    header = ["Index",
              "Title",
              "Course Link",
              "Ratings & Reviews",
              "Difficulty",
              "Start Date",
              "Course Duration",
              "Skills Gained"
            ]
    data = [line.split(", ")]

    if os.path.isfile(filename):
        with open(filename, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    else:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)


def full_query(query: str, limit: int = 50) -> None:
    """
    Perform a full query to scrape course data.
    """
    page = 1
    soup = get_soup(SEARCH_BASE_URL, query, page)
    courses_links = get_course_links(soup)
    index = 1
    while courses_links is not None:
        for course_link in courses_links:
            if index > limit:
                print("Courses successfully retrieved!")
                return
            # get course data
            html_soup = get_soup(BASE_URL, course_link)
            title = get_title(html_soup)
            ratings_reviews = get_course_ratings_reviews(html_soup)
            difficulty = get_difficulty(html_soup)
            start_date = get_start_date(html_soup)
            course_duration = get_course_duration(html_soup)
            skills = get_skills(html_soup)

            # Handle None values
            title = title.replace(',', '') if title else 'None'
            ratings_reviews = ratings_reviews.replace(',', '') if ratings_reviews else 'None'
            difficulty = difficulty.replace(',', '') if difficulty else 'None'
            start_date = start_date.replace(',', '') if start_date else 'None'
            course_duration = course_duration.replace(',', '') if course_duration else 'None'
            skills = skills.replace(',', '') if skills else 'None'

            line = (
                    f"{index}, "
                    f"{title.replace(',', '')}, "
                    f"{BASE_URL + course_link}, "
                    f"{ratings_reviews.replace(',', '')}, "
                    f"{difficulty.replace(',', '')}, "
                    f"{start_date}, "
                    f"{course_duration}, "
                    f"{skills}"
                    )

            append_to_csv(query, line)
            print(f"Data for {title} has been saved to {query}.csv")
            index += 1
        page += 1
        soup = get_soup(SEARCH_BASE_URL, query, page)
        courses_links = get_course_links(soup)


if __name__ == '__main__':
    print("Welcome to Coursera Course Scraper!\n")
    query = input("Please enter the course you would like to be scraped: ")
    try:
        LIMIT = int(input("Please enter the limit of the courses you want (an integer value): "))
        print("Limit value received. Beginning scrape...")
    except ValueError:
        print("Incorrect value entered. Falling back to default...")
        LIMIT = 100
    full_query(query, LIMIT)
