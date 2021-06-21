import cv2
import pandas as pd
import argparse


def get_argument():
    """
    This function returns the arguement which was passed through the terminal.
    """
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True)

    args = vars(ap.parse_args())
    return args


def get_img():
    """
    This function returns the img whose path is passed by us through terminal.
    """
    args = get_argument()
    img_path = args["image"]
    img = cv2.imread(img_path)
    return img


def read_color():
    """
    This function returns csv file which contains the name of the color with its RGB value.
    """
    index = ["color", "color_name", "hex", "R", "G", "B"]
    csv = pd.read_csv("colors.csv", names=index)
    return csv


clicked = False
blue = green = red = 0


# following code finds the closest colour to the clicked
def getColor(R, G, B):
    """
    This function returns the color name after comparing it with the csv file .
    """
    minimum = 1000
    csv = read_color()
    for i in range(len(csv)):
        # these below formula d is  absolute sum of the  differencr of (rgb value clicked on and the rgb value in csv file)
        d = abs(R - int(csv.loc[i, "R"]))
        d = d + abs(G - int(csv.loc[i, "G"]))
        d = d + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname


# This functionis called when we click on the point on the image
def click_event(event, x, y, flags, param):
    """
    This function is called when clicked on the image and here the value of the basic color is find using coordinates.
    """
    # LBUTTONDBCLICK is refering left click on mouse
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global clicked, blue, red, green
        clicked = True
        img = get_img()
        blue = int(img[y, x, 0])
        green = int(img[y, x, 1])
        red = int(img[y, x, 2])


def main():
    """
    This is the main function where all other function are put together to make it work.
    """
    global clicked
    img = get_img()
    while True:
        cv2.imshow("image", img)
        if clicked:
            # The following is the inbulit opencv function that forms the rectangle.
            cv2.rectangle(img, (20, 20), (750, 60), (blue, green, red), -1)
            text = getColor(red, green, blue)
            # The following is the inbulit opencv function that print text.
            cv2.putText(
                img,
                text + "[" + str(blue) + "," + str(green) + "," + str(red) + "]",
                (50, 50),
                2,
                0.8,
                (0, 0, 0),
                2,
                cv2.LINE_AA,
            )
            clicked = False
        # to quit the window click q
        if cv2.waitKey(1) == ord("q"):
            break

    cv2.destroyAllWindows()


cv2.namedWindow("image")
cv2.setMouseCallback("image", click_event)


if __name__ == "__main__":
    main()
