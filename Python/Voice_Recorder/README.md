# Voice Recorder using Python

## Modules Required

* sounddevice
sounddevice is used play and record audio signals in NumPy arrays.

* scipy
scipy is used to save the recorded audio in file format.

## Installation of the above module
Install the above modules using<!-- Italics-->*pip install sounddevice scipy* command.


## How to record audio
* Download or clone the repository.
* Install the required modules.
* Run voice_recorder.py after specifying the location where you want to store the final recorded audio in the <!-- Italics-->*scipy.io.wavfile.write()* function.
* The recorded audio will appear at the specified location.
* The duration of recording set here is 6.5 seconds, which can be modified by changing the value of <!-- Italics-->*time_sec* variable.


## Output
The recorded audio <!-- Italics-->*recorded_audio.wav* will be saved to the location entered in the <!-- Italics-->*scipy.io.wavfile.write()* function.

Here's the ouput:

![recoutput](https://user-images.githubusercontent.com/60272753/119265994-988af000-bc06-11eb-8a8f-7d9c73e7d006.PNG)

![voiceoutput](https://user-images.githubusercontent.com/60272753/119265992-96c12c80-bc06-11eb-935b-438d6ce73bf5.PNG)


## Audio


https://user-images.githubusercontent.com/60272753/119339369-b1e77700-bcae-11eb-8c52-ea1c30429ce2.mp4

