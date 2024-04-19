# Lorenzo Maggi
#18/04/2024

#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person.
#Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

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
vip:str =input()
frase:str =input()
print(f'{vip} once said,"{frase}"')
print("\n")
#2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. 
#Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.
filename:str = "python_notes.txt"
print(filename.removesuffix(".txt"))
print("\n")
#3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
names:list = ("lorenzo", "osama", "danila")
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




