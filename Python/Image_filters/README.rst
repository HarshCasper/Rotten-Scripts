Image Filter
============

|checkout|

Convolution is a technique widely used in image processing . Convolution
is a mathematical operation on two functions that produces a third
function expressing how the shape of one is modified by the other. (As
defined in Wikipedia).

Though this technique is widely used in image processing, in my
implementation it can be used as an image filter.

Images are made of pixels, colored images have 3 streams (red, green,
blue), these can be visualised as a matrix which is 3 dimensional Each
of the red, blue and green are streams, stacked together to form a cube

A kernel or a smaller matrix, in this case a 3X3 matrix is used to
perform convolution.

The kernel is used to perform dot product with the image. The resultant
is an image which has different properties.

This script written in Python, implements convolution over colored
images.

The end result is the application of filters to images.

I have used tensorflow, numpy and the image processing library.

The images attached show an image before and after blurring.

The following is a link to my blog on medium regarding the same : https://medium.com/@namyalg/3-dimensional-convolution-7041ca7f3e81

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/Image_filters/

