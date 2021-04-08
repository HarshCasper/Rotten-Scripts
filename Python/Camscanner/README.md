# Generate Scanned Image
## This script is used to generate a scanned copy of the image provided.

+ On running this script, a scanned file of the orignal image is generated after applying Adaptive Thresholding. 

+ It is effective when an image has different lighting conditions in different areas. Here, the algorithm determines the threshold for a pixel based on a small region around it. So we get different thresholds for different regions of the same image which gives better results for images with varying illumination. 

+ And this is what done in the script, multiple threshold values are set up in order to give image a scanned and enhanced look.


## To run the script:
1. Install the dependencies by running following command in terminal.

   `pip install opencv-python`
   `pip install numpy`
   `pip install matplotlib`
   
2. Run the script.

    `python camscanner.py \<filename\>`
    
    
## References:
1. https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html

2. https://medium.com/@anupriyam/basic-image-thresholding-in-opencv-5af9020f2472
