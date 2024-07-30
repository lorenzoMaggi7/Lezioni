def print_seq(): 
    
    print("Sequenza a):")
    for i in range(1,8):
        print(i)
    print()

    print("Sequenza b):")
    start = 3
    for i in range(5):
        print(start + i * 5)
    print()

    print("Sequenza c):")
    start = 20
    for i in range(6):
        print(start - i * 6)
    print()

    print("Sequenza d):")
    start = 19
    for i in range(5):
        print(start + i * 8)
    print()
    
    return





##################

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    dizio : dict = {}
    for i in dict1.keys():
        if i in dict2.keys():
            dizio[i] = dict1[i]
            dizio[i] += dict2[i]
        else:
            dizio[i] = dict1[i]
            
    for i in dict2.keys():
        if i not in dict1.keys():
            dizio[i] = dict2[i]
            
    return dizio

########################


def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    
    for i,j in dizionario.items():
        if j == valore:
            return i
    return None
        
##############

def sum_above_threshold(numbers: list[int], threshold : int) -> int:
    return sum(num for num in numbers if num > threshold)

######################

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    return {
        prodotto: prezzo * 0.90
        for prodotto, prezzo in prodotti.items()
        if prezzo > 20
    }
   

###################


def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    dizio = {}
    
    for chiave, valore in tuples:
        if chiave in dizio:
            dizio[chiave].append(valore)
        else:
            dizio[chiave] = [valore]
    
    return dizio
##################

def check_access(username: str, password: ..., is_active: bool) -> str:
        if username == "admin" and password == "12345" and is_active:
            return "Accesso consentito"
        else:
            return "Accesso negato"
    
##################

def frequency_dict(elements: list) -> dict:
    freq_dict = {}
    
    for element in elements:
        if element in freq_dict:
            freq_dict[element] += 1
        else:
            freq_dict[element] = 1
    
    return freq_dict

##################

def classifica_numeri(lista: int) -> dict[str:list[int]]:
    risultato = {
        'pari': [],
        'dispari': []
    }
    
    for numero in lista:
        if numero % 2 == 0:
            risultato['pari'].append(numero)  # Corretto: usa append()
        else:
            risultato['dispari'].append(numero)  # Corretto: usa append()
    
    return risultato


####################

def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA or conditionB and conditionC:
        return "Operazione permessa"
    else:
        return "Operazione negata"
    

#####################

def transform(x: int) -> int:
    if x % 2 == 0:
        return x / 2
        
    else:
        return (x * 3) - 1
        

######################


class Veicolo:
    def __init__(self, marca : str, modello : str, anno : int):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")
        
class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte: int):
        super().__init__(marca,modello,anno)
        self.porte = numero_porte
        
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.porte}")
        
class Moto(Veicolo):
    def __init__(self, marca, modello, anno, tipo : str):
        super().__init__(marca,modello,anno)
        self.tipo = tipo
        
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")

###########################