"""
    SIFT(Scale Invariant Feature Transform) Algorithm for the feature detection.
    This algorithm is patented, so this algorithm is included in the Non-free module in OpenCV.
"""

# Importing required libraries
import cv2
import numpy as np


def siftAlgorithm():
    """
    Take input of image and create a test image from it
    Implement SIFT Algorithm for feature extraction from image and after that
    Implement Brute Force Matcher Algorithm for matching the features of input and test image.
    Diplay the matching result and feature extraction image.
    """
    # Load the image
    path = input("Enter the path of the image: ")
    image = cv2.imread(path)

    # Create test image by adding Scale Invariance and Rotational Invariance
    test_image = cv2.pyrDown(image)
    test_image = cv2.pyrDown(test_image)
    num_rows, num_cols = test_image.shape[:2]

    rotation_matrix = cv2.getRotationMatrix2D((num_cols / 2, num_rows / 2), 30, 1)
    test_image = cv2.warpAffine(test_image, rotation_matrix, (num_cols, num_rows))

    # Resizing the image
    image = cv2.resize(image, (400, 400))
    test_image = cv2.resize(test_image, (400, 400))

    # Convert the image to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    test_gray = cv2.cvtColor(test_image, cv2.COLOR_RGB2GRAY)

    # Display the given and test image
    image_stack = np.concatenate((image, test_image), axis=1)
    cv2.imshow("Input VS Test image", image_stack)

    # Detect keypoints and Create Descriptor
    sift = cv2.xfeatures2d.SIFT_create()

    kp, dp = sift.detectAndCompute(gray, None)
    test_kp, test_dp = sift.detectAndCompute(test_gray, None)

    img = cv2.drawKeypoints(gray, kp, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Print the number of keypoints detected in the image
    print("Number of Keypoints Detected In The Image: ", len(kp))

    # Display the feature detected image
    image_name = path.split(r"/")
    image = image_name[-1].split(".")
    output = r".\\" + image[0] + "(_detected).jpg"
    cv2.imwrite("output", img)
    cv2.imshow("Feature Detected", img)

    # Create a Brute Force Matcher object.
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Perform the matching between the ORB descriptors of the training image and the test image
    matches = bf.match(dp, test_dp)

    # The matches with shorter distance are the ones we want.
    matches = sorted(matches, key=lambda x: x.distance)

    result = cv2.drawMatches(
        image, kp, test_image, test_kp, matches, test_gray, flags=2
    )

    # Display the best matching points
    cv2.imshow("Feature matching", result)

    # Print total number of matching points between the training and query images
    print(
        "\nNumber of Matching Keypoints Between The Training and Query Images: ",
        len(matches),
    )


# Driver Code
if __name__ == "__main__":
    siftAlgorithm()
    cv.waitKey(0)
    cv.destroyAllWindows()
