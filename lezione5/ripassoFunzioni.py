
"""Scrivi una funzione che inverte le chiavi e i valori in un dizionario. Se ci sono valori duplicati, scarta i duplicati.

For example:


print(inverti_mappa({'a': 1, 'b': 2, 'c': 3}))            {1: 'a', 2: 'b', 3: 'c'}

print(inverti_mappa({}))                                                        {}
"""
def inverti_mappa(dizionario):
    nuovo_dizionario = {}
    
    for chiave, valore in dizionario.items():
        if valore not in nuovo_dizionario:
            nuovo_dizionario[valore] = chiave
    
    return nuovo_dizionario

# Test dei casi
print(inverti_mappa({'a': 3, 'b': 3, 'c': 3}))  # Output: {3: 'a'}
print(inverti_mappa({'a': 1, 'b': 1, 'c': 2}))  # Output: {1: 'a', 2: 'c'}
print(inverti_mappa({'a': 2, 'b': 1, 'c': 2}))  # Output: {2: 'a', 1: 'b'}

	

"""
Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. 
Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.
"""
def tuple_list_to_dict(tuple_list):
    result_dict = {}
    for key, value in tuple_list:
        if key in result_dict:
            result_dict[key].append(value)
        else:
            result_dict[key] = [value]
    return result_dict

# Esempio d'uso
tuples = [("a", 1), ("b", 2), ("a", 3), ("c", 4), ("b", 5)]
result = tuple_list_to_dict(tuples)
print(result)


"""
Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.
"""

def remove_elements(data_list, elements_to_remove):
    for element, count in elements_to_remove.items():
        while count > 0 and element in data_list:
            data_list.remove(element)
            count -= 1
def rimuovi_elementi(lista, elementi_da_rimuovere):
    for elemento, numero in elementi_da_rimuovere.items():
        for _ in range(numero):
            if elemento in lista:
                lista.remove(elemento)
    return lista

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 1}))
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
print(rimuovi_elementi([1, 1, 1, 1], {1: 2}))
print(rimuovi_elementi([4, 5, 6], {1: 3}))
print(rimuovi_elementi([], {2: 1}))


# Esempio d'uso
data = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
elements_to_remove = {1: 2, 3: 1}
remove_elements(data, elements_to_remove)
print(data)
"""
Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.
"""
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

# Esempio di utilizzo
lista_voti = [
    {'nome': 'Mario', 'voto': 8},
    {'nome': 'Luigi', 'voto': 7},
    {'nome': 'Mario', 'voto': 9},
    {'nome': 'Luigi', 'voto': 6},
    {'nome': 'Maria', 'voto': 10}
]

voti_aggregati = aggrega_voti(lista_voti)

# Stampa dei voti aggregati
for studente, voti in voti_aggregati.items():
    print(f"{studente}: {voti}")


"""
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, 
scontati del 10%.
"""
def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    scontati:dict = {}

    for key, value in prodotti.items():
        if value > 20:
            prezzo_scontato = value * (1/10)
            scontati[key] = prezzo_scontato

    return scontati


"""

PARTE 1
Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo). 
La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
 
PARTE 2
Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare, 
e il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.


"""
def create_contact(name: str, email: str = None, telefono: int = None) -> dict:
    contatto = {'name': name}
    if email:
        contatto['email'] = email
    if telefono:
        contatto['telefono'] = telefono
    return contatto

def update_contact(dictionary: dict, name: str, email: str = None, telefono: int = None) -> dict:
    for contatto in dictionary:
        if contatto['name'] == name:
            if email:
                contatto['email'] = email
            if telefono:
                contatto['telefono'] = telefono
            break
    return dictionary
