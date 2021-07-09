# Ask 'How to' Questions using Voice

For asking how to type questions firstly we are using the `SpeechRecognition` library so that our device can recognize our voice command to take input and then `pyttsx3` library for converting text to speech so that the device can speak up the results or output, and last important library is `pywikihow` to fetch the answers for how to type questions. 

## Packages Used
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

## Installation

Install all these libraries with `pip` command in any terminal by using the following command

```python
pip install -r requirements.txt
```

OR

Go to the [`requirements.txt`](https://github.com/Umesh-01/Rotten-Scripts/blob/patch-2/Python/Ask_How_To_Qus_using_Voice/requirements.txt) file to manually install the libraries one by one

## Working
To start using the project, follow the below guidelines: 

**1.**  Fork this project/repository. 🍴

**2.**  Clone your forked copy of the project/repository.

```
git clone https://github.com/<your-github-username>/Rotten-Scripts.git
```

**3.** Navigate to the project directory :file_folder: 

```
cd Rotten-Scripts/Python/Ask_How_To_Qus_using_Voice/
```

**4.** Install the `requirements.txt` using command 🔧

```
pip install -r requirements.txt
```

**5.** Run `how_to.py` file 💻

```
python how_to.py
```

**6.** Now, ask your **"how to"** type question using voice command 🗣️

**7.** Finally, you will get the answer for your question 🔈  

## Output

#### In CLI

[Image 1](https://imgur.com/8dEKklo)

[Image 2](https://imgur.com/clqOIaG)

#### In PyCharm

[Image 1](https://imgur.com/EKBmZUP)

[Image 2](https://imgur.com/DQVbQpO)

## Contributor
[Umesh Singh](https://github.com/Umesh-01)
