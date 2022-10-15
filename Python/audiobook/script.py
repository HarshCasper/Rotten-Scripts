from audiobook import AudioBook
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("-f", "--file", required=True, help="Path to file")
args = vars(arg.parse_args())

ab = AudioBook(speed="normal") # default speed is normal/slow/fast

def read_book(input_file_path):
    """ if you want to read your book """
    ab.create_json_book(input_file_path)


def save_audio(input_file_path):
    """ if you want to save your audio books """
    ab.save_audio(input_file_path)
    
if __name__ == "__main__":
    input_file_path = args["file"]
    read_book(input_file_path)
    # save_audio(input_file_path)

# contributor: @codeperfectplus
# full code: https://github.com/Py-Contributors/audiobook
# Pypi: https://pypi.org/project/audiobook/

# requirements.txt audiobook==2.0.0
