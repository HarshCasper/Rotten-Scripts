# Test_Summary

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

Text Summarization is an advanced project and comes under the umbreall of Natural Language Processing.
There are multiple methods people use in order to summarize text.

they can be affectively clubbed under 2 methods:

- Abstractive: Understand the true context of text before summarization (like a human).
- Extractive: Rank the text within the file and identify the impactful terms.

While both these approaches are under reasearch, extrcative summarization is presently sed acroos multiple latfomrs.
There are multiple methods by which text is summarized under extractive approach as well.

In this script we will use the 2 important approach __Lex__ & __Text__, and will discuss their pros and cons.
click 
[here](https://en.wikipedia.org/wiki/Automatic_summarization#:~:text=The%20edges%20between%20sentences%20are,by%20the%20sentences'%20lengths) 
for more info.

Both the script uses datasets from Natural Language Processing.

## Structure

- [Lex Rank](Lex%20Rank) contains the necessary files for Lex Ranking approach.
- [Text Rank](Text%20Rank) contains the necessary files for Text Ranking approach.
- [Assets](assets) contains the the text files.

## Instructions

Detailed set of instructions can be found in respective directories.

## Author(s)

Made by [Vybhav Chaturvedi](https://www.linkedin.com/in/vybhav-chaturvedi-0ba82614a/)


## Setup instructions

- Setup a `python 3.x` virtual environment.
- `Activate` the environment
- Install the dependencies using ```pip3 install -r requiremnts.txt```
- You are all set and the [script](../../AutoStyler/Scripts/text_extract.py) is Ready to run.
- Carefully follow the Instructions.

## Further Readings

Some newcomers for the first time struggle with Tesseract, this is a direct link to the [installer](https://github.com/UB-Mannheim/tesseract/wiki)

Setting up OCR can be found [here](https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i)

## Usage

Just make sure that Tessaract is in proper directory, run the code according the comments and guidelines.

```
Smaple - 
Enter the Folder name containing Images: <Name of Folder>
Enter your desired output location: <Name of Folder>
```

## Output

Output

![Output](assets/Output.PNG)

Image containing Text

![Before Compression](assets/Sample.PNG)

After Extraction

![After Backup](assets/TextFile.PNG)



