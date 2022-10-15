## Installation

Install using [pypi](https://pypi.org/project/audiobook/)

```sh
pip install audiobook
```

```python
from audiobook import AudioBook
ab = AudioBook(speed="normal") # argument: Speech-Speed="slow/normal/fast"

ab.save_audio(file_path, password=None) # save audio file 
ab.read_book(file_path, password=None) # listen to the book
```

## Usages

The audiobook is a python module for listening to your favourite PDF book.

## Test

Run tests:

```sh
pip install -r requirements.txt
python -m unittest tests
```

## Documentation

Read Detailed [Documentation here](https://audiobook.readthedocs.io/)

### Linux Installation Requirements

- If you are using a Linux system and the voice output is not working, then :
    Install espeak , ffmpeg and libespeak1 as shown below:

```sh
sudo apt update && sudo apt install espeak ffmpeg libespeak1
```

## Roadmap

- Speech-Speed Control
- Support more extensions
- Save the audiobook for future

## Project status

This project is currently in development. Any contributions are welcome.

## Changelog

**V2.0.0**

- [x] Save Audio Book locally
- [x] Listen to the book
- [x] Speech-speed control
- [x] Read password-protected PDF
- [x] Create JSON file for the book  
- [ ] Change the voice of the narrator

- [ ] Support more extensions
