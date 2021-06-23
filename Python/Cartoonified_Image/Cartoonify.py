import cv2
import numpy as np
from skimage import io

# Class Defination


class Cartoon:
    def __init__(self):
        img = io.imread("original_image.jpg")
        # 1) Edges
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 7
        )

        # 2) Color
        color = cv2.bilateralFilter(img, 10, 300, 300)
        RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # 3) Cartoon
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        cartoon_img = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)
        cartoon_image = cv2.stylization(RGB_img, sigma_s=150, sigma_r=0.25)

        # Re-sizeing
        resize1 = cv2.resize(RGB_img, (600, 450))
        resize2 = cv2.resize(cartoon_img, (600, 450))
        resize3 = cv2.resize(cartoon_image, (600, 450))
        self.resize1 = resize1
        self.resize2 = resize2
        self.resize3 = resize3


# Displaying
c1 = Cartoon()
c1.resize1
c1.resize2
c1.resize3
cv2.imshow("original_image", c1.resize1)
cv2.imshow("cartoonified_image", c1.resize2)
cv2.imshow("cartoonified_image_2", c1.resize3)
cv2.waitKey(0)
cv2.destroyAllWindows()
