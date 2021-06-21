# Importing Necessary projects
import cv2
import numpy as np

# Creating the video capture object
cap = cv2.VideoCapture(0)

# Defining upper and lower ranges for yellow color
# If you don't have a yellow marker feel free to change the RGB values

Lower = np.array([20, 100, 100])
Upper = np.array([30, 255, 255])

# Defining kernel for Morphological operators
kernel = np.ones((5, 5), np.uint8)
# Defining starting point
x0, y0 = -1, -1


# Creating an empty image / white background with the same frame size
temp = np.ones((480, 640, 3), dtype=np.uint8)
temp = temp * 255

while True:
    ret, frame = cap.read()
    s = frame.shape
    # Flipping for mirror image
    frame = cv2.flip(frame, 1)
    # Getting a hsv version of the frame for easy colour detection and locating the mask
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, Lower, Upper)
    # Performing morphological operators
    mask = cv2.erode(mask, kernel, iterations=2)
    final = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    final = cv2.dilate(mask, kernel, iterations=1)

    # Finding contours in the mask
    contours, _ = cv2.findContours(final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # Getting the largest contours assuming it would be the object of interest
    if contours:
        cnt = max(contours, key=cv2.contourArea)
        x, y, width, height = cv2.boundingRect(cnt)

        if x0 == -1:
            x0, y0 = x + width // 2, y + height // 2
        else:
            # Drawing on the temporary masked image
            temp = cv2.line(
                temp, (x0, y0), (x + width // 2, y + height // 2), (0, 0, 255), 5
            )
            # To track can be removed if necessary
            frame = cv2.line(
                frame, (x0, y0), (x + width // 2, y + height // 2), (255, 255, 255), 5
            )
            x0, y0 = x + width // 2, y + height // 2
    else:
        x0, y0 = -1, -1

    # Operations using bitwise functions for the written stuff on the Result image
    # BLACK FOREGROUND AND WHITE BACKGROUND
    temp_gray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
    # WHITE FOREGROUND AND BLACK BACKGROUND
    temp_gray_inv = cv2.bitwise_not(temp_gray)
    # Plain white background
    white_background = np.full(temp.shape, 255, dtype=np.uint8)
    bk = cv2.bitwise_or(white_background, white_background, mask=temp_gray_inv)
    # 3 channeled temp_gray_inv
    fg = cv2.bitwise_or(temp, temp, mask=temp_gray_inv)
    # Red foreground and black background
    Result = cv2.bitwise_or(frame, fg)

    cv2.imshow("Result", Result)
    # To end the program
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()
