import sys
from string import ascii_uppercase, ascii_lowercase


def rot_13(string):
    return ''.join([encrypt_char(c) for c in string])


def encrypt_char(c):
    lts = None
    if c in ascii_uppercase:
        ltrs = ascii_uppercase
    elif c in ascii_lowercase:
        ltrs = ascii_lowercase
    else:
        return c
    new_index = (ltrs.index(c) + 13) % 26
    return ltrs[new_index]


def exit_with_error():
    print('Usage: please provide a string to encrypt')
    sys.exit(1)


def main(args):
    try:
        string = args[0]
        if len(string) <= 0:
            exit_with_error()
        print(rot_13(string))
    except (IndexError, ValueError):
        exit_with_error()


if __name__ == "__main__":
    main(sys.argv[1:])
