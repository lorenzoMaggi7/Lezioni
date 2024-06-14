from dottore import Dottore
from paziente import Paziente
class Fattura(Dottore, Paziente):
    def __init__(self, patient:list[Paziente], doctor:Dottore) -> None:
        self.patient = patient
        self.doctor = doctor
        self.salary = int
        self.fatture = int
        self.doctor.isAValidDoctor()
        if self.doctor.isAValidDoctor() == True:
            self.fatture == len(patient)
            self.salary == 0
        else:
            self.patient,self.doctor,self.salary,self.fatture == None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getSalary(self):
        return self.parcel * len(self.patient)
    
    def getFatture(self):
        self.fatture == len(self.patient)
        return self.fatture
    
    def addPatient(self, newPatient:Paziente):
        self.patient.append(newPatient)
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del Dottor {self.last_name} è stato aggiunto il paziente {self.codice}")

    def removePatient(self,idCode:Paziente):
        for paziente in self.patient:
            if paziente.codice == idCode:
                self.patient.remove(self.codice)
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del Dottor {self.last_name} è stato rimosso il paziente {self.codice}")
        