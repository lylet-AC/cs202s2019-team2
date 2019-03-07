from Song import Song



def main():

    # set up the location of the songlist
    filepath = "../data/songlist.txt"

    # populate the playlist based on these songs
    playlist = populate_playlist(filepath)

    # This is how to iterate through the playlist
    for song in playlist:

        # you can print the whole song like this
        print(song.get_song_as_string())
        # you can access individual data like this
        print(song.title)



def populate_playlist(filepath):

    # set up an empty playlist
    playlist = []

    # open the file
    with open(filepath) as file:

        # for each line in the file
        for line in file:

            # split the data by the " | " delimiter making a list of data
            data = line.strip().split(" | ")

            # take this list of song data and create a new song in our playlist
            playlist.append(Song(data[0], data[1], data[2], data[3], data[4], data[5]))

    return playlist

main()
