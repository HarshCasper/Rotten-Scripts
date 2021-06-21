import cv2
import numpy as np


def watermarkLogo(pImg, pLogo):
    # importing the main image
    image = cv2.imread(pImg)
    oH, oW = image.shape[:2]
    image = np.dstack([image, np.ones((oH, oW), dtype="uint8") * 255])

    # importing the logo image
    lgo_img = cv2.imread(pLogo, cv2.IMREAD_UNCHANGED)

    # Resizing the image
    scl = 55
    w = int(lgo_img.shape[1] * scl / 100)
    h = int(lgo_img.shape[0] * scl / 100)
    dim = (w, h)
    lgo = cv2.resize(lgo_img, dim, interpolation=cv2.INTER_AREA)
    lH, lW = lgo.shape[:2]

    (B, G, R, A) = cv2.split(lgo)
    B = cv2.bitwise_and(B, B, mask=A)
    G = cv2.bitwise_and(G, G, mask=A)
    R = cv2.bitwise_and(R, R, mask=A)
    lgo = cv2.merge([B, G, R, A])

    # Blending
    ovr = np.zeros((oH, oW, 4), dtype="uint8")
    ovr[oH - lH - 0 : oH - 0, oW - lW - 0 : oW - 0] = lgo
    final = image.copy()
    final = cv2.addWeighted(ovr, 1, final, 1, 0)

    # Save the result
    cv2.imwrite("watermark.png", final)
    print("\nWatermark image saved.\n")


if __name__ == "__main__":
    pImg = input("Enter image path: ")
    pLogo = input("Enter logo image path: ")
    watermarkLogo(pImg, pLogo)
