# Stop Motion creator
This python script creates stopmotion videos from given video file at a required framerate.

# How to use?
Just type in:

`python main.py --input videofile.mp4 --output stopmotion.mp4 --frate 0.3`

This will convert the video file into images at mentioned framerate and create an additional directory which will be deleted once the script is complete and the resulting video file will be available.

You can always type in:

`python main.py -h` or `python main.py -h` for any help with arguments.


```
-i --input (input videofile)
-o --output (Output videoname include the extension.)
-fps --framesps (Requried frame rate)
-frate --frate (Required frames per second) default set to 0.1
```

# Requirements
Before running the script, just install open-cv for python using this command:

`pip install opencv-python`

> Happy Stop Motioning.
