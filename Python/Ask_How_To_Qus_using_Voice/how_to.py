import pyttsx3      
import speech_recognition as sr                     
from pywikihow import search_wikihow                

engine = pyttsx3.init()

def fun_talk(audio):
    engine.say(audio)
    engine.runAndWait()

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

        query = get_command().lower()

        if 'how to' in query:
            try:
                max_results = 1
                data = search_wikihow(query, max_results)
                data[0].print()
                fun_talk(data[0].summary)

            except Exception as e:
                fun_talk('Sorry, I am unable to find the answer for your query.')
