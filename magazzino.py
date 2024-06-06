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
    def __init__(self):
        self.prodotti = {}

    def aggiungi_prodotto(self, prodotto: Prodotto):
        if prodotto.nome in self.prodotti:
            self.prodotti[prodotto.nome].quantità += prodotto.quantità
        else:
            self.prodotti[prodotto.nome] = prodotto

    def cerca_prodotto(self, nome: str) -> Prodotto:
        if nome in self.prodotti:
            return self.prodotti[nome]
        return None

    def verifica_disponibilità(self, nome: str) -> str:
        prodotto = self.cerca_prodotto(nome)
        if prodotto:
            if prodotto.quantità > 0:
                return f"Il prodotto {nome} è disponibile"
            else:
                return f"Il prodotto {nome} non è disponibile"
        else:
            return f"Il prodotto {nome} non è presente nel magazzino"


magazzino = Magazzino()


mela = Prodotto("Mela", 10)
arancia = Prodotto("Arancia", 5)
banana = Prodotto("Banana", 0)


magazzino.aggiungi_prodotto(mela)
magazzino.aggiungi_prodotto(arancia)
magazzino.aggiungi_prodotto(banana)


print("Test ricerca prodotto")
if magazzino.cerca_prodotto("Mela") == mela:
    print("Ricerca prodotto Mela passata")
else:
    print("Errore: ricerca prodotto Mela fallita")

if magazzino.cerca_prodotto("Arancia") == arancia:
    print("Ricerca prodotto Arancia passata")
else:
    print("Errore: ricerca prodotto Arancia fallita")

if magazzino.cerca_prodotto("Banana") == banana:
    print("Ricerca prodotto Banana passata")
else:
    print("Errore: ricerca prodotto Banana fallita")

if magazzino.cerca_prodotto("Pera") is None:
    print("Ricerca prodotto Pera passata")
else:
    print("Errore: ricerca prodotto Pera non dovrebbe esistere")

print("\nTest verifica disponibilità")

if magazzino.verifica_disponibilità("Mela") == "Il prodotto Mela è disponibile":
    print("Disponibilità prodotto Mela passata")
else:
    print("Errore: disponibilità prodotto Mela")

if magazzino.verifica_disponibilità("Arancia") == "Il prodotto Arancia è disponibile":
    print("Disponibilità prodotto Arancia passata")
else:
    print("Errore: disponibilità prodotto Arancia")

if magazzino.verifica_disponibilità("Banana") == "Il prodotto Banana non è disponibile":
    print("Disponibilità prodotto Banana passata")
else:
    print("Errore: disponibilità prodotto Banana")

if magazzino.verifica_disponibilità("Pera") == "Il prodotto Pera non è presente nel magazzino":
    print("Disponibilità prodotto Pera passata")
else:
    print("Errore: disponibilità prodotto Pera")
        

