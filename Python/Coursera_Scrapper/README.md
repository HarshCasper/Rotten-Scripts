• This Python script is a web scraper for the Coursera website. It fetches information about courses based on a user-provided query and saves the data to a CSV file. Here's a breakdown of the script:

• The script imports necessary libraries: *bs4* for parsing HTML, *csv* for writing to CSV files, *os* for interacting with the OS, and *requests* for making HTTP requests.

• It defines constants for the base URL and search URL of Coursera.

• The get_soup function makes a GET request to the provided URL and returns a BeautifulSoup object of the HTML content.

• The get_courses_links function extracts the links of the courses from the search results page.

• The get_title, get_course_ratings_reviews, get_start_date, get_course_duration, get_difficulty, and get_skills functions extract specific details about a course from its page.

• The append_to_csv function writes the scraped data to a CSV file. If the file doesn't exist, it creates one and writes the header and data; otherwise, it appends the data.

• The full_query function is the main function that coordinates the scraping process. It calls the other functions to scrape the data, handles any None values, and writes the data to the CSV file.

• In the if __name__ == '__main__': block, the script prompts the user for a course query and the limit of courses to scrape, then calls the full_query function with these inputs.

# Note: This script uses CSS selectors to locate elements on the webpage. If Coursera changes its website structure, the script may stop working.

# Note: The Errors that are being printed in the stdout means that that particular course does not have that specific attribute and they should be ignored

![image for the working scrapper](https://i.imgur.com/hNRi2cY.png)
