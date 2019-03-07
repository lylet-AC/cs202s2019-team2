from PlaylistProcessor import populate_playlist
from PlaylistSorter import *


if __name__ == '__main__':

    # input for the program
    algorithm = input("Please enter a number for an algorithm:\n  1.) InsertionSort\n  2.) BubbleSort\n  3.) SelectionSort\n  4.) ShellSort\nEntry: ")
    sort_what = input("Please enter a number for what to sort:\n  1.) Title\n  2.) Artist\n  3.) Album\n  4.) Genre\n  5.) Year\n  6.) Rank\nEntry: ")

    # set up the location of the songlist
    filepath = "../data/songlist.txt"

    # populate the playlist based on these songs
    playlist = populate_playlist(filepath)

    # depending on algorithm and sort_what make calls to the sort functions
    if algorithm == "1":
        InsertionSort(playlist, sort_what)

    elif algorithm == "2":
        BubbleSort(playlist, sort_what)

    elif algorithm == "3":
        SelectionSort(playlist, sort_what)

    elif algorithm == "4":
        ShellSort(playlist, sort_what)

    else:
        print("You have entered an invalid algorithm!")
