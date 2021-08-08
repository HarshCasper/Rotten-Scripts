import sounddevice as sd
import wavio as wv
import random

# Sampling frequency
freq = 44100

# Recording duration in seconds
duration = 20

print("Recording...")

# Start recorder with the given values of duration and sample frequency
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

# Record audio for the given number of seconds
sd.wait()

name = random.randint(1, 10000)

# Convert the NumPy array to audio file
wv.write(f"recording{name}.wav", recording, freq, sampwidth=2)

print("Recording Completed...")
