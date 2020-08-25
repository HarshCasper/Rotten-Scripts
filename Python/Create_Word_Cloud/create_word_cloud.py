import argparse
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--text', action='store', type=str, required=True, help="Enter the path to the text file")
my_parser.add_argument('--background', action='store', type=str, required=False, help="Enter a background color of your choice")
my_parser.add_argument('--mask', action='store', type=str, required=False, help="Enter the path to a mask of your choice")
my_parser.add_argument('--contour_width', action='store', type=int, required=False, help="Enter the width of the contour you prefer")
my_parser.add_argument('--contour_color', action='store', type=str, required=False, help="Enter the color of the contour you prefer")
my_parser.add_argument('--color_func', action='store', type=bool, required=False, help="Do you want the color of the mask intact?")

def createWordCloud (text, background_color, mask, contour_width, contour_color, color_func):
    print(text, background_color, mask, contour_color, color_func)
    name = text.split('.')[0]
    text = open(text).read()
    mask = np.array(Image.open(mask))
    if (color_func is not None):
        mask_colors = ImageColorGenerator(mask)
    else:
        mask_colors = None
    wordcloud = WordCloud(stopwords=STOPWORDS, mask=mask, max_font_size=50, 
                            max_words=1000, background_color=background_color, color_func=mask_colors,
                            contour_width=contour_width, contour_color=contour_color).generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    wordcloud.to_file(name+'.png')

args = my_parser.parse_args()
text = args.text
background_color = args.background
mask = args.mask
contour_width = args.contour_width
contour_color = args.contour_color
color_func = args.color_func
createWordCloud(text, background_color, mask, contour_width, contour_color, color_func)