from persona import Persona

class Dottore(Persona):
    def __init__(self,first_name, last_name, specialization:str, parcel: float) -> None:
        super().__init__(first_name, last_name)
        self.specialization = specialization
        self.parcel = parcel
        if self.specialization != str:
            self.specialization == None
            print("La specialization non è una stringa")
        if self.parcel != float:
            self.parcel == None
            print("La parcel non è un float")
        
    def setspecialization(self, specialization):
        if type(self.specialization) == str:
            self.specialization = specialization
        else:
            print("La specializzazione inserita non è una stringa")

    def setParcel(self, parcel):
        if type(self.parcel) == float:
            self.parcel = parcel
        else:
            print("La parcella inserità non è un float")
    
    def getSpecialization(self):
        print(self.specialization)

    def getParcel(self):
        print(self.parcel)

    def isAValidDoctor(self):
        if self.age >= 30:
            print(f"{self.first_name} {self.last_name} is valid!")
        else:
            print(f"{self.first_name} {self.last_name} is not valid!")

    def doctorGreet(self):
        self.greet()
        print(f"Sono un medico {self.specialization}")