"""
1. Create a Playlist:

Write a function called create_playlist() that accepts a playlist name and a variable number of song titles. 
The function should return a dictionary with the playlist name and a set of songs. Call the function with different numbers of songs to demonstrate flexibility.

Example: create_playlist("Road Trip", {"Song 1", "Song 2"})

Write a function called add_like() that accepts a dictionary, the name of a playlist, 
and a boolean value indicating whether it is liked (True or False). This function should return an updated dictionary.
Example: add_like(dictionary, “Road Trip”, liked=True)
"""

def create_playlist(name, songs):
    playlist = {"name": name, "songs": set(songs)}
    return playlist

def add_like(dictionary, playlist_name, liked=True):
    for playlist in dictionary:
        if playlist["name"] == playlist_name:
            playlist["liked"] = liked
            break
    return dictionary

playlist1 = create_playlist("Fiera di paese", {"Cicirinela", "Halleluja"})
print(playlist1)

playlist2 = create_playlist("Gym Mix", {"King supreme", "Yummi", "TOO HAPPY"})
print(playlist2)

playlists = [playlist1, playlist2]

playlists = add_like(playlists, "Road Trip", liked=True)
print(playlists)

playlists = add_like(playlists, "Gym Mix", liked=False)
print(playlists)
print(" ")

"""
2. Book Collection:

Write a function called add_book() that accepts an author's name and a variable number of book titles authored by them. 
This function should return a dictionary where the author's name is the key and the value is a list of their books. 
Demonstrate this function by adding books for different authors.

Example: add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])

Write a function called delete_book() that accepts a dictionary and the name of the author from whom to remove all details. 
This function should return an updated dictionary.

Example: delete_book(dictionary, “Mark Twain”)
"""
def add_book(author, books):
    book_collection = {}
    book_collection[author] = list(books)
    return book_collection

def delete_book(dictionary, author):
    if author in dictionary:
        del dictionary[author]
    else:
        print(f"The author '{author}' does not exist in the book collection.")
    return dictionary

book_collection = add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])
print(book_collection)

book_collection = add_book("Jane Austen", ["Pride and Prejudice", "Sense and Sensibility"])
print(book_collection)

book_collection = delete_book(book_collection, "Mark Twain")
print(book_collection)


"""

"""