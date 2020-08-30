from secrets import choice
from sys import argv
import string


def generate_password(password_size):
    # Converts to list a big string that contains all available characters
    # so ' !"# ... ABC ... xyz' becomes [' ', '!', '"', ..., 'z']
    available_characters = list(
        ' !"#$%&\'()*+,-./:;<=>?@[\\^_`{|}~' +
        string.ascii_lowercase +
        string.ascii_uppercase
    )

    # Iterate password_size times, each time taking a new random character
    # from our list of available_characters
    password = ''
    for i in range(password_size):
        password += choice(available_characters)

    return password


if __name__ == '__main__':
    # Tries to generate a password with argv[1] length. Remember that
    # argv[0] is the program name (password_generator) and argv[1] is
    # the length of the password which the user wants to generate.
    try:
        print(generate_password(int(argv[1])))
    except IndexError:
        print('Correct usage: python3 password_generator.py password_length')
        print('Example: python3 password_generator.py 20')
