# Lorenzo Maggi
#18/04/2024

#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person.
#Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”


from collections import defaultdict


x = str(input())
mex: str = f"Ciao {x}, ti va di imparare python?"
print(mex)
print("\n")
#2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

y =str(input())
#questa variabile contiene il nome in minuscolo
minuscolo:str = y.lower()
#questa variabile contiene il nome in maiuscolo
maiuscolo:str = y.upper()
#questa variabile contiene il nome in title
titolo:str = y.title()
print(minuscolo)
print(maiuscolo)
print(titolo)
print("\n")
#2-5/2.6. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following,
#including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”
vip:str =input("Name of a famous person: ")
frase:str =input("This persone said: ")
print(f'{vip} once said,"{frase}"')
print("\n")
#2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. 
#Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.
filename:str = "python_notes.txt"
print(filename.removesuffix(".txt"))
print("\n")
#3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
names:list = ("lorenzo", "osama", "danilo")
print(names[0])
print(names[1])
print(names[2])
print("\n")
#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them.
#The text of each message should be the same, but each message should be personalized with the person’s name.
print(f"Ciao {names[0]} come stai?")
print(f"Ciao {names[1]} come stai?")
print(f"Ciao {names[2]} come stai?")
print("\n")
#3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
#Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
cars:list =("Porsche 911", "Toyota Supra", "Ferrari Roma")
print(f"I would like to own a {cars[0]}")
print(f"I would like to buy a {cars[1]}") 
print(f"I would like to drive a {cars[2]}")
print("\n")
#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
#Make a list that includes at least three people you’d like to invite to dinner.
#Then use your list to print a message to each person, inviting them to dinner.
people:list = ["Michael Jackson", "Diego Armando Maradona", "Francesco Totti"]
print(f"Hi {people[0]},i would like to have you at my dinner")
print(f"Hola {people[1]},me gustaría invitarte a cenar esta noche ")
print(f"Ciao {people[2]}, sta sera cenone da me?")
print("\n")
"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.
"""
print(f"I'm sorry guys, but {people[0]} can't come tonight")
people.pop(0)
people.append("Steve Jobs")
print(f"Hi {people[2]}, sorry to call you at the last minute, i would like to have you at my dinner")
print(f"Hola {people[0]}, cuento contigo para esta noche")
print(f"Ao {people[1]}, sta sera ce devi sta")
print("\n")
      
"""
3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
"""
print(f"Hi {people}, i've just found a bigger table, so i'm gonna call more people for the dinner")
print("\n")
people.insert(0, "Lionel Messi")
people.insert(2, "Micheal Jordan")
people.append("Antonio Cassano")
for i in people:
    print(f"Hi {i},tonight we are gonna have fun")
print("\n")


"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list,
 print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list.
Print your list to make sure you actually have an empty list at the end of your program.
"""

print(f"Guys, i'm sorry but i only can invite just 2 people tonight")
print(f"{people[0]}, lo siento pero no puedo tenerte esta noche")
people.pop(0)
print(f"{people[0]}, lo siento pero no puedo tenerte esta noche")
people.pop(0)
print(f"{people[0]}, i'm sorry but i can't have you tonight")
people.pop(0)
print(f"{people[1]}, i'm sorry but i can't have you tonight")
people.pop(1)
print(f"{people[0]}, sta sera ce stamo io te e antonio, se divertimo")
print(f"{people[1]}, sta sera ce stamo io te e francesco, se divertimo")
print("\n")
people1 = people
del people[0:2]
print(people)
print("\n")


"""
3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed.
"""
places: list = ["Japan","Indonesia","Scotland","Kenya","Brasil"]
print(places)
places1 = sorted(places)
print(places1)
print(places)
places2 = sorted(places, reverse=True)
print(places2)
print(places)
places.reverse()
print(places)
places.reverse()
places.sort()
print(places)
places.sort(reverse=True)
print(places)

print("\n")

#3-9. Dinner Guests: Working with one of the programs from Exercises 3, use len() to print a message indicating the number of people you’re inviting to dinner.

print(f"The number of guests that i'm inviting to dinner is {len(people1)}")



#3-10. Every Function: Think of things you could store in a list.
#For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like.
#Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
colors:list = ["red","blue","yellow","purple","green","lilac","brown","white"]
[colors.lower() for colors in colors[0:]]
print(colors)
[colors.upper() for colors in colors[0:]]
print(colors)
[colors.title() for colors in colors[0:]]
print(colors)
print(f"To me {colors[5]} is the best color ever ")
print(f"{colors[5]} is darker than {colors[-1]}")
colors.reverse()
print(colors)
colors.sort()
print(colors)
colors.pop(0)
print(colors)
colors.append("black.txt")
print(colors[-1])
for i in range(len(colors)):
    if colors[i].endswith(".txt"):
        colors[i] = colors[i].removesuffix(".txt")
        print(colors)
    continue

