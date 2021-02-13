Convert Frames to Video
=======================

|checkout|

This python script will convert all the frames from a folder into a
video. This is accomplished using OpenCV, a highly optimized library for
computer vision applications. Specifically, we use the VideoWriter
function to combine images(in a particular fps) and obtain a video.

Setting up:
-----------

-  Create a virtual environment and activate it
-  Install the requirements

.. code:: sh

     $ pip install opencv-python

Running the script:
-------------------

.. code:: sh

     $ python frames_to_video_converter.py [image_folder_path]  #without the brackets

The script will ask you for the needed ‘fps’ and a video name.

Note:
-----

The images in the folder should be numbered in the order in which they
appear in the video.

.. figure:: frames.JPG
   :alt: Pendulum frames images

After running the script, the video will be created in the directory
where the script is running.

.. figure:: video.gif
   :alt: frames_video

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/Frames_to_Video_converter/

