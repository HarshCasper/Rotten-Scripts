# pip install pyttsx3
import pyttsx3 
# pip install SpeechRecognition
import speech_recognition as sr  
# pip install wikipedia
import wikipedia  

# creating object
engine = pyttsx3.init()

# function for speaking up the wikipedia results through speakers
def fun_talk(audio):
    engine.say(audio)
    engine.runAndWait()

# function for taking the questions/queries using voice commands and recognizing them
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

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"

        return command


if __name__ == '__main__':

    # taking the query input in the form of voice command from the user using the get_command function
    query = get_command().lower()

    try:
        # checking if it contains the word 'wikipedia'
        if 'wikipedia' in query:
            fun_talk('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            
            # searching query on wikipedia and getting the results
            results = wikipedia.summary(query, sentences=5)
            fun_talk("According to Wikipedia")
            print(results)
            fun_talk(results)
        else:
            print("Try again..\nFor example, say \"india country wikipedia\"")
            fun_talk("Try again..\nFor example, say \"india country wikipedia\"")

    except Exception as e:
        print("There is something wrong. Try again please..")
