## Translator and Language Detector Tool using Python 3
This is a python script which will detect the language of the input texts and also it can also translate the input text into the desired language which is provided by the users. It supports 107 languages.
It's like building your own version of google translate or you can call it as **Google Translate 2.0**

### Methods to run the code :
- Clone the repository or, you can download the codebase as a zip file.
- If you have downloaded the zip file of the codebase then unzip the folder in your computer/laptop.
- You must have installed Python IDEs or, you can use the Anaconda Navigator.
- If you have Anaconda Navigator then, you should have used the ipynb file for this project.
- Otherwise you can use the .py file in your Python IDEs such as, PyCharm, VS Code etc.
- Install the python libraries -
```
pip install googletrans
pip install pprint
```
- After installing the libraries, run the ipynb file or, py file to deploy the project.

### Explanation of the code :
- Using this library we can translate from any language to another language.
- Also this library will predict the language of the input text.
- To detect the language of the input text and also the output text the system will generate a particular code for every language.
- Languages can be detected here
```
'af': 'afrikaans',
 'am': 'amharic',
 'ar': 'arabic',
 'az': 'azerbaijani',
 'be': 'belarusian',
 'bg': 'bulgarian',
 'bn': 'bengali',
 'bs': 'bosnian',
 'ca': 'catalan',
 'ceb': 'cebuano',
 'co': 'corsican',
 'cs': 'czech',
 'cy': 'welsh',
 'da': 'danish',
 'de': 'german',
 'el': 'greek',
 'en': 'english',
 'eo': 'esperanto',
 'es': 'spanish',
 'et': 'estonian',
 'eu': 'basque',
 'fa': 'persian',
 'fi': 'finnish',
 'fr': 'french',
 'fy': 'frisian',
 'ga': 'irish',
 'gd': 'scots gaelic',
 'gl': 'galician',
 'gu': 'gujarati',
 'ha': 'hausa',
 'haw': 'hawaiian',
 'he': 'hebrew',
 'hi': 'hindi',
 'hmn': 'hmong',
 'hr': 'croatian',
 'ht': 'haitian creole',
 'hu': 'hungarian',
 'hy': 'armenian',
 'id': 'indonesian',
 'ig': 'igbo',
 'is': 'icelandic',
 'it': 'italian',
 'iw': 'hebrew',
 'ja': 'japanese',
 'jw': 'javanese',
 'ka': 'georgian',
 'kk': 'kazakh',
 'km': 'khmer',
 'kn': 'kannada',
 'ko': 'korean',
 'ku': 'kurdish (kurmanji)',
 'ky': 'kyrgyz',
 'la': 'latin',
 'lb': 'luxembourgish',
 'lo': 'lao',
 'lt': 'lithuanian',
 'lv': 'latvian',
 'mg': 'malagasy',
 'mi': 'maori',
 'mk': 'macedonian',
 'ml': 'malayalam',
 'mn': 'mongolian',
 'mr': 'marathi',
 'ms': 'malay',
 'mt': 'maltese',
 'my': 'myanmar (burmese)',
 'ne': 'nepali',
 'nl': 'dutch',
 'no': 'norwegian',
 'ny': 'chichewa',
 'or': 'odia',
 'pa': 'punjabi',
 'pl': 'polish',
 'ps': 'pashto',
 'pt': 'portuguese',
 'ro': 'romanian',
 'ru': 'russian',
 'sd': 'sindhi',
 'si': 'sinhala',
 'sk': 'slovak',
 'sl': 'slovenian',
 'sm': 'samoan',
 'sn': 'shona',
 'so': 'somali',
 'sq': 'albanian',
 'sr': 'serbian',
 'st': 'sesotho',
 'su': 'sundanese',
 'sv': 'swedish',
 'sw': 'swahili',
 'ta': 'tamil',
 'te': 'telugu',
 'tg': 'tajik',
 'th': 'thai',
 'tl': 'filipino',
 'tr': 'turkish',
 'ug': 'uyghur',
 'uk': 'ukrainian',
 'ur': 'urdu',
 'uz': 'uzbek',
 'vi': 'vietnamese',
 'xh': 'xhosa',
 'yi': 'yiddish',
 'yo': 'yoruba',
 'zh-cn': 'chinese (simplified)',
 'zh-tw': 'chinese (traditional)',
 'zu': 'zulu'
 ```
- In a single word, It will work as Language Detector and as well as a Translator.

### Language Detection Tool :
<img src = "https://i.imgur.com/6jvs9rb.png">

### Translator Tool :
<img src = "https://i.imgur.com/Q5a6coh.png">

***********************************************************************

### Code Contributed by, Abhishek Sharma, 2021, @abhisheks008, #LGMSOC 2021
