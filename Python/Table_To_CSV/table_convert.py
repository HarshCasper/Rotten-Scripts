import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import re
import keyboard

from PIL import Image

import pytesseract

# Path to Tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r''

# Path to Input File
file = r''
img = cv2.imread(file, 0)
img.shape

# Adaptive thresholding for the image to a binary image
img_bin = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# inverting the image
img_bin = 255 - img_bin
cv2.imwrite(file+'cv_inverted.png', img_bin)
# Plotting the image to see the output
plotting = plt.imshow(img_bin, cmap='gray')


# Grid Detection
# countcol(width) of kernel as 100th of total width
kernel_len = np.array(img).shape[1] // 100
# Vertical Line Kernel
ver_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_len))
# Horizontal Line Kernel
hor_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_len, 1))
# A kernel of 2x2
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

# Vertical Line Detection
image_1 = cv2.erode(img_bin, ver_kernel, iterations=3)
vertical_lines = cv2.dilate(image_1, ver_kernel, iterations=3)
cv2.imwrite(file+"vertical.jpg", vertical_lines)


# Horizontal Line Detection
image_2 = cv2.erode(img_bin, hor_kernel, iterations=3)
horizontal_lines = cv2.dilate(image_2, hor_kernel, iterations=3)
cv2.imwrite(file+"horizontal.jpg", horizontal_lines)

# Grid Generation
img_vh = cv2.addWeighted(vertical_lines, 0.5, horizontal_lines, 0.5, 0.0)
# Eroding and thresholding the image
img_vh = cv2.erode(~img_vh, kernel, iterations=2)
thresh, img_vh = cv2.threshold(img_vh, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imwrite(file+"img_vh.jpg", img_vh)
bitxor = cv2.bitwise_xor(img, img_vh)
bitnot = cv2.bitwise_not(bitxor)


# Detect contours
contours, hierarchy = cv2.findContours(img_vh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


# Cell Detection
def sort_contours(cnts, method="left-to-right"):
    # initialize flags and index variable
    reverse = False
    i = 0
    # Handle Method "Keep at default"
    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True
    # Choosing the Axis of sorting the cells
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1
    # A list of boxes
    bounding_boxes = [cv2.boundingRect(count) for count in cnts]
    (cnts, bounding_boxes) = zip(*sorted(zip(cnts, bounding_boxes),
                                         key=lambda b: b[1][i], reverse=reverse))
    # return the list of sorted contours and bounding boxes
    return cnts, bounding_boxes


# Sorting the generated grid
contours, boundingBoxes = sort_contours(contours, method="top-to-bottom")

# Total height
heights = [boundingBoxes[i][3] for i in range(len(boundingBoxes))]

# Mean Height (for equally weighted cells)
mean = np.mean(heights)

# Empty List to Store boxes
box = []
# Coordinates of every box
for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    if w < 1000 and h < 500:
        image = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        box.append([x, y, w, h])


# Creating two lists to define row and column in which cell is located
row = []
column = []
j = 0

# Sorting the boxes to their respective row and column
for i in range(len(box)):

    if i == 0:
        column.append(box[i])
        previous = box[i]

    else:
        if box[i][1] <= previous[1] + mean / 2:
            column.append(box[i])
            previous = box[i]

            if i == len(box) - 1:
                row.append(column)

        else:
            row.append(column)
            column = []
            previous = box[i]
            column.append(box[i])
# print(column)
# print(row)

# calculating maximum number of cells
countcol = 0
for i in range(len(row)):
    countcol = len(row[i])
    if countcol > countcol:
        countcol = countcol

# Retrieving the center of each column
center = [int(row[i][j][0] + row[i][j][2] / 2) for j in range(len(row[i])) if row[0]]

center = np.array(center)
center.sort()
print(center)
# Regarding the distance to the columns center, the boxes are arranged in respective order

finalboxes = []
for i in range(len(row)):
    lis = []
    for k in range(countcol):
        lis.append([])
    for j in range(len(row[i])):
        diff = abs(center - (row[i][j][0] + row[i][j][2] / 4))
        minimum = min(diff)
        indexing = list(diff).index(minimum)
        lis[indexing].append(row[i][j])
    finalboxes.append(lis)

# from every single image-based cell/box the strings are extracted via pytesseract and stored in a list
outer = []
for i in range(len(finalboxes)):
    for j in range(len(finalboxes[i])):
        inner = ''
        if len(finalboxes[i][j]) == 0:
            outer.append(' ')
        else:
            for k in range(len(finalboxes[i][j])):
                y, x, w, h = finalboxes[i][j][k][0], finalboxes[i][j][k][1], finalboxes[i][j][k][2], \
                             finalboxes[i][j][k][3]
                finalimg = bitnot[x:x + h, y:y + w]
                kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 1))
                border = cv2.copyMakeBorder(finalimg, 2, 2, 2, 2, cv2.BORDER_CONSTANT, value=[255, 255])
                resizing = cv2.resize(border, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
                dilation = cv2.dilate(resizing, kernel, iterations=1)
                erosion = cv2.erode(dilation, kernel, iterations=2)

                out = pytesseract.image_to_string(erosion)
                if len(out) == 0:
                    out = pytesseract.image_to_string(erosion, config='--psm 3')
                inner = inner + " " + out
            outer.append(inner)

# Creating a dataframe of the generated OCR list
arr = np.array(outer)
dataframe = pd.DataFrame(arr.reshape(len(row), countcol))
print(dataframe)
print("Ready to Convert the Img File\n Do you want a csv file or excel file?\n "
      "\tPress [x] for Excel.\n"
      "\tPress [c] for csv.\n")
while True:
    if keyboard.read_key() == "x":

        data = dataframe.replace(r'\n', '', regex=True)
        data = data.style.set_properties(align="left")
        # Converting it in a excel-file
        ILLEGAL_CHARACTERS_RE = re.compile(r'[\000-\010]|[\013-\014]|[\016-\037]')
        data = data.applymap(lambda x: ILLEGAL_CHARACTERS_RE.sub(r'', x) if isinstance(x, str) else x)
        # Converting it in a excel-file
        print(data)
        # Change the Path to the destination
        writer = pd.ExcelWriter(file+'excel.xlsx',
                                engine='xlsxwriter',
                                options={'strings_to_numbers': True},
                                )
        data.to_excel(writer, encoding="utf-8")
        writer.save()
        print("Thank You\n")
        break
    elif keyboard.read_key() == "c":
        data = dataframe.replace(r'\n', '', regex=True)
        # Converting it in a excel-file
        ILLEGAL_CHARACTERS_RE = re.compile(r'[\000-\010]|[\013-\014]|[\016-\037]')
        data = data.applymap(lambda x: ILLEGAL_CHARACTERS_RE.sub(r'', x) if isinstance(x, str) else x)
        # Converting it in a excel-file
        print(data)
        # Change the Path to the destination
        data.to_csv(file+'csv.csv', encoding="utf-8")
        print("Thank You\n")
        break
    else:
        print("Nothing!!!\n")
        break

