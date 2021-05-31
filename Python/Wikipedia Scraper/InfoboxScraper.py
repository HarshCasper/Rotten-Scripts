from bs4 import BeautifulSoup
import requests

BOLD = '\033[1m'
END = '\033[0m'

def get_data(req):
    """
    The function will scrape the infobox using BeautifulSoup's parser
    and gather the information to display.
    """
    # Dictionary to store the collected information
    info_dict = {} 

    # Initializing html parsing object of BeautifulSoup
    soup = BeautifulSoup(req.text, 'html.parser')

    # Finding the infobox class
    info_table = soup.find('table', {'class': 'infobox'})

    # Gathering all the text fields within the infobox
    for tr in info_table.find_all('tr'):
        try:
            if tr.find('th'):
                info_dict[tr.find('th').text] = tr.find('td').text

        except AttributeError:
            pass
    
    # Presenting the information in the command line
    for x, y in info_dict.items():
        print('\n{}{}{} : \n{}'.format(BOLD, x, END, y))


def main():
    """
    The main function takes the user input search query and generates the URL
    to scrape accordingly.
    """
    while 1:
        # Taking user input 
        entry = input('\nEnter your search query: ')
        
        # Formatting the input suitable for the URL
        entry = entry.split()
        query = ' '.join([i.capitalize() for i in entry])

        try:
            # Generating the URL and making the request
            req = requests.get('https://en.wikipedia.org/wiki/'+query)

            if req.status_code == 200:
                get_data(req)

            else:
                print('\nInvalid URL!')
        except:
            print('\nCONNECTION ERROR! TRY AGAIN')

        cont = input('\nWould you like to continue?\nPress (y/n): ')
        if cont == 'n':
            break


if __name__ == '__main__':
    main()

