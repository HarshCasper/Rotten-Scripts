from cv2 import cv2
import sys


def capture(path):
    video = cv2.VideoCapture(path)
    count = 0
    while video.isOpened():
        sucess, frame = video.read()
        if sucess is False:
            break
        # This part of function actually saves the images.
        cv2.imwrite("frame" + str(count) + ".jpg", frame)
        count += 1

    video.release()


if __name__ == "__main__":
    capture(sys.argv[1])
