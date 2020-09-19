# This script is capable of converting some special/secret text
# into 64 BASE Encoded String

# importing base64

import base64
import argparse
parser = argparse.ArgumentParser(description='String Encode and Decode')
parser.add_argument('string', help='Enter String to encode')
args = parser.parse_args()


def ConvertToBase64(string):

    # encoding the string to base64
    print("Encoded String:")
    string = base64.b64encode(string.encode('utf-8'))
    print(string)

    # decoding the string to base64
    print("Want to decode(Y/N):")
    choice = input()
    if(choice == 'y' or choice == 'Y'):
        print("Decoded String:")

        # decoding the given string
        string = base64.b64decode(string).decode('utf-8')
        print(string)
    else:
        print("String Encoded")

if __name__ == '__main__':
    ConvertToBase64(args.string)
