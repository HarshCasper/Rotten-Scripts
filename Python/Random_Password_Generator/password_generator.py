from secrets import choice
from sys import argv
from string import ascii_lowercase, ascii_uppercase


def generate_password(password_size):
    # Creates one big string with all available characters
    # ' !"#...0123...ABC...xyz'
    numbers = '0123456789'
    symbols = ' !"#$%&\'()*+,-./:;<=>?@[\\^_`{|}'
    available_characters = numbers + symbols + ascii_lowercase + ascii_uppercase

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
    if len(argv) != 2:
        print('Usage: python3 password_generator.py password_length')
        print('Example: python3 password_generator.py 20')
    else:
        print(generate_password(int(argv[1])))
