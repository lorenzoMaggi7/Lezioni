class Persona:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.età = Persona.età
        if self.first_name != str:
            self.first_name == None
            print("Il nome inserito non è una stringa")
        if self.last_name != str:
            self.last_name == None
            print("Il nome inserito non è una stringa")
        if self.first_name and self.last_name != str:
            self.età == None
        if self.first_name and self.last_name == str:
            self.età == 0

    def setName(self,first_name):
        if type(first_name) == str:
            self.first_name = first_name
        else:
            print("Il nome inserito non è una stringa")

    def setLatName(self, last_name):
        if type(last_name) == str:
            self.last_name = last_name
        else:
            print("Il cognome inserito non è una stringa")

    def setAge(self, age):
        if type(age) == int:
            self.age = age
        else:
            print("L'età deve essere un intero")

    def getName(self):
        print(self.first_name)
    
    def getLastName(self):
        print (self.last_name)
    
    def getAge(self):
        print (self.age)
    
    def greet(self):
        print (f"Ciao, sono {self.first_name} {self.last_name}! Ho {self.age} anni!")
    


           
        
            
