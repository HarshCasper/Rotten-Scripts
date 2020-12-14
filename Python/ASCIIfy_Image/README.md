# ASCIIfy your image

This python script converts the input image to an ASCII version of itself. This is achieved by giving a different range of grayscale values to different special characters from the ASCII set. The whole image is then converted based on this.

## Setting up:

- Create a virtual environment and activate it

- Install the requirements

```sh
  $ pip install pillow
```

## Running the script:

```sh
  $ python asciify.py [image_path]  #without the brackets
```

## Example running the script

```sh
  $ python asciify.py input.jpg  
```

![Input image](input.jpg)

### Will be converted to....
<br>

![Converted image](image.png)
