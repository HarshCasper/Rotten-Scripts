# SIFT(Scale invariant Feature Transform)

- In this script, we implement the `SIFT algorithm` for the feature extraction from an image
- After that create a test image by adding Scale Invariant and Rotational Invariant to the input image by which the resolution and alignment of the input image is changed.
- After this, we use the `Brute Force Matcher algorithm` for matching the feature of the input and test image.
- The SIFT features are local and based on the appearance of the object at particular interest points, and are invariant to image scale and rotation.

There are mainly four steps involved in the SIFT algorithm.

- **Scale-space peak selection:** Potential location for finding features.

- **Keypoint Localization:** Accurately locating the feature keypoints.

- **Orientation Assignment:** Assigning orientation to keypoints.

- **Keypoint descriptor:** Describing the keypoints as a high dimensional vector.

- **Keypoint Matching:** Keypoints between two images are matched by identifying their nearest neighbours. But in some cases, the second closest-match may be very near to the first.

## Setup instructions

- This algorithm is patented, so this algorithm is included in the Non-free module in OpenCV.
- For using this script, you need to use the `Open CV version <3.0` and additionally you need to install the `opencv-contrib-python` of the same version.
- User need to input the path of the image for which user want to extract the features

## Output

#### Input1
![](https://i.ibb.co/5XQT3Qb/Input-Image.png) ![](https://i.ibb.co/6g3cWkk/Output-image.png)
![](https://i.ibb.co/kMFG4gX/Output-SIFT.png)

#### Input2
![](https://i.ibb.co/whqTTDw/Input2-SIFT.png)
![](https://i.ibb.co/DtZPKBv/Output2-SIFT.png)

## References
- [OpenCV (SIFT Algorithm)](https://docs.opencv.org/master/da/df5/tutorial_py_sift_intro.html)
- [Wikipedia (SIFT Algorithm)](https://en.wikipedia.org/wiki/Scale-invariant_feature_transform)
## Author

[Shubham Gupta](https://github.com/ShubhamGupta577)
