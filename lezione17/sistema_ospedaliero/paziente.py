from persona import Persona

class Paziente(Persona):

    def __init__(self, first_name, last_name, age, idCode:str) -> None:
        super().__init__(first_name, last_name, age)
        self.codice = idCode

    def setIdCode(self,idCode):
        self.codice = idCode

    def getidCode(self):
        print(self.codice)

    def patientInfo(self):
        print(f"Paziente:{self.first_name} {self.last_name} /n ID :{self.codice}")


        