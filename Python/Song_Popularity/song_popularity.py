import lyricsgenius
# Feed your Client Access Token
genius = lyricsgenius.Genius("___")

# Feed the artist name, and the number of song
artist = genius.search_artist("Coldplay", max_songs=3, sort="popularity")
