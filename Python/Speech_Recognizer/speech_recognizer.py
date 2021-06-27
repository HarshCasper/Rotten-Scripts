import speech_recognition as sr                    
import pyttsx3       

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
            command = rec.recognize_google(audio, language='en-in')
            print(f"You said: {command}\n")
            fun_talk(f"You said: {command}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"

        return command


if __name__ == '__main__':

    if 1:

        query = get_command().lower()
