#!/usr/bin/env python
# coding: utf-8

# # Translator Tool using Python

# #### Created by, Abhishek Sharma [Date : 16.10.2020] 

# In[37]:


from IPython.display import Image
Image ("https://specials-images.forbesimg.com/imageserve/1183427805/960x0.jpg")


# Importing the Library functions which we have to use to implement the Translator

# In[2]:


from googletrans import Translator, constants
from pprint import pprint


# In[3]:


translator = Translator()


# ### Indonesia > English (By default)

# In[4]:


# translate a Indonesia text to english text (by default)
translation = translator.translate("Selamat siang")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


# ### Indonesia > Arabic (By default)

# In[5]:


# translate Indonesian text to arabic for instance
translation = translator.translate("Selamat siang", dest="ar")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


# ### specify source language

# In[38]:


translation = translator.translate("Bagaimana kabarmu hari ini ?", src="id")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


# In[7]:


# print all translations and other data
pprint(translation.extra_data)


# ### Translate more than a phrase :

# ### Indonesia > English 

# In[8]:


# translate more than a phrase
## (Indonesian to English)

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


# ### Indonesian > Japanese

# In[9]:


# translate more than a phrase
## (Indonesian to Japanese)

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


# ### Indonesian > Azerbaijan

# In[10]:


# translate more than a phrase 
#(Indonesian to Azerbaijan)
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


# ### Indonesian > Malay

# In[11]:


# translate more than a phrase 
#(Indonesian to Malay)

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


# ### Indoneisan > Turkish

# In[12]:


# translate more than a phrase 
#(Indonesian to Turkish)

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


# ### Indonesian to Bengali

# In[19]:


# translate more than a phrase 
#(Indonesian to Bengali)

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


# ### Indonesian > Hindi

# In[13]:


# translate more than a phrase 
#(Indonesian to Hindi)

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


# ### Detect a Language :

# #### A. Checking of Hindi Language and also check the confidence level of the AI 

# In[39]:


# detect a language
detection = translator.detect("नमस्ते दुनिया")
print("Language code:", detection.lang)
print("Confidence:", detection.confidence)


# In[15]:


# detect a language
detection = translator.detect("kamu lagi apa ?")
print("Language code:", detection.lang)
print("Confidence:", detection.confidence)


# In[16]:


# detect a language
detection = translator.detect("jam berapa kamu pergi ke sekolah  ?")
print("Language code:", detection.lang)
print("Confidence:", detection.confidence)


# In[17]:


# detect a language
detection = translator.detect("sudah makan ?")
print("Language code:", detection.lang)
print("Confidence:", detection.confidence)


# #### B. Print all the languages and their respective codes :

# In[18]:


# print all available languages
print("Total supported languages:", len(constants.LANGUAGES))
print("Languages:")
pprint(constants.LANGUAGES)


# ### The Automated version of Google Translator 2.0

# In[33]:


# Creating the dummy version of Google Translate
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


# In[42]:


Image ("https://cdn.images.express.co.uk/img/dynamic/59/750x445/976492.jpg")


# **Limitations :**
# 
# Google Translate, like other automatic translation tools, has its limitations. The service limits the number of paragraphs and the range of technical terms that can be translated, and while it can help the reader understand the general content of a foreign language text, it does not always deliver accurate translations, and most times it tends to repeat verbatim the same word it's expected to translate. Grammatically, for example, Google Translate struggles to differentiate between imperfect and perfect aspects in Romance languages so habitual and continuous acts in the past often become single historical events. Although seemingly pedantic, this can often lead to incorrect results (to a native speaker of for example French and Spanish) which would have been avoided by a human translator. Knowledge of the subjunctive mood is virtually non-existent. Moreover, the formal second person (vous) is often chosen, whatever the context or accepted usage. Since its English reference material contains only "you" forms, it has difficulty translating a language with "you all" or formal "you" variations.
# 
# 
# Due to differences between languages in investment, research, and the extent of digital resources, the accuracy of Google Translate varies greatly among languages. Some languages produce better results than others. Most languages from Africa, Asia, and the Pacific, tend to score poorly in relation to the scores of many well-financed European languages, with Afrikaans and Chinese being the high-scoring exceptions from their continents. No languages indigenous to Australia or the Americas are included within Google Translate. Higher scores for European can be partially attributed to the Europarl Corpus, a trove of documents from the European Parliament that have been professionally translated by the mandate of the European Union into as many as 21 languages. A 2010 analysis indicated that French to English translation is relatively accurate, and 2011 and 2012 analyses showed that Italian to English translation is relatively accurate as well. However, if the source text is shorter, rule-based machine translations often perform better; this effect is particularly evident in Chinese to English translations. While edits of translations may be submitted, in Chinese specifically one cannot edit sentences as a whole. Instead, one must edit sometimes arbitrary sets of characters, leading to incorrect edits A good example is Russian-to-English. Formerly one would use Google Translate to make a draft and then use a dictionary and common sense to correct the numerous mistakes. As of early 2018 Translate is sufficiently accurate to make the Russian Wikipedia accessible to those who can read English. The quality of Translate can be checked by adding it as an extension to Chrome or Firefox and applying it to the left language links of any Wikipedia article. It can be used as a dictionary by typing in words. One can translate from a book by using a scanner and an OCR like Google Drive, but this takes about five minutes per page.
# 
# 
# In its Written Words Translation function, there is a word limit on the amount of text that can be translated at once. Therefore, long text should be transferred to a document form and translated through its Document Translate function.
# 
# 
# Moreover, like all machine translation programs, Google Translate struggles with polysemy (the multiple meanings a word may have) and multiword expressions (terms that have meanings that cannot be understood or translated by analyzing the individual word units that compose them). A word in a foreign language might have two different meanings in the translated language. This might lead to mistranslations.
# 
# 
# Additionally, grammatical errors remain a major limitation to the accuracy of Google Translate.

# ## Thank You! Stay Safe! :)
