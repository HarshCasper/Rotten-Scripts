# Image_Sketch

Using this script, users can convert images to corresponding pencil sketches. The script uses OpenCV.

## Steps

Using OpenCV and Python, an RGB color image can be converted into a pencil sketch in four simple steps:

1. Convert the RGB color image to grayscale.
2. Invert the grayscale image to get a negative.
3. Apply a Gaussian blur to the negative from step 2.
4. Blend the grayscale image from step 1 with the blurred negative from step 3 using a color dodge.

## Input

![](https://i.imgur.com/psq5aL2.jpg)

## Output

- Step 1: Get the image and convert it into grayscale by using COLOR_BGR2GRAY from cv2.

![](https://i.imgur.com/UMe8Ll8.jpg)

- Step 2: Invert the image i.e, obtain the negative of the grayscale image using bitwise_not from cv2.
![](https://i.imgur.com/l66ycT6.jpg)

- Step 3: Blur the image by applying Gaussian filter to the inverted image.
![](https://i.imgur.com/H4En933.jpg)

- Step 4: Merge the gray scale image and the Gaussian filter applied image.
![](https://i.imgur.com/yAYRiCK.jpg)

__The sketch is ready!__
