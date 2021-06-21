from PIL import Image, ImageDraw, ImageFont


def watermarkText(path, text):
    # Create an Image Object from an Image
    img = Image.open(path)
    width, height = img.size

    draw = ImageDraw.Draw(img)

    # font needs to be downloaded and use the dir of it as argument
    font = ImageFont.truetype("JMH Typewriter-Thin.ttf", 50)

    textwidth, textheight = draw.textsize(text, font=font)

    # calculate the x,y coordinates of the text
    margin = 5
    x = width - textwidth - margin
    y = height - textheight - margin

    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font, fill="white")

    # Save watermarked image
    img.save("watermark.png")
    print("\nWatermark image saved.\n")


if __name__ == "__main__":
    path = input("Enter image path: ")
    text = input("Enter text: ")
    watermarkText(path, text)
