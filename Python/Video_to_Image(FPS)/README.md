# Video to Image at required FPS
This python script converts video to images at a required framerate which can be useful for Extracting Deep Learning training images.
There are two files single_convert uses a single video and multi_convert requires the video files specified as an input.

# How to use?
Just type in:

`python single_convert.py --input videofile.mp4 --output output_dir --frate 1`

This will convert the video file into images at 1s per framerate meaning it will extract images every one second.

`python multi_convert.py --input videofile.mp4 --output output_dir --frate 1`

This will convert the video files into images at 1s per framerate meaning it will extract images every one second.

You can always type in:

`python single_convert.py -h` or `python single_convert.py -h` for any help with arguments.


```
-i --input (input argument)
-o --output (output path)
-fps --framesps (Requried frame rate)
-frate --frate (Required frames per second) default set to 0.1
```

# Requirements
Before running the script, just install open-cv for python using this command:

`pip install opencv-python`

> Happy Extracting images.
