"""

def substract(a:float,b:float):
    x = a-b
    return x
a=23
b=12.45
print(substract(a, b))


USIAMO UN FOR


def sum(l:list[float]) -> float :
    somma = 0
    for elem in l:
        somma += elem
    return somma

result = sum([1,2,3,4,5.66,546564,67.060606060,-123])

USIAMO UN WHILE

def sum(l:list[float]) -> float :
    somma = 0
    while i < len(l):
        somma += l[i]
        i += 1
    return somma

result = sum([1,2,3,4,5.66,546564,67.060606060,-123])

i:int = int(input())
def check_value(i: int):
    if i > 5:
        print(f"{i} is bigger than 5")
    elif i < 5:
        print(f"{i} is smaller than 5")
    else:
        print(f"{i} is equal to 5")
check_value(i)


##############
x:str = str(input())

def check_lenght(x: str):
    if len(x) > 10:
        print(f"{x} is longer than 10 characters")
    elif len(x) < 10:
        print(f"{x} is shorter than 10 characters")
    else:
        print(f"{x} is equal to 10 characters")
check_lenght(x)


###############

def print_numbers(p:list):
    for v in p:
        print(v)
        
print_numbers([1,2,3,4,5,6,7,8,9])

##############
def check_each(w:list):
    for r in w:
        
        if r > 5:
            print(f"{r} is bigger than 5")
        elif r < 5:
         print(f"{r} is smaller than 5")
        else:
            print(f"{r} is equal to 5")
check_each([23,54,1,2,3,54,2,8,9])

"""

"""
8-1. Message: 
Write a function called display_message(), 
that prints one sentence telling everyone what you are learning about in this chapter. 
Call the function, and make sure the message displays correctly.
"""
def display_message():
    print("In this chapter, we are learning about functions in Python.")

display_message()
print(" ")
"""
8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. 
The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
Call the function, making sure to include a book title as an argument in the function call.
"""
def favorite_book(title):
    print(f"My favorite book is {title}")

favorite_book("Death note")

"""
8-3. T-Shirt: 
Write a function called make_shirt() 
that accepts a size and the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it. 
Call the function once using positional arguments to make a shirt. 
Call the function a second time using keyword arguments.
"""
def make_shirt(size, message):
    print(f"The size of the shirt is {size}, and the message write on it is {message}")

make_shirt("M", "Daje Roma")
print(" ")
"""
8-4. Large Shirts: 
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, 
and a shirt of any size with a different message.
"""
def make_shirt(size="large", message="I love Python"):
    print(f"Shirt size: {size.title()}, Message: {message}")
make_shirt()
make_shirt(size="medium")
make_shirt(size="small", message="Ciao")
print(" ")
"""
8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. 
The function should print a simple sentence, such as Reykjavik is in Iceland. 
Give the parameter for the country a default value. 
Call your function for three different cities, at least one of which is not in the default country.
"""

def describe_city(name, country="Country"):
    print(f"{name} is in {country}")
describe_city("Rome","Italy")
describe_city("Acapulco","Messico")
describe_city("Dubai")
print(" ")
"""
8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. 
The function should return a string formatted like this: "Santiago, Chile". 
Call your function with at least three city-country pairs, and print the values that are returned.
"""
def city_country(city, country):
    print(f"{city},{country}")
city_country("Rome","Italy")
city_country("Milano","Italy")
city_country("Las Palmas","Spain")
print(" ")

"""
8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
The function should take in an artist name and an album title, 
and it should return a dictionary containing these two pieces of information. 
Use the function to make three dictionaries representing different albums. 
Print each return value to show that the  dictionaries are storing the album information correctly. 
Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
Make at least one new function call that includes the number of songs on an album.
"""
def make_album(name, album_name,songs=None):
    album:dict = {"artist" : name, "title" : album_name}
    if songs:
        album["numbers of songs"] = songs
    return album
album1 = make_album("Travis Scott", "Utopia")
album2 = make_album("Pino Daniele", "Nero a metà", 12)
album3 = make_album("Starjunk 95", "Visual Paradise", 4)

print(album1)
print(album2)
print(album3)
print(" ")

"""
8-8. User Albums: Start with your program from Exercise 8-7. 
Write a while loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
Be sure to include a quit value in the while loop.
"""
def make_album(name, title, songs=None):
    album = {'artist': name, 'title': title}
    if songs:
        album['number_of_songs'] = songs
    return album

