### Get lyrics
This script will send input of artist name and song name to a http://www.azlyrics.com/ to fetch the song lyrics.
### Requirements

Make sure you have the requirements fulfilled by running the following command, additional packages might will be installed too:

`pip install -r requirements.txt`


##### How to use the script?

- Arguments
  ```
  python get_lyrics.py --artist <artistName> --song <songName>
  ```
  For example, I would like to find a lyric for the Godzilla song by Eminem:
  ```
  python get_lyrics.py --artist "eminem" --song "godzilla"
  ```
