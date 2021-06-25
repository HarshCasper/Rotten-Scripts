# Ask 'How to' Questions using Voice

For asking how to type questions firstly we are using the `SpeechRecognition` library so that our device can recognize our voice command to take input and then `pyttsx3` library for converting text to speech so that the device can speak up the results or output, and last important library is `pywikihow` to fetch the answers for how to type questions. 

### SpeechRecognition

It is a library for performing speech recognition, with support for several engines and APIs, online and offline.

`SpeechRecognition` engine/API support:

- CMU Sphinx (works offline)
- Google Speech Recognition
- Google Cloud Speech API
- Microsoft Bing Voice Recognition
- Houndify API
- IBM Speech to Text

### pyttsx3 

`pyttsx3` is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3. Works without internet connection or delay. Supports multiple TTS engines, including Sapi5, nsss, and espeak.

### pywikihow

`pywikihow` is an unofficial WikiHow python API. It uses BeautifulSoup to scrape WikiHow information and return the data that we want.

## Install

Install all these libraries with `pip` command in any terminal

```python
pip install SpeechRecognition

pip install pyttsx3

pip install pywikihow
```

## Working

Import the `SpeechRecognition` , `pyttsx3` and `pywikihow` libraries in the Python file that you are going to use to get the get the information/ answers for your how to type questions. The `pywikihow` library provide functions to easily get the information from WikiHow website to your console/application.

For example-

```python
import pyttsx3                                      

import speech_recognition as sr                     

from pywikihow import search_wikihow                
```

## Screenshots

#### In CLI

<img src="https://github.com/Umesh-01/Rotten-Scripts/blob/patch-2/Python/Ask_How_To_Qus_using_Voice/Images/howtoqus3.png">

<img src="https://github.com/Umesh-01/Rotten-Scripts/blob/patch-2/Python/Ask_How_To_Qus_using_Voice/Images/howtoqus4.png">

#### In PyCharm

<img src="https://github.com/Umesh-01/Rotten-Scripts/blob/patch-2/Python/Ask_How_To_Qus_using_Voice/Images/howtoqus1.png">

<img src="https://github.com/Umesh-01/Rotten-Scripts/blob/patch-2/Python/Ask_How_To_Qus_using_Voice/Images/howtoqus2.png">

## Contributor
<a href="https://github.com/Umesh-01">Umesh Singh</a>
