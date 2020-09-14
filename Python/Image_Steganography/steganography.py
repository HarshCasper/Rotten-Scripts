import sys
import os
from PIL import Image

def string_to_binary(text):
    return [format(ord(i), '08b') for i in text]

def encode(img):
    secret_text = input('Enter the secret message: ')
    if(len(secret_text)==0):
        print('No text entered!!')
        return

    secret_text_binary = string_to_binary(secret_text)
    len_secret_text_binary = len(secret_text_binary)

    imdata = iter(img.getdata())
    changed_pixels = list()

    for i in range(len_secret_text_binary):
        pix = [value for value in imdata.__next__()[:3] +
                                  imdata.__next__()[:3] +
                                  imdata.__next__()[:3]]
        for j in range(0,8):
            if (secret_text_binary[i][j] == '0' and pix[j]% 2 != 0):
                pix[j] -= 1
            elif (secret_text_binary[i][j] == '1' and pix[j] % 2 == 0):
                if(pix[j] == 0):
                    pix[j] += 1
                else:
                    pix[j] -= 1

        if (i == len_secret_text_binary - 1):
            if (pix[-1] % 2 == 0):
                if(pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1

        changed_pixels.append(tuple(pix[0:3]))
        changed_pixels.append(tuple(pix[3:6]))
        changed_pixels.append(tuple(pix[6:9]))

    index = 0
    for i in img.getdata():
        i = changed_pixels[index];
        index += 1
        if index == len(changed_pixels)-1:
            break

    img.save(input("Enter the encoded image name(with extension): "))

def decode(img_path):
    message = ""
    imgdata = iter(image.getdata())
    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                                     imgdata.__next__()[:3] +
                                     imgdata.__next__()[:3]]
        binstr = ''
        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'

        message += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            print(message)

if __name__ == '__main__' :
    operation = sys.argv[1]
    img_path = " ".join(sys.argv[2:])
    if(operation == 'encode'):
        image = Image.open(img_path)
        new_image = image.copy()
        encode(new_image)
    elif(operation == 'decode'):
        image = Image.open(img_path)
        decode(image)
    else:
        print('Invalid input')
