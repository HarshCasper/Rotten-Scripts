# Save the slides you like from Slideshare as a pdf

This python script will download slides from Slideshare and save them as a pdf file. This is accomplished with Selenium Web-driver and fpdf library.
For any SlideShare link, the script grabs the urls of all the elements with class name 'slide-image'. This is the class name of all the slides in SlideShare. It then downloads individual images with the help of the urls. These individual images are stitched together and converted to a pdf document.

## Setting up:

- Create a virtual environment and activate it

- Install the requirements

```sh
  $ pip install -r requirements.txt
```

## Running the script:

```sh
  $ python slide_downloader.py [url]  #without the brackets
```

## Example running the script:

```sh
  $ python slide_downloader.py https://www.slideshare.net/fadirra/free-ai-kit-game-theory
```

The code asks you for a filename for the pdf and done!! The pdf will be saved in the same directory.
