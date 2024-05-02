#############TEST################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################




"""
Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e viceversa a seconda del parametro to_fahrenheit. 
Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit.
"""
def converti_temperatura(temperatura, to_fahrenheit=True):
    if to_fahrenheit:
        fahrenheit = (temperatura * 9/5) + 32
        return fahrenheit
    else:
        celsius = (temperatura - 32) * 5/9
        return celsius

print(converti_temperatura(25))
print(converti_temperatura(75, to_fahrenheit=False))  

"""
Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.
"""
def countdown(n: int) -> int:
    if n >= 0:
        for i in range(n,-1,-1):
            print(i)
    else:
        print("the numbers must be positive")

"""
Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. 
L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. 
La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte
"""
def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA:
        return "Operazione permessa"
    elif conditionB and conditionC:
        return "Operazione permessa"
    else:
        return "Operazione negata"

print(check_combination(True,False,True))
print(check_combination(False,True,True))
print(check_combination(False,False,True))

"""
Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
"""
def remove_duplicates(lista):
        lista_senza_duplicati = []
        for elemento in lista:
            if elemento not in lista_senza_duplicati:
                lista_senza_duplicati.append(elemento)
        return lista_senza_duplicati

lista_originale = [1, 2, 3, 2, 4, 5, 1, 'a', 'b', 'c', 'a']
lista_senza_duplicati = remove_duplicates(lista_originale)
print(lista_senza_duplicati)


"""
Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). 
L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo. 
La funzione ritorna "Accesso consentito" oppure "Accesso negato".
"""

def check_access(username: str, password: str, is_active: bool) -> str:
    if username == "admin" and password == "12345" and is_active:
        return "Accesso consentito"
    else:
        return "Accesso negato"

print(check_access("admin", "12345", True))
print(check_access("ciao","12345", True))

"""
    Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, 
    cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
"""
def parentesi_bilanciate(stringa:str) -> bool:
    list = []
    for carattere in stringa:
        if carattere == '(':
            list.append(carattere)
        elif carattere == ')':
            if len(list) > 0 and list[-1] == '(':
                list.pop()
            else:
                return False
    return len(list) == 0

# Esempio di utilizzo
stringa1 = "((()))"
stringa2 = "()()()"
stringa3 = "(()()"
stringa4 = "())("
stringa5 = "()(()"

print(parentesi_bilanciate(stringa1))  # Output: True
print(parentesi_bilanciate(stringa2))  # Output: True
print(parentesi_bilanciate(stringa3))  # Output: False
print(parentesi_bilanciate(stringa4))  # Output: False
print(parentesi_bilanciate(stringa5))  # Output: False
"""
Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. 
Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.
"""
def conta_isolati(lista):
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
lista_numeri = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7, 7]
risultato = conta_isolati(lista_numeri)
print("Numero di elementi isolati nella lista:", risultato)

"""
Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.
"""
def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    new_set = original_set.copy()  
    for numero in elements_to_remove:
        if numero in new_set:
            new_set.remove(numero)  
    return new_set

insieme_originale = {1, 2, 3, 4, 5}
numeri_da_rimuovere = [2, 4, 6]
new_set = remove_elements(insieme_originale, numeri_da_rimuovere)
print("Nuovo insieme dopo la rimozione:", new_set)



"""
Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.
"""
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    risultato = {}
    for chiave in dict1:
        if chiave in dict2:
            risultato[chiave] = dict1[chiave] + dict2[chiave]
        else:
            risultato[chiave] = dict1[chiave]

    for chiave in dict2:
        if chiave not in dict1:
            risultato[chiave] = dict2[chiave]

    return risultato
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 30, 'c': 40, 'd': 50}

risultato = merge_dictionaries(d1, d2)
print(risultato)



