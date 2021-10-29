import sys
import os
from PIL import Image

"""
method string_to_binary(string)
            - converts a string to a list with every character in a string as binary
"""


def string_to_binary(text):
    return [format(ord(i), "08b") for i in text]


"""
method encode(image)
            - the method takes parameter image
            - takes in a secret message from the user and embeds the text in the image
            - the technique used to do this is the called least significant bit changing
"""


def encode(img):
    secret_text = input("Enter the secret message: ")
    if len(secret_text) == 0:
        print("No text entered!!")
        return

    secret_text_binary = string_to_binary(secret_text)
    len_secret_text_binary = len(secret_text_binary)

    imdata = iter(img.getdata())
    changed_pixels = []

    for i in range(len_secret_text_binary):
        pixels = [
            value
            for value in imdata.__next__()[:3]
            + imdata.__next__()[:3]
            + imdata.__next__()[:3]
        ]

        letter = secret_text_binary[i]

        for j in range(len(letter) + 1):
            if j == 8:
                if i == len_secret_text_binary - 1:
                    if pixels[j] % 2 == 0:
                        pixels[j] += 1
                else:
                    if pixels[j] % 2 != 0:
                        pixels[j] -= 1
            elif int(letter[j]) == 0:
                if pixels[j] % 2 != 0:
                    pixels[j] -= 1
            elif int(letter[j]) == 1:
                if pixels[j] % 2 == 0:
                    pixels[j] += 1

        changed_pixels.append(tuple(pixels[0:3]))
        changed_pixels.append(tuple(pixels[3:6]))
        changed_pixels.append(tuple(pixels[6:9]))

    width = img.size[0]
    (x, y) = (0, 0)
    for pix in changed_pixels:
        img.putpixel((x, y), pix)
        if x == width - 1:
            x = 0
            y += 1
        else:
            x += 1

    new_img_name = input("Enter the name of new image(with extension png) : ")
    img.save(new_img_name)


"""
method decode(image)
            - takes parameter an image
            - decrypts the hidden message from the image which uses LSB to hide text.
"""


def decode(image):
    message = ""
    imgdata = iter(image.getdata())

    while True:
        pixels = [
            value
            for value in imgdata.__next__()[:3]
            + imgdata.__next__()[:3]
            + imgdata.__next__()[:3]
        ]
        binstr = ""
        for i in pixels[:8]:
            if i % 2 == 0:
                binstr += "0"
            else:
                binstr += "1"

        message += chr(int(binstr, 2))
        if pixels[-1] % 2 != 0:
            print(message)
            return


if __name__ == "__main__":
    operation = sys.argv[1]
    img_path = " ".join(sys.argv[2:])
    if operation == "encode":
        image = Image.open(img_path)
        new_image = image.copy()
        encode(new_image)
    elif operation == "decode":
        image = Image.open(img_path)
        new_img = image.copy()
        decode(new_img)
    else:
        print("Invalid input")
