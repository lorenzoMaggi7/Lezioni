"""
Scrivi un programma in Python che gestisca un magazzino. 
Il programma deve permettere di aggiungere prodotti al magazzino, cercare prodotti per nome e verificare la disponibilità di un prodotto.

Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 
Test case:

    Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente, aggiunge i prodotti al magazzino.
    Il sistema cerca un prodotto per verificare se esiste nell'inventario.
    Il sistema verifica la disponibilità dei prodotti in inventario.

"""
class Prodotto:
    def __init__(self, nome: str, quantità: int):
        self.nome = nome
        self.quantità = quantità

class Magazzino:
    def __init__(self,magazino: dict) -> None:
        self.nome = magazino
        nome = {}

    def aggiungi_prodotto(self,prodotto: Prodotto):
        self.nome[prodotto.nome] = prodotto

    def cerca_prodotto(self,nome: str):
        if nome in self.nome:
            return self.nome[nome]
        else:
            return None

    def verifica_disponibilità(self,nome:str):
        if nome in self.nome:
            disponibilità = self.nome[nome].quantità
            if disponibilità > 0:
                return f"Il prodotto {nome} è disponibile"
            else:
                return f"Il prodotto {nome} non è disponibile"
        else:
            return f"Il prodotto {nome}non è presente nel magazzino"
        

prodotto1 = Prodotto(nome="Lametta", quantità=50)
prodotto2 = Prodotto(nome="Penne", quantità=100)

magazzino1 = Magazzino(prodotto1)