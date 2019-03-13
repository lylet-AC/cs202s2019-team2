
# define a new class that stores some data
class Song():
    def __init__(self, title, artist, album, genre, year, rank):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.year = int(year)
        self.rank = int(rank)

    def __repr__(self):
        return repr((self.title, self.artist, self.album, self.genre, self.year, self.rank))

    # this returns a string of the song data formatted like the input file
    def get_song_as_string(self):
        string = self.title+" | "+self.artist+" | "+self.album+" | "+self.genre+" | "+str(self.year)+" | "+str(self.rank)
        return string
