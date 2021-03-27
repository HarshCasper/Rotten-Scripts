from PIL import ImageFont, ImageDraw, Image
from cv2 import cv2
import sys
import os

try:
    os.mkdir('outputs')
except FileExistsError:
    pass


def generate_image(img_no, author_name, blog_title):
    author = f'''By {author_name}'''
    margin = 10
    image = Image.open(f'raw_img/img{img_no}.jpg')
    width, height = image.size
    size = (width, height)
    draw = ImageDraw.Draw(image)
    font_title = ImageFont.truetype('arial.ttf', 280)
    textwidth_title, textheight_title = draw.textsize(blog_title, font_title)
    x_title = (width - textwidth_title)/2
    y_title = 350
    draw.text((x_title, y_title), blog_title, font=font_title)

    font_author = ImageFont.truetype('arial.ttf', 180)
    textwidth_author, textheight_author = draw.textsize(author, font_author)
    x_author = width - textwidth_author - margin
    y_author = height - textheight_author - margin
    draw.text((x_author, y_author), author, font=font_author)

    image.save(f'outputs/output{img_no}.jpg')


if __name__ == "__main__":
    generate_image(sys.argv[1], ' '.join(sys.argv[2:4]),
                   ' '.join(sys.argv[4:]).replace('/n', '\n'))
