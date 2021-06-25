# pip install pyttsx3
import pyttsx3      

# pip install SpeechRecognition
import speech_recognition as sr                     

# pip install pywikihow
from pywikihow import search_wikihow                

# creating object
engine = pyttsx3.init()

# function for speaking up the results through speakers
def fun_talk(audio):
    engine.say(audio)
    engine.runAndWait()

# function for taking the voice commands and recognizing it
def get_command():

    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        rec.pause_threshold = 1

        audio = rec.listen(source)

        try:
            print("Recognizing...")
            query = rec.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"

        return query


if __name__ == '__main__':

    #while True:
    if 1:

        # taking the voice command  from the user
        query = get_command().lower()

        # checking if it contains the phrase 'how to'
        if 'how to' in query:
            try:
                max_results = 1
                data = search_wikihow(query, max_results)
                data[0].print()
                fun_talk(data[0].summary)

            except Exception as e:
                fun_talk('Sorry, I am unable to find the answer for your query.')
