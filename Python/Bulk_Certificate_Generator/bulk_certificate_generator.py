__author__ = 'Sri Manikanta Palakollu'
__date__ = '27-07-2020'

from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import random

# y_coordinate = 1020
y_coordinate = int(input('Enter the Y-cordinate value to write the name: '))
template_name = input("Enter your custom template name: ")
data_file = input('Enter your names file name: ')

try:
    df = pd.read_excel('data/{}'.format(data_file))
    names = list(df['Name'].values)
except ValueError:
    print("There is a value error in the Dataframe please check the value")

try:
    for name in names:

        certificateId = "SICET" + str(random.randint(45765654, 99765957))
        name = name.rstrip()

        # Change the certificate name According to yours
        img = Image.open("Certificate_Template/{}".format(template_name))
        width, height = img.size
        draw = ImageDraw.Draw(img)

        # Customize the Font Size based on your requirement.
        font = ImageFont.truetype("Fonts/BirdsOfParadise.ttf", 200)
        offset = 20
        x_coordinate = int(width / 2 - font.getsize(name)[0] / 2) + offset
        draw.text((x_coordinate, y_coordinate), name, (238, 33, 33), font=font)
        id_font = ImageFont.truetype("Fonts/lesser_concern.ttf", 90)
        draw.text((190, 2250), "ID: ", (0, 0, 0), font=id_font)

        # Writing the Certificate Id
        draw.text((290, 2250), certificateId, (0, 0, 0), font=id_font)

        # Signature Content
        draw.text((1500, 2250), "Hackathon Intiator", (0, 0, 0), font=id_font)
        img.save("Certificates/" + str(name.replace(" ", "_")) + ".jpg")
        print("Certificate Created for {}".format(name))
except Exception:
    print('Something went wrong.!')
