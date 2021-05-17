# CONVERTING IMAGE TO PENCIL SKETCH

### A RGB image can be converted into a pencil sketch using 4 easy steps!

![](https://i.imgur.com/psq5aL2.jpg)

### Step 1: Get the image and convert it into grayscale by using COLOR_BGR2GRAY from cv2.
![](https://i.imgur.com/UMe8Ll8.jpg)

### Step 2: Invert the image i.e, obtain the negative of the grayscale image using bitwise_not from cv2.
![](https://i.imgur.com/l66ycT6.jpg)

### Step 3: Blur the image by applying Gaussian filter to the inverted image.
![](https://i.imgur.com/H4En933.jpg)

### Step 4: Merge the gray scale image and the Gaussian filter applied image.
![](https://i.imgur.com/yAYRiCK.jpg)

### The sketch is ready!
