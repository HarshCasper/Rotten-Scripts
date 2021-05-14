# Generate Scanned Image

## This script is used to generate a scanned copy of the image provided.

+ On running this script, a scanned file of the orignal image is generated after applying Adaptive Thresholding. 

+ It is effective when an image has different lighting conditions in different areas. Here, the algorithm determines the threshold for a pixel based on a small region around it. So we get different thresholds for different regions of the same image which gives better results for images with varying illumination. 

+ And this is what done in the script, multiple threshold values are set up in order to give image a scanned and enhanced look.


## To run the script:

1. Setup a virtual environment.
2. Install the dependencies by running ```pip3 install -r requirements.txt```
3. Run the script.

```sh
python camscanner.py \<filename\>
```
       
## References:

For Thresholding, consider going through [OpenCV Doecumantation](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html) and this [Article](https://medium.com/@anupriyam/basic-image-thresholding-in-opencv-5af9020f2472).
