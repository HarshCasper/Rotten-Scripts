import sys
from PIL import Image, ImageDraw

"""
A grayscale pixel value is converted into one of these special characters 
"""
ASCII_SET = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

"""
method resize()
            - takes parameter image and new_width
            - resizes the image into new_width maintaining the aspect aspect_ratio
            - returns this resized image, new width and new height
"""


def resize(image, new_width=100):
    (old_width, old_height) = image.size
    aspect_ratio = old_height / old_width
    new_height = int(aspect_ratio * new_width)
    new_image = image.resize((new_width, new_height))
    return new_image, new_width, new_height


"""
method convertToGray()
            - takes parameter image
            - returns converted grayscale image
"""


def convertToGray(image):
    return image.convert("L")


"""
method PixelToAscii()
            - takes parameter image
            - returns a string with all image pixels converted to ascii special symbols from ASCII_SET
"""


def PixelToAscii(image, buckets=25):
    pixels = list(image.getdata())
    new_pixels = [ASCII_SET[pixel_value // buckets] for pixel_value in pixels]
    return "".join(new_pixels)


"""
method saveImage()
            - takes parameter string, new width and new height
            - writes the string in an image and saves the image as image.png
"""


def saveImage(ascii_str, new_width, new_height):
    image = Image.new(mode="RGB", size=(new_width * 11, new_height * 11), color="white")
    draw = ImageDraw.Draw(image)
    draw.multiline_text((0, 0), ascii_str, fill=(0, 0, 0), align="center", spacing=0)
    image.save("image.png")


"""
method asciify()
            - takes parameter image path
            - calls the required functions to asciify the image
"""


def asciify(img_path):
    try:
        image = Image.open(img_path)
    except Exception:
        print("Unable to find image in", img_path)
        return
    image, new_width, new_height = resize(image)
    gray_image = convertToGray(image)
    ascii_char_list = PixelToAscii(gray_image)

    len_ascii_list = len(ascii_char_list)
    ascii_str = ""
    ascii_str = "".join([ascii_str + i + i for i in ascii_char_list])

    ascii_str = [
        ascii_str[index : index + 2 * new_width]
        for index in range(0, 2 * len_ascii_list, 2 * new_width)
    ]
    ascii_str = "\n".join(ascii_str)

    saveImage(ascii_str, new_width, new_height)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        img_path = str(" ".join(sys.argv[1:]))
    asciify(img_path)
