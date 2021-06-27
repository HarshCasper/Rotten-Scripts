# Speech Recognizer
Speech recognizer helps us to save time by speaking instead of typing. 
It also gives us the power to communicate with our devices without even writing one line of code. 
This makes technological devices more accessible and easier to use. Speech recognition is a great example of using machine learning in real life.

## Modules Used

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

## Install

Install both the libraries with `pip` command in any terminal

```python
pip install SpeechRecognition

pip install pyttsx3
```

## Working

Import the `SpeechRecognition` and `pyttsx3` libraries in the Python file that you are going to use for recognizing your voice commands in your console/application.

For example-

```python
import speech_recognition as sr 

import pyttsx3                                                        
```
