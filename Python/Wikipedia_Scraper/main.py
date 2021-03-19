from bs4 import BeautifulSoup
import requests


def get_player_name():
    """ Takes Football player's name input from the user and
    returns a string suitable to concatenate in the wikipedia URL. """

    player = input('Enter the name of the Football player: ').split(' ')
    player_name = ''
    for i in player:
        name = i.capitalize()
        player_name += name
        player_name += ' '

    return player_name


def get_club_info(headers):
    """ Stores only the information regarding the club career of
    a player among all the titles in the contents box. """

    # For storing the club data
    club_data = []

    try:
        start = None
        for i in range(len(headers)):
            each = headers[i].getText()
            if each == "Club career":
                start = i + 1
                break

        while headers[start].getText() != 'International career':
            club_data.append(headers[start].getText())
            start += 1

        return club_data

    # In case the name given is not a Football player
    except TypeError:
        print('INVALID PLAYER NAME!!')
        return 0


def display_info(club_data):
    """ To display the club career information of player collected. """

    for item in club_data:
        if item[:4].isdigit():
            print(f'    {item}')
        else:
            print()
            print(f'CLUB NAME: {item}')


def main():
    print()
    print('WELCOME!!!HERE YOU CAN GET THE CLUB CAREER INFORMATION'
          ' REGARDING YOUR FAVOURITE FOOTBALL PLAYER FROM WIKIPEDIA!')
    while True:
        print()
        name = get_player_name()

        # Concatenating the Football players name to the wikipedia URL
        # to send a GET request
        req = requests.get('https://en.wikipedia.org/wiki/' + name)

        if req.status_code == 200:

            # BeautifulSoup object for parsing through the html text
            soup = BeautifulSoup(req.text, 'html.parser')

            # Searching for the content box with css selector '.mw-headline'
            titles = soup.select('.mw-headline')

            # collecting info regarding club career only
            club_info = get_club_info(titles)

            if club_info:
                # For presenting the collected information
                display_info(club_info)

            print()
            key = input('Press "y" to continue or any other key to quit: ').lower()
            if key != 'y':
                break

        else:
            print('URL NOT FOUND!!')

            print()
            key = input('Press "y" to continue or any other key to quit: ').lower()
            if key != 'y':
                break


if __name__ == '__main__':
    main()

