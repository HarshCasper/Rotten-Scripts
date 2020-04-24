import requests
import os

# Variables
directory_name = "MSFT Books"
links_list_url = 'http://ligman.me/2sZVmcG'  # URL that contains url of all the books
print_status = True  # Print the current status of the script

# Create a directory
if not os.path.exists(directory_name):
    os.makedirs(directory_name)
    if print_status:
        print("{} was successfully created.".format(directory_name))

initial_response = requests.get(links_list_url)  # Requesting the list of links
loop = list(initial_response.iter_lines(decode_unicode=True))
# Creates a list of all the links using the the iter_lines method of the Response class (from Requests)

for url in loop[1:]:
    response = requests.get(url)
    book_name = response.url.split("/")[-1]  # Last part of the url is the title of the book

    with open('{}/{}'.format(directory_name, book_name), 'wb') as bin_file:  # Writing the file using open function
        bin_file.write(response.content)

    if print_status:
        print("{} was downloaded.".format(book_name))
