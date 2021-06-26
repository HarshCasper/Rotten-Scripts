from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
from fpdf import FPDF
import threading
import speech_recognition as sr
import os

#variables
video_clip = ''
audio_clip = ''

def audio_to_pdf():
    '''
    Function to convert audio to pdf:
    Here, we first extract the audio from the selected video and store it into
    'my_audio.wav'. Then, using the speech recognition module and Google speech API,
    we convert this audio to text and write it into a file named 'my_text.txt'.
    This text file is then passed to text_to_pdf function to convert it into a pdf and at
    the end the audio and text files are removed using the OS module as we don't need them anymore.
    '''
    global audio_clip
    try :
        #extract audio
        audio_clip = video_clip.audio.write_audiofile(r"my_audio.wav")
        r = sr.Recognizer()
        #open the audio file
        with sr.AudioFile("my_audio.wav") as source:
            #listen for the data
            audio_data = r.record(source)
            #recognize
            text = r.recognize_google(audio_data)
            #write into a file
            write_file = open('my_text.txt', 'w')
            write_file.write(text)
            write_file.close()
            #convert to pdf
            text_to_pdf('my_text.txt')
        print("Conversion Successfull!")
    except:
        print("Conversion not performed")

    #delete audio and text files
    os.remove("my_text.txt")
    os.remove("my_audio.wav")


def text_to_pdf(file):
    '''
    Function to convert text to pdf:
    In this function, we create a pdf using the FPDF module and add a page to it and set the font.
    Effective page width is calculated so that
    Then, we open the text file in read mode and using multi_cell(for wrapping the text into multiple lines),
    insert the text from the text file into the pdf.
    At last, we save it as 'my_pdf.pdf'.
    '''
    pdf = FPDF(format='letter', unit='in')
    pdf.add_page()
    pdf.set_font("Arial", size = 12)
    effective_page_width = pdf.w - 2*pdf.l_margin
    #open text file in read mode
    f = open(file, "r")
    #write the pdf
    for x in f:
        pdf.multi_cell(effective_page_width, 0.15, x)
        pdf.ln(1)

    #save the pdf
    pdf.output("../Video to PDF(CLI)/my_pdf.pdf")


if __name__ == '__main__':
    try:
        video_filepath = input('Enter video path : ')
        video_clip = VideoFileClip(str(video_filepath))
        print('Starting conversion....')
        audio_to_pdf()
    except:
        print('No video selected')
