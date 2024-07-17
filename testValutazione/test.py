
print("Esercizi Lezione 5")


# Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e viceversa a seconda del parametro to_fahrenheit. 
# Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit.
def convert_temperature(temperatura, to_fahrenheit=True) -> float:
    if to_fahrenheit:
        fahrenheit = (temperatura * 9/5) + 32
        return fahrenheit
    else:
        celsius = (temperatura - 32) * 5/9
        return celsius


print(convert_temperature(0))
print(convert_temperature(32, False))
print(convert_temperature(100))
print(convert_temperature(212, False))
print(convert_temperature(-42))
print(" ")

# La funzione dovrebbe calcolare la media dei numeri in una lista di interi.
# Un errore nell'implementazione porta a risultati inaspettati.
def calculate_average(numbers: list[int]) -> float:
    if len(numbers) != 0:
        return sum(numbers) / len(numbers)
    else:
        return 0
    

print(calculate_average([1, 2, 3, 4, 5]))
print(calculate_average([]))
print(calculate_average([10, 20, 30]))

	

print(" ")

#Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.

def countdown(n: int) -> int:
    if n >= 0:
        for i in range(n, -1,-1):
            print(i)

    else:
        print("the number must be positive")


 	

countdown(5)
 	
print(" ")

countdown(50)
 	
print(" ")

countdown(1)

print(" ")



#Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. 
#L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. 
#La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.
def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA or (conditionB and conditionC):
        return "operazione riuscita"
    else:
        return "operazione fallita"
    
print(check_combination(True, False, True))
print(check_combination(False, True, True))
print(check_combination(False, False, True))
print(check_combination(True, True, True))
print(" ")


#Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
def remove_duplicates(lista) -> list:
    lista_senza_duplicati = []
    for elemento in lista:
        if elemento not in lista_senza_duplicati:
            lista_senza_duplicati.append(elemento)
    return lista_senza_duplicati
    

 	

print(remove_duplicates([1, 2, 3, 1, 2, 4]))
print(remove_duplicates([4, 5, 'a', 4, 6]))
print(remove_duplicates([1, 1, 1, 1]))
print(remove_duplicates([]))
print(remove_duplicates(['a', 'b', 'a']))
print(" ")


# Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). 
# L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo. 
# La funzione ritorna "Accesso consentito" oppure "Accesso negato".
def check_access(username: str, password: str, is_active: bool) -> str:
    if username == "admin" and password == "12345" and is_active:
        return "Accesso consentito"
    else:
        return "Accesso negato"
    
print(check_access("admin", "12345", True))
print(check_access("admin", "12345", False))
print(check_access("user", "12345", True))
print(check_access("admin", "54321", True))
print(" ")

#Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.

def check_parentheses(expression: str) -> bool:
    list = []
    for carattere in expression:
        if carattere == '(':
            list.append(carattere)
        elif carattere == ')':
            if len(list) > 0 and list[-1] == '(':
                list.pop()
            else:
                return False
    return len(list) == 0

 	

print(check_parentheses("()()"))
print(check_parentheses("(()))("))
print(check_parentheses("((()))"))
print(" ")


# Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. 
# Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.

def count_isolated(lista) -> int:
    isolati:int = 0
    lunghezza:int = len(lista)
    
    for i in range(lunghezza):
        if i == 0:  
            if lista[i] != lista[i+1]:  
                isolati += 1
        elif i == lunghezza - 1: 
            if lista[i] != lista[i-1]: 
                isolati += 1
        else:
            if lista[i] != lista[i-1] and lista[i] != lista[i+1]:  
                isolati += 1
                
    return isolati



 	

print(count_isolated([1, 2, 2, 3, 3, 3, 4]))
print(count_isolated([1, 1, 2, 2, 3, 4, 4]))
print(count_isolated([1, 2, 3, 4, 5]))
print(count_isolated([1, 1, 1, 1, 1]))
print(" ")



#Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.
def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    new_set = original_set.copy()  
    for numero in elements_to_remove:
        if numero in new_set:
            new_set.remove(numero)  
    return new_set

 	

print(remove_elements({1, 2, 3, 4}, [2, 3]))
print(remove_elements({5, 6, 7}, [7, 8, 9]))
print(remove_elements({1, 2}, [3]))
print(" ")




#Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    result = {}
    for key in dict1:
        if key in dict2:
            result[key] = dict1[key] + dict2[key]
        else:
            result[key] = dict1[key]

    for key in dict2:
        if key not in dict1:
            result[key] = dict2[key]

    return result

print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
 	

print(merge_dictionaries({}, {'a': 10, 'b': 20}))
print(merge_dictionaries({'x': 5}, {'x': -5}))
print(merge_dictionaries({}, {}))



#################################################
print("#" *30)
print("Esercizi Lezione 7")
#################################################
#Scrivi una funzione che inverte le chiavi e i valori in un dizionario. Se ci sono valori duplicati, scarta i duplicati.
def inverti_mappa(dizionario: dict[str:int]) -> dict[str:int]:
    nuovo_dizionario: dict = {}

    for chiave, valore in dizionario.items():
        if valore not in nuovo_dizionario:
            nuovo_dizionario[valore] = chiave

        return nuovo_dizionario
    

 	

print(inverti_mappa({'a': 1, 'b': 2, 'c': 3}))
print(inverti_mappa({'a': 3, 'b': 3, 'c': 3}))
print(inverti_mappa({'a': 1, 'b': 1, 'c': 2}))
print(inverti_mappa({}))
print(" ")


#Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. 
#Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.

def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    result_dict = {}
    for key, value in tuples:
        if key in result_dict:
            result_dict[key].append(value)
        else:
            result_dict[key] = [value]
    return result_dict


print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))
print(lista_a_dizionario([('a', 1)]))
print(lista_a_dizionario([]))
print(lista_a_dizionario([('c', 1), ('b', 2), ('c', 3), ('c', 4)]))
print(" ")

#Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
# Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.
def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
   for element, count in da_rimuovere.items():
        while count > 0 and element in lista:
            lista.remove(element)
            count -= 1
            
def rimuovi_elementi(lista, elementi_da_rimuovere):
    for elemento, numero in elementi_da_rimuovere.items():
        for i in range(numero):
            if elemento in lista:
                lista.remove(elemento)
    return lista


print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 1}))
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
print(rimuovi_elementi([1, 1, 1, 1], {1: 2}))
print(rimuovi_elementi([4, 5, 6], {1: 3}))
print(" ")

#Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.
def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    voti_aggregati = {}

    for dizionario in voti:
        studente = dizionario.get('nome')
        voto = dizionario.get('voto')

        if studente is not None and voto is not None:
            if studente in voti_aggregati:
                voti_aggregati[studente].append(voto)
            else:
                voti_aggregati[studente] = [voto]

    return voti_aggregati

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
print(aggrega_voti([{'nome': 'Alice', 'voto': 100}]))
print(aggrega_voti([{'nome': 'Bob', 'voto': 75}, {'nome': 'Bob', 'voto': 85}]))
