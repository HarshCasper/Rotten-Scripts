# Script to Convert audio files from one format to another
import os
from glob import glob
import pydub
import mutagen

# Directory containing the audio File
song_dir = 'C:\\Users\\asus\\Desktop\\Songs\\*.mp3'  # Extension is according the the file type before conversion.


def conversion(song):
    for song in song:
        mp3_song = os.path.splitext(song)[0] + '.wav'  # Extension in which file is supposed to be convert
        """
        Support .mp3,
                .mp4,
                .ogg,
                .aac,
                .flv,
                .mkv,
                .flac,
                .wav
        """
        sound = pydub.AudioSegment.from_mp3(song)
        sound.export(mp3_song, format="wav")  # Change the extension to the desired format
        os.remove(song)  # If you want to keep  the old format, comment this line
    print("Conversion Done")


def parameters(song):
    for song in song:
        audio_info = mutagen.File(song).info
        print("Sample Rate is", audio_info.sample_rate)


def main():
    print(song_dir)
    song = glob(song_dir)  # Glob for file selection
    print(song)
    parameters(song)
    conversion(song)


if __name__ == "__main__":
    main()