print(colors)
colors.insert(0,"cyan")
print(colors)
del colors[1:3]
print(colors)
print("\n")

"""
6-1. Person: Use a dictionary to store information about a person you know. 
Store their first name, last name, age, and the city in which they live. 
You should have keys such as first_name, last_name, age, and city. 
Print each piece of information stored in your dictionary.
"""
person:dict={
    "first_name" : "Lorenzo",
    "last_name" : "Maggi",
    "age" : 22,
    "city" : "Roma"
    }
print(person)
print("\n")
"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. 
Think of a favorite number for each person, and store each as a value in your dictionary. 
Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.
"""
favorite_number:dict={"Lorenzo" :[ 7], "Osama" : [3], "Danila" : [18], "Gaia" : [12], "Giovanni" : [90]}
print(favorite_number)
print("\n")

"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, 
or print the word on one line and then print its meaning indented on a second line. 
Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
"""
Glossary:dict={
    "insert: " : "To insert elements into a list in Python, you can use the insert() method.",
    "append: " : "To append elements to a list in Python, you can use the .append() method.",
    "sort: " : "In Python, you can sort a list using the sorted() function or the sort() method.",
    "pop: " : "In Python, the pop() method is used to remove and return the element at a specific index from a list.",
    "remove: " : "In Python, the remove() method is used to remove the first occurrence of a specified element from a list."
}
for key,value in Glossary.items():
    print(key, value)
    print()

"""
6-7. People: Start with the program you wrote for Exercise 6-1. 
Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
Loop through your list of people. As you loop through the list, print everything you know about each person
"""

new_people:dict={
    "first_name" : "Andrea",
    "last_name" : "Barbato",
    "age" : 27,
    "city" : "Roma" 
}
other_people:dict={
    "first_name" : "Francesco",
    "last_name" : "Palombi",
    "age" : 22,
    "city" : "Roma"
}


people = defaultdict(list)

for d in (person, new_people, other_people):
    for key, value in d.items():
        people[key].append(value)

people = dict(people)

print(people)
print()



"""
6-8. Pets: Make several dictionaries, where each dictionary represents a different pet.
In each dictionary, include the kind of animal and the owner’s name. 
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet. 
"""
animal1:dict = {
    "animal1" : "Dog",
    "dog_race" : "Bulldog",
    "owners_name" : "Sandra",
    }
animal2:dict = {"animal" : "Fish",
    "fish_race" : "clownfish",
    "owners_name" : "Osama"
    }
animal3:dict = {
    "animal" : "Horse",
    "horse_race" : "Mustang",
    "owners_name" : "Carlo"
}

pets:list = []

pets.append(animal1)
pets.append(animal2)
pets.append(animal3)

print(pets)

"""
6-9. Favorite Places: Make a dictionary called favorite_places. 
Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. 
Loop through the dictionary, and print each person’s name and their favorite places
"""

favorite_places:dict = {
    "Lorenzo" : {"Japan","Spain","Uganda"},
    "Osama" : {"Morocco", "Italy", "Portugal"},
    "Danila" : {"Canada","Argentina", "Belarus"}
}

for person, places in favorite_places.items():
    print(f"{person}'s favorite places:")
    for place in places:
        print("- " + place)
    print()  

"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
Then print each person’s name along with their favorite numbers.
"""

favorite_number["Danila"].append(42)
favorite_number["Gaia"].append(3)
favorite_number["Giovanni"].append(2)
favorite_number["Lorenzo"].append(10)

print(favorite_number)
print()

"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. 
The keys for each city’s dictionary should be something like country, population, and fact. 
Print the name of each city and all of the information you have stored about it.
"""
cities:dict = {"Roma" : {"Country" : "Italy","population" : "2873000", "fact" : "Rome is beeautifull"},
               "Sidney": {"Country": "Australia", "population" : "5300000", "fact" : "Sidney is the fifth most expensive in the world"},
               "Nice" : {"Country" : "France","population" : "342522", "fact" : "A cannon shoot for lunch every day"}
               }
print(cities["Roma"])
print()
print(cities["Sidney"])
print()
print(cities["Nice"])
print()

"""
6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways.
Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, 
or improving the formatting of the output.
"""

def add_favorite_places():
    person = input("Enter the name of the person: ")
    places = input("Enter their favorite places separated by commas: ").split(",")
    places = [place.strip() for place in places]
    if person in favorite_places:
        if isinstance(favorite_places[person], set):
            favorite_places[person] = list(favorite_places[person])  
        favorite_places[person].extend(places)
    else:
        favorite_places[person] = places

add_more = input("Do you want to add more favorite places? (yes/no): ").lower()
while add_more == "yes":
    add_favorite_places()
    add_more = input("Do you want to add more favorite places? (yes/no): ").lower()

print("\nFavorite Places:")
for person, places in favorite_places.items():
    print(f"{person}'s favorite places:")
    for place in places:
        print(f"- {place}")
    print()
    
