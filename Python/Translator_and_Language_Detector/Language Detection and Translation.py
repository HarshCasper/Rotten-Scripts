from IPython.display import Image
Image ("https://specials-images.forbesimg.com/imageserve/1183427805/960x0.jpg")

from googletrans import Translator, constants
from pprint import pprint


translator = Translator()



# translate a Indonesia text to english text (by default)
translation = translator.translate("Selamat siang")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


# Indonesia > Arabic (By default)
# translate Indonesian text to arabic for instance
translation = translator.translate("Selamat siang", dest="ar")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


# specify source language
translation = translator.translate("Bagaimana kabarmu hari ini ?", src="id")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

# print all translations and other data
pprint(translation.extra_data)


# Translate more than a phrase :

# Indonesia > English 

sentences = [
    "Halo Semua",
    "Apa kabar ?",
    "Apakah kamu bisa berbahsa Indonesia ?",
    "oke bagus!",
    "Senang berkenalan denganmu"
]
translations = translator.translate(sentences, dest="en")
for translation in translations:
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


# Indonesian > Japanese
sentences = [
    "Halo Semua",
    "Apa kabar ?",
    "Apakah kamu bisa berbahsa Indonesia ?",
    "oke bagus!",
    "Senang berkenalan denganmu"
]
translations = translator.translate(sentences, dest="ja")
for translation in translations:
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


# Indonesian > Azerbaijan

sentences = [
    "Halo Semua",
    "Apa kabar ?",
    "Apakah kamu bisa berbahsa Indonesia ?",
    "oke bagus!",
    "Senang berkenalan denganmu"
]
translations = translator.translate(sentences, dest="az")
for translation in translations:
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


# Indonesian > Malay

sentences = [
    "Halo Semua",
    "Apa kabar ?",
    "Apakah kamu bisa berbahsa Indonesia ?",
    "oke bagus!",
    "Senang berkenalan denganmu"
]
translations = translator.translate(sentences, dest="ms")
for translation in translations:
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


# Indoneisan > Turkish

sentences = [
    "Halo Semua",
    "Apa kabar ?",
    "Apakah kamu bisa berbahsa Indonesia ?",
    "oke bagus!",
    "Senang berkenalan denganmu"
]
translations = translator.translate(sentences, dest="tr")
for translation in translations:
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


# Indonesian to Bengali

sentences = [
    "Halo Semua",
    "Apa kabar ?",
    "Apakah kamu bisa berbahsa Indonesia ?",
    "oke bagus!",
    "Senang berkenalan denganmu"
]
translations = translator.translate(sentences, dest="bn")
for translation in translations:
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


# Indonesian > Hindi
sentences = [
    "Halo Semua",
    "Apa kabar ?",
    "Apakah kamu bisa berbahsa Indonesia ?",
    "oke bagus!",
    "Senang berkenalan denganmu"
]
translations = translator.translate(sentences, dest="hi")
for translation in translations:
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


# Detect a Language :

detection = translator.detect("नमस्ते दुनिया")
print("Language code:", detection.lang)
print("Confidence:", detection.confidence)


detection = translator.detect("kamu lagi apa ?")
print("Language code:", detection.lang)
print("Confidence:", detection.confidence)


detection = translator.detect("jam berapa kamu pergi ke sekolah  ?")
print("Language code:", detection.lang)
print("Confidence:", detection.confidence)


detection = translator.detect("sudah makan ?")
print("Language code:", detection.lang)
print("Confidence:", detection.confidence)


# B. Print all the languages and their respective codes :

print("Total supported languages:", len(constants.LANGUAGES))
print("Languages:")
pprint(constants.LANGUAGES)


#  The Automated version of Google Translator 2.0
print ("Welcome to the translator! Please follow the steps...\n\n")
while (1>0):
    s = input ("Enter the Text : ")
    change = input ("Enter in which language do you want to translate (code) : ")
    translation = translator.translate(s, dest=change)
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    check = input("\nDo you wanna continue it [Y/N] ? ")
    if (check == 'N' or check == 'n'):
        print ("\n\n::Thank you for using the translator! Have a nice day ahead!!::")
        break
