"""
Obiettivo:
Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) e una classe derivata Film che rappresenti specificamente un film. 
Gli studenti dovranno anche creare oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.

Specifiche della Classe Media:
 
Attributi:
- title (stringa): Il titolo del media.
- reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5, dove 1=Terribile, 2=Brutto, 3=Normale, 4=Bello, 5=Grandioso.

Metodi:
- set_title(self, title): Imposta il titolo del media.
- get_title(self): Restituisce il titolo del media.
- aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
- getMedia(self): Calcola e restituisce la media delle valutazioni.
- getRate(self): Restituisce una stringa che descrive il giudizio medio del media basato sulla media delle valutazioni.
- ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
- recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, il giudizio e le percentuali di ciascun voto. 

Esempio di riassunto:
 
Titolo del Film: The Shawshank Redemption
Voto Medio: 3.80
Giudizio: Bello
Terribile: 10.00%
Brutto: 10.00%
Normale: 10.00%
Bello: 30.00%
Grandioso: 40.00%

Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().


"""
class Media:
    def __init__(self,title: str, reviews:list = None) -> None:
        self.title = title
        self.reviews = [1,2,3,4,5]

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title
    
    def aggiungiValutazione(self, voto:int):
        try:
            voto = int(voto)
            if 1 <= voto <= 5:
                self.reviews.append(voto)
            else:
                raise ValueError
        except ValueError:
            raise ValueError("La valutazione deve essere compreso tra 1 e 5")

    def getMedia(self):
        if not self.reviews:
            return 0 
        return sum(self.reviews) / len(self.reviews)

    def getRate(self):
        media = self.getMedia()
        if media == 0:
            return "Nessuna valutazione"
        elif 1 <= media < 2:
            return "Terribile"
        elif 2 <= media < 3:
            return "Brutto"
        elif 3 <= media < 4:
            return "Normale"
        elif 4<= media <= 5:
            return "Bello"
        else:
            return "Grandioso"
        
    def ratePercentage(self,voto):
        if not self.reviews:
            return 0
        count = self.reviews.count(voto)
        return (count / len(self.reviews)) * 100
    
    def recensione(self):
        print( f"Titolo: {self.title}")
        print(f"Voto medio: {self.getMedia(): .2f}")
        print(f"Giudizio: {self.getRate()}")
        print(f"Terribile : {self.ratePercentage(1): .2f}")
        print(f"Brutto : {self.ratePercentage(2): .2f}")
        print(f"Normale : {self.ratePercentage(3): .2f}")
        print(f"Bello : {self.ratePercentage(4): .2f}")
        print(f"Grandioso : {self.ratePercentage(5): .2f}")
class Film(Media):
    def __init__(self, title: str, reviews: list = None) -> None:
        super().__init__(title, reviews)


film1= Film(title="La palla")
film2= Film("Ciao")
valutazione_film1 = [2,4,5,3,2,5,4,5,4,4]
valutazione_film2 = [5,5,5,5,5,5,5,5,5,5]

for voto in valutazione_film1:
    film1.aggiungiValutazione(voto)

for voto in valutazione_film2:
    film2.aggiungiValutazione(voto)


film1.recensione()
print("")
film2.recensione()
