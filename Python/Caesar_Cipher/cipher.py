"""
A Python Script to implement Caesar Cipher. The technique is really basic.
# It shifts every character by a certain number (Shift Key)
# This number is secret and only the sender, receiver knows it.
# Using Such a Key, the message can be easily decoded as well.

# This Script Focuses on Encryption Part
"""


def cipher(imput_string, shift_key):
    """
    Implementation of Crypto Technique.
            Params: input_string (required), shift_key (required)
            Returns: encrypted_string
            :type imput_string: str
            :type shift_key: int
    """
    # Initialise str to store the encrypted message
    encrypted_string = ""
    for text in imput_string:
        """
        There are 3 possibilities
        - Lower Case
        - Upper Case
        - Blank Space
        """
        if text == " ":
            # For Blank Space, encrypted as it is
            encrypted_string += text
        elif text.isupper():
            # For Upper Case
            encrypted_string = encrypted_string + chr(
                (ord(text) + shift_key - 65) % 26 + 65
            )
        else:
            # For Lower Case
            encrypted_string = encrypted_string + chr(
                (ord(text) + shift_key - 97) % 26 + 97
            )
    return encrypted_string


if __name__ == "__main__":
    """
    Function Calling
    """
    imput_string = input("Enter the text to be encrypted: ")
    shift = int(input("Enter the shift key: "))
    print("Text before Encryption: ", imput_string)
    print("Shift Key: ", shift)
    print("Encrypted text: ", cipher(imput_string, shift))
