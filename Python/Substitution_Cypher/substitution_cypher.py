import string
import sys

all_letters = string.ascii_letters
i_a = {}
for i in range(0, len(all_letters)):
    i_a[i] = all_letters[i]
a_i = {}
for i in range(0, len(all_letters)):
    a_i[all_letters[i]] = i


def encrypt(text, key):
    enc_string = ""
    for i in range(0, len(text)):
        if text[i] == " ":
            enc_string = enc_string + " "
        elif text[i].isupper():
            enc_string = enc_string + i_a[(a_i[text[i].upper()] + key) % 26].upper()
        else:
            enc_string = enc_string + i_a[(a_i[text[i].upper()] + key) % 26].lower()
    return enc_string


def decrypt(enc_text, key):
    dec_string = ""
    for i in range(0, len(enc_text)):
        if enc_text[i] == " ":
            dec_string = dec_string + " "
        elif enc_text[i].isupper():
            dec_string = (
                dec_string + i_a[abs((a_i[enc_text[i].upper()] - key)) % 26].upper()
            )
        else:
            dec_string = (
                dec_string + i_a[abs((a_i[enc_text[i].upper()] - key)) % 26].lower()
            )
    return dec_string


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def try_again():

    retry = input("Do you want to try again. Enter 1 for yes and anything for no")
    if retry != "1":
        sys.exit()


if __name__ == "__main__":
    while True:
        while True:
            choice = input(
                "Do you want to encrypt or decrypt a text. press 0 for encrypt and 1 for decrypt\n"
            )
            if choice in ["0", "1"]:
                break
            else:
                print("Please enter only 0 or 1\n")
                try_again()
        if choice == "0":
            while True:
                text = input("Please enter a text you want to encrypt\n")
                if hasNumbers(text):
                    print("Only alphabets from A-Z or a-z are allowed")
                    try_again()
                else:
                    key = int(input("Please enter the key"))
                    if isinstance(key, int) is False:
                        print("Only integers are allowed for key")
                        try_again()
                    else:
                        print(encrypt(text, key))
                        break
        if choice == "1":
            while True:
                text = input("Please enter a text you want to decrypt\n")
                if hasNumbers(text):
                    print("Only alphabets from A-Z or a-z are allowed")
                    try_again()
                else:
                    key = int(input("Please enter the key"))
                    if isinstance(key, int) is False:
                        print("Only integers are allowed for key")
                        try_again()
                    else:
                        print(decrypt(text, key))
                        break

        try_again()
