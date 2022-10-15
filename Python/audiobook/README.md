## Installation

Install using [pypi](https://pypi.org/project/audiobook/)

```sh
pip install audiobook
```

## Usages

The audiobook is a python module for listening to your favourite PDF book.

```python
from audiobook import AudioBook
ab = AudioBook(speed="normal") # argument: Speech-Speed="slow/normal/fast"

ab.save_audio(file_path, password=None) # save audio file 
ab.read_book(file_path, password=None) # listen to the book
```

### Linux Installation Requirements

- If you are using a Linux system and the voice output is not working, then :
    Install espeak , ffmpeg and libespeak1 as shown below:

```sh
sudo apt update && sudo apt install espeak ffmpeg libespeak1
```
