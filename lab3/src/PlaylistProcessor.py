from Song import Song


def populate_playlist(filepath):

    # set up an empty playlist
    playlist = []

    try:
        # open the file
        with open(filepath) as file:

            # for each line in the file
            for line in file:

                # split the data by the " | " delimiter making a list of data
                data = line.strip().split(" | ")

                # take this list of song data and create a new song in our playlist
                playlist.append(Song(data[0], data[1], data[2], data[3], data[4], data[5]))

    except BaseException as e:
        print("Reading the file has encountered an error.")
        print(e)

    return playlist

def dump_playlist(filepath, playlist):

    try:
        # open the file to place songs
        file = open(filepath, "w")

        # This is how to iterate through the playlist
        for song in playlist:

            # you can print the whole song like this
            print(song.get_song_as_string())
            file.write(song.get_song_as_string())

        file.close()
        print("Writing the file is complete!")

    except BaseException as e:
        print("Writing the file encountered an error.")
        print(e)
