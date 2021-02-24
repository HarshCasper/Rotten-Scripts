# Subtitle Downloader using Python

Every one loves to watch series and movies, and some people need subtitle to understand the dialogues because of different accents used.  
We often use some websites to download the subtitles, but it is quite a hectic task to do, search for the right website, and then download it, and finally start watching the movie.  
But what if we automate this with Python, and with just one command we can download the subtitles of any movie/series.

![Movie](https://www.bollywoodhungama.com/wp-content/uploads/2020/04/Hollywood-movies-have-amassed-only-Rs.-50-crores-at-the-India-box-office-in-the-first-quarter-of-2020.jpg)

## Prerequisites

1. Python must be installed in your laptop/system. If you don't, install it from [here](https://www.python.org/downloads/).
2. `pip install subtitle-downloader-python3==0.1.0`

## Understanding the Code - subtitle_downloader.py

![image](https://snipboard.io/L3afcO.jpg)

This is the whole code, so now let's understand it line by line.

```
import urllib
import os
import hashlib
import sys
```

`urllib` module is the URL handling module for python. It is used to fetch URLs (Uniform Resource Locators). It uses the urlopen function and is able to fetch URLs using a variety of different protocols. You don't need to install it, it comes with the standard library of Python, but in case it's not working, use `pip install urllib`.

The `os` module in python provides functions for interacting with the operating system. OS, comes under Python's standard utility modules. This module provides a portable way of using operating system dependent functionality.

`hashlib` module implements a common interface to many different secure hash and message digest algorithms. The terms “secure hash” and “message digest” are interchangeable. Older algorithms were called message digests. The modern term is secure hash.

`sys` module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.

Now, the next code is using the [SubDB](http://thesubdb.com/api/) API, you can check it's documentation from here.

## Understanding the code - __init__.py

```
from .subtitle import main
```

It is used to add the subtitles to your file i.e. movie/series.

You can find this package [here](https://pypi.org/project/subtitle-downloader-python3/0.1.0/).

How to publish a Python package on PyPI? [Check the video here](https://www.youtube.com/watch?v=TgCCbV_2C7s&t=6s)
