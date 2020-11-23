import lyricsgenius
# Feed your Client Access Token
genius = lyricsgenius.Genius("9ty1rExjjFq3wXSm404uxGX9Pf0dp7K5H6FiJzr3LxW5XS7xdH7S_iG7g5H4NTGb")

# Feed the artist name, and the number of song
artist = genius.search_artist("Coldplay", max_songs=3, sort="popularity")
