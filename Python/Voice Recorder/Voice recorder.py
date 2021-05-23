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
  
    
# Recording duration
time_sec = 6.5

print('Recording Started...')
  
# rec to start the sudio recording
# blocking argument is set to true to make function synchronous
audio = sounddevice.rec(int(sampling_freq*time_sec), blocking=True)
  
    
# to convert numpy array to audio file  
scipy.io.wavfile.write("recorded_audio.wav", sampling_freq, audio)

print('Recorded')
