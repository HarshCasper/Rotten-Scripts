# Script to Convert audio files from one format to another
import os
from glob import glob
import pydub
import mutagen
import keyboard

# Directory containing the audio File
# Extension is according the the file type before conversion.
song_dir = './*.mp3'


def conversion(song):
    for song in song:
        # Extension in which file is supposed to be converted
        mp3_song = os.path.splitext(song)[0] + '.wav'
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
        # Change the extension to the desired format
        sound.export(mp3_song, format="wav")
        # If you want to keep the old format, Press anything other than [y]
        print("Converted", os.path.basename(mp3_song), "Do you want to delete the original files? Press [y] for Yes.\n")
        while True:
            if keyboard.read_key() == "y":
                print("Deleting Duplicate File\n")
                os.remove(song)
                print("Thank You\n")
                break
            else:
                print("Nothing Deleted!!!\n")
                break
    print("Conversion Done")


def parameters(song):
    for song in song:
        audio_info = mutagen.File(song).info
        print("Sample Rate is", audio_info.sample_rate)


def main():
    print(song_dir)
    # Glob for file selection
    song = glob(song_dir)
    print(song)
    parameters(song)
    conversion(song)


if __name__ == "__main__":
    main()
