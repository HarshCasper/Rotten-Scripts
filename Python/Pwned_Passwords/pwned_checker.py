import requests
import hashlib
from decouple import config


def send_request(start_char):
    """
    The function sends a request to the API with the URL containing
    first 5 characters of the hashed password
    """
    # Concatenating first 5 characters of hashed password to the URL
    url = 'https://api.pwnedpasswords.com/range/' + start_char
    try:
        res = requests.get(url)

        # Only status code of 200 includes all password hashes beginning
        # with the starting characters alongside its prevalent counts
        if res.status_code != 200:
            print('\nError fetching results!!!')
            return 0

        return res

    except:
        print('\nConnection Error!!!')
        return 0


def get_count(res, suffix):
    """
    Function to get the count of the number of times the partial hash of the
    password appears in the dataset of breached passwords
    """
    # The data has a ':' delimiter separating the hashed password and its count
    results = (line.split(':') for line in res.text.splitlines())

    for hashed, count in results:
        # Checking if there is a match for the last 5 characters
        # the resultant tuple
        if hashed == suffix:
            return count

    return 0


def password_hashing(password):
    """
    Function to generate the SHA-1 hash of a UTF-8 encoded password
    """
    sha1pass = hashlib.sha1(password.encode('utf -8')).hexdigest().upper()

    # Inorder to maintain anonymity, storing only the partial hash for searching
    head, tail = sha1pass[:5], sha1pass[5:]
    return head, tail


print('\n\n\t------ !!CHECK IF YOUR PASSWORD IS SAFE!! ------')
print('Reading your password from the .env file and fetching results...')

password = config("PASSWORD")
start, end = password_hashing(password)

res = send_request(start)

if res:
    num = get_count(res, end)

    if num:
        print(f'\nYour password was found {num} many times in the dataset,'
              f' it is recommended to change it ASAP!')
    else:
        print(f'\nYour password was not found in the dataset. '
              f'You have a safe password!')


