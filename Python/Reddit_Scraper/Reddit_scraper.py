import requests
import csv
import time
from bs4 import BeautifulSoup


def write_to_csv(row_array):
    """
    The function stores the scraped info in a .csv file
    :param row_array:
    :return:
    """
    # Headings for the first row of the file
    header_list = ['Title', 'Author', 'Date and Time', 'Upvotes',
                   'Comments', 'Url']
    file_name = input('\nEnter the name of file to store the info: ')

    # Adding info into the rows of the file
    with open(file_name + '.csv', 'a', encoding='utf-8') as csv_f:
        csv_pointer = csv.writer(csv_f, delimiter=',')
        csv_pointer.writerow(header_list)
        csv_pointer.writerows(row_array)

    print(f'Done! Check your directory for {file_name}.csv file!')


def scraper():
    """
    The function scrapes the post info from the desired subreddit and stores it
    into the desired file.
    :return:
    """
    subreddit = input('Enter the name of the subreddit: r/').lower()
    max_count = int(input('Enter the maximum number of entries to collect: '))

    # Generating the URL leading to the desired subreddit
    url = 'https://old.reddit.com/r/' + subreddit

    # Using a user-agent to mimic browser activity
    headers = {'User-Agent': 'Mozilla/5.0'}

    req = requests.get(url, headers=headers)

    if req.status_code == 200:
        # Parsing through the web page for obtaining the right html tags and
        # scraping the details required
        soup = BeautifulSoup(req.text, 'html.parser')
        print('\nCOLLECTING INFORMATION....')

        attrs = {'class': 'thing'}
        counter = 1
        full = 0
        reddit_info = []
        while 1:
            for post in soup.find_all('div', attrs=attrs):
                try:
                    title = post.find('a', class_='title').text

                    author = post.find('a', class_='author').text

                    time_stamp = post.time.attrs['title']

                    comments = post.find('a', class_='comments').text.split()[0]
                    if comments == 'comment':
                        comments = 0

                    upvotes = post.find('div', class_='score likes').text
                    if upvotes == '•':
                        upvotes = "None"

                    link = post.find('a', class_='title')['href']
                    link = 'www.reddit.com' + link

                    # Storing the scraped data in an array
                    reddit_info.append([title, author, time_stamp, upvotes,
                                        comments, link])

                    if counter == max_count:
                        full = 1
                        break

                    counter += 1
                except AttributeError:
                    continue

            if full:
                break

            try:
                # To go to the next page
                next_button = soup.find('span', class_='next-button')
                next_page_link = next_button.find('a').attrs['href']

                time.sleep(2)

                req = requests.get(next_page_link, headers=headers)
                soup = BeautifulSoup(req.text, 'html.parser')
            except:
                break

        # Writing the stored information in a .csv file
        print('DONE!\n')
        write_to_csv(reddit_info)

    else:
        print('Error fetching results.. Try again!')


if __name__ == '__main__':
    scraper()

