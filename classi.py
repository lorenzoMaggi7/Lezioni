"""
class Person:
# name
# surname
# age

    def __init__(self, name:str, surname:str, age:int ):
        self.name = name
        self.surname = surname
        self.age = age

lorenzo = Person("Lorenzo", "Maggi", 24)
print(f"Nome = {lorenzo.name}, Cognome = {lorenzo.surname}, Età = {lorenzo.age}")
lorenzo.age = 22
print(f"Età = lorenzo.age")


danila = Person("Danila","Rahautsou", 21)
print(f"Nome = {danila.name}, Cognome = {danila.surname}, Età = {danila.age}")


name : str = input()
surname : str = input()
age : int = int(input())

person = Person(name,surname,age)
print(f"Nome = {person.name}, Cognome = {person.surname}, Età = {person.age}")

persons = [Person("Lorenzo", "Maggi", 24), Person("Danila","Rahautsou", 21), Person("Oussama", "Hliwa", 22)]
avg_age = 0
for person in persons:
    avg_age += person.age
avg_age /= len(persons)
print(f"Età media = {avg_age}")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hobbies : set[str] = []


    def add_hobbies(self, hobbies:set[str]):
        self.hobbies.update(hobbies)
        
    def add_hobby(self, hobby:str):
        self.hobbies.add(hobby)

    def remove_hobby(self, hobby : str):
        if hobby in self.hobbies:
            self.hobbies.remove(hobby)

    def __str__(self) -> str:
        return f"Person(name={self.name}, age = {self.age}, hobbies = {self.hobbies})"
    



alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)
print(f"Age = {bob.age}")
if alice.age > bob.age:
    print(f"Alice is {alice.age}, so it's older than bob")


alice.add_hobby("Pallacanestro")
print(alice)
alice.remove_hobby("Pallacanestro")
alice.add_hobbies(["Pallacenstro","Rugby","Cricket"])
print(alice)


osama = Person("Osama H.", 22)
giovanni = Person("Giovanni D.", 24)
frenk = Person("Frenk B.", 20)

people: list = [Person("Osama H.", 22),
          Person("Giovanni D.", 24),
          Person("Frenk B.", 20),
          Person("Alice W.", 45),
          Person("Bob M.", 36)]



#
ages = float("inf")
name1:list= []
for age in people:
    if ages > age.age:
        ages = age.age
        name1.append(age.name)

print(name1[-1])
#



min_age = float("inf")
index_min_age = 0
for i, person in enumerate(people):
    if person.age < min_age:
        min_age = person.age
        index_min_age = i

person= people[index_min_age]
print(f"La persona piu giovane è {person}")

"""
"""
###################################################################################

class Student:
    def __init__(self,name:str, studyProgram:str):
        self.name = name
        self.studyProgram = studyProgram
        self.age = int
        self.gender = str
        #self.age = None
        #self.gender = None


    def add_age_gender(self):
        self.age = int(input("inserisci la tua età: "))
        self.gender = (input("Inserisci il tuo genere: "))

    
#####         COME LO FAREBBE IL PROF          #####

    def set_age(self, new_age: int)
        self.age = new_age
    
        
    def set_gender(self, new_gender: str):
        self.gender = new_gender


    



    def __str__(self) -> str:
        return f"Person(name={self.name}, study program = {self.studyProgram}, età = {self.age}, genere = {self.gender})"



lorenzo = Student("Lorenzo", "Fullstack")
oussama = Student("Oussama", "Cyber")
lorenzoT = Student("Lorenzo", "Cloud")

print(lorenzo)
print(oussama)
print(lorenzoT)

####### PROF #######

lorenzo.set_age(22)
lorenzo.set_gender(M)
print(lorenzo)



lorenzo.add_age_gender()
print(lorenzo)
oussama.add_age_gender()
print(oussama)
lorenzoT.add_age_gender()
print(lorenzoT)




###################################################################
@classmethod
def get_avg_grade(cls):
    return 0
"""


"""


Though classmethod and staticmethod are quite similar, there's a slight difference in usage for both entities: 
classmethod must have a reference to a class object as the first parameter, whereas staticmethod can have no parameters at all.
Example

class Date(object):
    
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

date2 = Date.from_string('11-09-2012')
is_date = Date.is_date_valid('11-09-2012')

Explanation

Let's assume an example of a class, dealing with date information (this will be our boilerplate):

class Date(object):
    
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

This class obviously could be used to store information about certain dates (without timezone information; let's assume all dates are presented in UTC).

Here we have __init__, a typical initializer of Python class instances, which receives arguments as a typical instance method, 
having the first non-optional argument (self) that holds a reference to a newly created instance.

Class Method

We have some tasks that can be nicely done using classmethods.

Let's assume that we want to create a lot of Date class instances having date information coming from an outer source encoded as a string with format 'dd-mm-yyyy'. 
Suppose we have to do this in different places in the source code of our project.

So what we must do here is:

    Parse a string to receive day, month and year as three integer variables or a 3-item tuple consisting of that variable.
    Instantiate Date by passing those values to the initialization call.

This will look like:

day, month, year = map(int, string_date.split('-'))
date1 = Date(day, month, year)

For this purpose, C++ can implement such a feature with overloading, but Python lacks this overloading. Instead, we can use classmethod. 
Let's create another constructor.

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

date2 = Date.from_string('11-09-2012')

Let's look more carefully at the above implementation, and review what advantages we have here:

    We've implemented date string parsing in one place and it's reusable now.
    Encapsulation works fine here (if you think that you could implement string parsing as a single function elsewhere, this solution fits the OOP paradigm far better).
    cls is the class itself, not an instance of the class. It's pretty cool because if we inherit our Date class, all children will have from_string defined also.

"""
"""
class Animal:
    def __init__(self,name:str, legs: int):
        self.name = name
        self.legs = legs

    def setLegs(self):
        self.legs = int(input("Inserisci il numero di zampe dell'animale: "))


    def getLegs(self):
        return self.legs 
        

    def __str__(self) -> str:
        return f"nome={self.name.capitalize()}, numero zampe = {self.legs})"

gatto = Animal("Gatto", 4)
ragno = Animal("Ragno", 8)
print(gatto.name, gatto.legs)
print(ragno.name, ragno.legs)

ragno.legs = 6
print(ragno.legs)

ragno.setLegs()
print(ragno)

print(gatto.getLegs())
print(ragno.getLegs())

"""

class Food:
    def __init__(self, name:str, price:float, description:str):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self) -> str:
        return f"{self.name.capitalize()}(price{self.price}, descr = {self.description})"




class Menu:
    def __init__(self, Foods:list[Food] = []):
        self.Foods: list[Food] = Foods

    def addFood(self,new_menu:Food):
        self.Foods.append(new_menu)

    def removeFood(self,latest_menu:Food):
        if latest_menu in self.Foods:
            self.Foods.remove(latest_menu)

    def __str__(self) -> str:
        repr: str = ""
        for food in self.Foods:
            repr += "\n" + food.__str__()
        return repr[1:]    


carbonara:Food = Food("Carbonara", 12, "pasta con guanciale, uovo, pecorino e pepe"),
margherita:Food = Food("Margherita", 8, "pizza margherita con pomodoro e mozzarella"),
gelato:Food = Food("Gelato", 3, "gelato al gusto menta e cioccolato")

menu = Menu()
menu.addFood(carbonara)
menu.addFood(gelato)
print(menu.Foods)
"""
## o anche
menu = Menu[carbonara, gelato, margherita]
"""
menu.removeFood(carbonara)
print(menu)