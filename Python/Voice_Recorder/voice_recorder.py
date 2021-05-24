""" install the req libraries if not installed before
pip install sounddevice scipy """   

import scipy.io.wavfile
# importing the req libraries
import sounddevice

""" Run the code to start recording, audio will be saved to the same folder """

# set a sample frequency of the audio to be recorded
sampling_freq = 48000

# set a default value for samplerate and channels using sounddevice.default
sounddevice.default.samplerate = sampling_freq

# set default no. of channels
# Max number of channels for a device can be found out with query_devices()
sounddevice.default.channels = 2
  
    
# Recording duration, can modify the duration by changing the value
time_sec = 6.5

print('Recording Started...')
  
# rec function to start the audio recording
# blocking argument is set to true to make function synchronous
audio = sounddevice.rec(int(sampling_freq*time_sec), blocking=True)
  
    
# converting numpy array to audio file  
# specify the location where you want to store the recorded file in '...'
scipy.io.wavfile.write(r'C:\Users\cv\Desktop\recorded_audio.wav', sampling_freq, audio)

print('Recorded')
