from Song import Song


def PythonSort(playlist, attr):
    """Learning experience using the built in python sort"""

    outlist = sorted(playlist, key=lambda song: getattr(song,value))

    for song in outlist:
        print(song.get_song_as_string())

    return outlist

def InsertionSort(playlist, attr):
    """Insertion sort method"""

    for i in range(1, len(playlist)):

        song1 = playlist[i]
        value1 = getattr(playlist[i], attr)
        j = i-1

        while j >= 0 and value1 < getattr(playlist[j], attr):
            playlist[j+1] = playlist[j]
            j -= 1
        playlist[j+1] = song1

    return playlist

def BubbleSort(playlist, attr):
    """Bubble sort method"""

    return playlist

def SelectionSort(playlist, attr):
    for i in range(len(playlist)):
        minIndex=i
        attrI = getattr(playlist[minIndex],attr)
        attrT = getattr(playlist[i], attr)
        for j in range(i+1, len(playlist)):
            if attrT < getattr(playlist[j], attr):
                if attrI > getattr(playlist[j], attr):
                    minIndex = j
        playlist[i], playlist[minIndex] = playlist[minIndex], playlist[i]
    return playlist

def ShellSort(playlist, attr):
    l = len(playlist)
    gap = l//2
    while gap > 0:
        for i in range(gap,l):
            temp = playlist[i]
            j=i
            while j >= gap and getattr(playlist[j-gap],attr) > getattr(temp,attr):
                playlist[j] = playlist[j-gap]
                j-= gap
            playlist[j] == temp
        gap//=2
    return playlist


def setLambda(data):
    if data == "1":
        value = "title"

    elif data == "2":
        value = "artist"

    elif data == "3":
        value = "album"

    elif data == "4":
        value = "genre"

    elif data == "5":
        value = "year"

    elif data == "6":
        value = "rank"

    else:
        value = "title"

    return value
