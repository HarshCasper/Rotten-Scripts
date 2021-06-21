import pyautogui
from PIL import Image, ImageGrab
import time

# To check the obstacles
while True:
    image = ImageGrab.grab().convert("L")  # translating to greyscale (faster)
    data = image.load()

    # cactus
    for i in range(275, 325):
        for j in range(563, 650):
            data[i, j] = 0

    # bird
    for i in range(250, 300):
        for j in range(410, 563):
            data[i, j] = 200

    image.show()
    break