while True:
    artist = input("Enter the artist's name (or 'stop' to exit): ")
    if artist.lower() == "stop":
        break
    title = input("Enter the album title: ")
    number_of_songs = input("Enter the number of songs on the album (optional): ")
    
    if number_of_songs.isdigit(): 
        number_of_songs = int(number_of_songs)
    else:
        number_of_songs = None
    
    album = make_album(artist, title, number_of_songs)
    print(album)
print(" ")

"""
8-9. Messages: Make a list containing a series of short text messages. 
Pass the list to a function called show_messages(), which prints each text message.
"""
def show_messages(messages:list):
    for message in messages:
        print(message)
messages = ["Ciao","Anvedi","Come va?","Na crema"]
show_messages(messages)
print(" ")

"""
8-10. Sending Messages: 
Start with a copy of your program from Exercise 8-9. 
Write a function called send_messages() that prints each text message 
and moves each message to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages were moved correctly.
"""
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)

messages = ["Ciao","Anvedi","Come va?","Na crema"]

sent_messages = []

send_messages(messages, sent_messages)

print("\nOriginal messages:")
show_messages(messages)
print("\nSent messages:")
show_messages(sent_messages)
print(" ")
"""
8-11. Archived Messages: Start with your work from Exercise 8-10. 
Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the original list has retained its messages.
"""
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)

messages = ["Ciao","Anvedi","Come va?","Na crema"]

messages_copy = messages[:]

sent_messages = []

send_messages(messages_copy, sent_messages)

print("\nOriginal messages:")
show_messages(messages)
print("\nSent messages:")
show_messages(sent_messages)
print(" ")

"""
8-12. Sandwiches: 
Write a function that accepts a list of items a person wants on a sandwich. 
The function should have one parameter that collects as many items as the function call provides, 
and it should print a summary of the sandwich that’s being ordered. 
Call the function three times, using a different number of arguments each time.
"""
def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print("- " + item)

make_sandwich("Ham", "Cheese", "Lettuce")
make_sandwich("Turkey", "Brie", "Tomato", "Mayonnaise")
make_sandwich("Nutella", "Philadelphia")
print(" ")
"""
8-13. User Profile:  
Build a profile of yourself by calling build_profile(), 
using your first and last names and three other key-value pairs that describe you. 
All the values must be passed to the function as parameters. 
The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
"""
def build_profile(first_name,last_name,particular_signs,age,height):
    profile = f"{first_name} {last_name}, age {age}, particular signs {particular_signs}, height {height}"
    return profile

my_profile = build_profile("Lorenzo", "Maggi", age=22, particular_signs="tattoo", height=180)

print(my_profile)
print(" ")

"""
8-14. Cars: 
Write a function that stores information about a car in a dictionary. 
The function should always receive a manufacturer and a model name. 
It should then accept an arbitrary number of keyword arguments. 
Call the function with the required information and two other name-value pairs, 
such as a color or an optional feature. Your function should work for a call like this one: 
car = make_car('subaru', 'outback', color='blue', tow_package=True) 
Print the dictionary that’s returned to make sure all the information was stored correctly. 
"""
def cars(name, model, color, tow_package=False):
    make_car:dict = {"name" : name, "model" : model, "color" : color, "tow_package" : tow_package}
    return make_car
car= cars("subaru", "baracca", color="blue", tow_package=True)
print(car)
print(" ")
"""
8-15. Printing Models: 
Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
"""
from printing_models import print_models, show_completed_models

unprinted_designs = ["phone case", "giovanni's robot", "luffy's strawhat"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(" ")
"""
8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. 
Import the function into your main program file, and call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
"""
import book
favorite_book.book("Bleach")

from book import book
book("Naruto")

from book import book as custom_book
custom_book("Steel ball run")

import book as bk
bk.book("Mashle")

from book import *
book("Blue lock")
print(" ")

"""
8-17. Styling Functions: 
Choose any three programs you wrote for this chapter, 
and make sure they follow the styling guidelines described in this section.
"""

def favorite_book(title):
    """Prints a message about a favorite book."""
    print(f"One of my favorite books is {title}\n")

favorite_book("Death note")

########################################################
def make_shirt(size, message):
    """Prints a summary of the shirt size and message."""
    print(f"The shirt size is {size} and the message printed on it is: {message}\n")

make_shirt("M", "Daje Roma")

make_shirt(size="L", message="Bella pe te")

#######################################################
def display_message():
    """Prints a message about what I am learning in this chapter."""
    print("In this chapter, I am learning about functions in Python")

display_message()
