from PlaylistProcessor import populate_playlist
from PlaylistSorter import *
from Song import Song

if __name__ == '__main__':

    # input for the program
    algorithm = input("Please enter a number for an algorithm:\n  1.) InsertionSort\n  2.) BubbleSort\n  3.) SelectionSort\n  4.) ShellSort\nEntry: ")
    sort_what = input("Please enter a number for what to sort:\n  1.) Title\n  2.) Artist\n  3.) Album\n  4.) Genre\n  5.) Year\n  6.) Rank\nEntry: ")

    # set up the location of the songlist
    filepath = "../data/songlist.txt"

    # populate the playlist based on these songs
    playlist = populate_playlist(filepath)

    # set the lambda function depending on what we want to sort
    #setLambda(sort_what)
	
    # depending on algorithm and sort_what make calls to the sort functions
    if algorithm == "1":
        InsertionSort(playlist)

    elif algorithm == "2":
        BubbleSort(playlist)

    elif algorithm == "3":
        SelectionSort(playlist)

    elif algorithm == "4":
        ShellSort(playlist)
	
    elif algorithm == "5":
        PythonSort(playlist)

    else:
        print("You have entered an invalid algorithm!")
