from Song import Song

# set the default sorting value to the title
#static = Song.album

def PythonSort(playlist):

	# This is how to iterate through the playlist
    for song in playlist:

        # you can print the whole song like this
        print(song.get_song_as_string())
        # you can access individual data like this
        print(song.title)

	#outlist = sorted(playlist, key=lambda song: song.title)
	
	#print(outlist)
	#return outlist
	
	

def InsertionSort(playlist):
    # TODO: implementation for InsertionSort


    return playlist

def BubbleSort(playlist):
    # TODO: implementation for BubbleSort

    return playlist

def SelectionSort(playlist):
    # TODO: implementation for SelectionSort


    return playlist

def ShellSort(playlist):
    # TODO: implementation for ShellSort


    return playlist
	
"""def setLambda(data):
	if data == "1":
		value = Song.title
	if data == "2":
		value = Song.artist
	if data == "3":
		value = Song.album
	if data == "4":
		value = Song.genre
	if data == "5":
		value = Song.year
	if data == "6":
		value = Song.rank
		
	return value	"""
	
"""

Heres a code snippet using a lambda function for sorting

>>> student_objects = [
...     Student('john', 'A', 15),
...     Student('jane', 'B', 12),
...     Student('dave', 'B', 10),
... ]
>>> sorted(student_objects, key=lambda student: student.age)   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]


"""
