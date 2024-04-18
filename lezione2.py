# Lorenzo Maggi
#18/04/2024

#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person.
#Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

x = str(input())
mex: str = f"Ciao {x}, ti va di imparare python?"
print(mex)

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

#2-5/2.6. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following,
#including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”
vip:str =input()
frase:str =input()
print(f'{vip} once said,"{frase}"')

#2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. 
#Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.
filename:str = "python_notes.txt"
print(filename.removesuffix(".txt"))

#3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
names:list = ("lorenzo", "osama", "danila")
print(names[0])
print(names[1])
print(names[2])

#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them.
#The text of each message should be the same, but each message should be personalized with the person’s name.
print(f"Ciao {names[0]} come stai?")
print(f"Ciao {names[1]} come stai?")
print(f"Ciao {names[2]} come stai?")
