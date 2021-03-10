## Backgraound Remover ##

- This is simple background remover script that intends to remove background from a still frame.
- This uses python with various libraries like openCV and numpy.

## How to Setup ##

- Clone the folder to your local repository.
- Install libraries like openCV using command *pip install opencv-python*. 
- The *main.py* file does all the work. 
- Change path of the image on line number    to the path of image you want to remove background of.
- Run the program from CLI using *python main.py*.

## How does this work ## 

- It reads the input.
- Converts it into grey.
- Thresholds it and inverts it as mask.
- Optionally apply morphology to clean up any extraneous spots
- Anti-alias the edges.
- Convert a copy of the input to BGRA and insert the mask as the alpha channel.

## Parameters and customizations ##

- BLUR - To change the amount of opacity you want to cover while masking the input.
- MASK_COLOR - To change the background of the output to your desired color. The color format used there is BGR.


## What you might see ##

- Output and Input Image. 
![Image]('https://imgur.com/gallery/IDRm79h')

## Author ##
- [piSquared]('https://github.com/pi-squared-4')  

