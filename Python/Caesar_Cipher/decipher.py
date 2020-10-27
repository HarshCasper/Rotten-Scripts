"""
A Python Script to implement Caesar Cipher. The technique is really basic.
# It shifts every character by a certain number (Shift Key)
# This number is secret and only the sender, receiver knows it.
# Using Such a Key, the message can be easily decoded as well.
# This Script Focuses on the Decoding Part only.
"""


def decipher(encrypt_string, shift_key):
    """
    Implementation of DeCipher Technique.
            Params: encrypt_string (required), shift_key (required)
            Returns: decrypted_string
    """
    # Initialise str to store the decrypted message
    decrypted_string = ''
    for text in encrypt_string:
        if text == ' ':
            # For Blank Space, encrypted as it is
            decrypted_string += text
        elif text.isupper():
            # For Upper Case
            decrypted_string = decrypted_string + chr((ord(text) - shift_key - 65) % 26 + 65)
        else:
            # For Lower Case
            decrypted_string = decrypted_string + chr((ord(text) - shift_key - 97) % 26 + 97)
    return decrypted_string


if __name__ == "__main__":
    """
    Function Calling
    """
    encrypted_string = input('Enter the text to be decrypted: ')
    shift = int(input('Enter the shift key: '))
    print('Text before Decryption: ', encrypted_string)
    print('Shift Key: ', shift)
    print('Decrypted text: ', decipher(encrypted_string, shift))

"""
Sample Output-
Enter the text to be decrypted: Rfshmjxyjw nx GQZJ
Enter the shift key: 5
Text before Decryption:  Rfshmjxyjw nx GQZJ
Shift Key:  5
Decrypted text:  Manchester is BLUE
"""