# Change Image Background

#### AIM:  
We will build a project that can help us in changing the background of any image without using any image editor like Photoshop, etc. This project can be done with the help of some libraries using Python programming.
#### PURPOSE: 

In this project we will be changing the background of image with the help of some libraries using Python programming.

#### DESCRIPTION:
The details of python libraries and how they are working is here- 

**LIBRARIES USED**
- **Numpy:** `numpy` forms the basis of powerful machine learning libraries like scikit-learn and SciPy. As machine learning grows, so does the list of libraries built on `numpy`. TensorFlow’s deep learning capabilities have broad applications — among them speech and image recognition, text-based applications, time-series analysis, and video detection. PyTorch, another deep learning library, is popular among researchers in computer vision and natural language processing.

- **OpenCV:** `opencv` is a library of programming functions mainly aimed at real-time computer vision. Originally developed by Intel, it was later supported by Willow Garage then Itseez. The library is cross-platform and free for use under the open-source Apache 2 License.

- **Matplotlib:** `matplotlib` is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK.

#### INSTALLATION:
Install the following libraries using `pip` command in any terminal

```python
pip install numpy
pip install opencv-python
pip install matplotlib
```
#### WORKFLOW:

1. We are importing the required libraries 
2. Reading the image as per our choice
3. Then applying mask on the image
4. Resizing the image, so that both the images can be of same size
5. Now with the help of and operation combining the masked image with background image
6. After that displaying and saving the final image

