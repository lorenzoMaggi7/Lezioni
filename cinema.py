"""
Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, ognuna con un diverso film in programmazione. 
Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
 
Classi:
- Film: Rappresenta un film con titolo e durata.
 
    - Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

    Metodi:
        - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
        - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
- Cinema: Gestisce le operazioni legate alla gestione delle sale.

Metodi:
    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

Test case:

    Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
    Un cliente sceglie un film e prenota un certo numero di posti.
    Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.
"""

class Film:

    def __init__(self, titolo:str, durata: float):
        self.titolo = titolo
        self.durata = durata


class Sala:

    def __init__(self,numero_identificativo: int, film: Film,posti_totali: int):
        self.numero = numero_identificativo
        self.film = film
        self.posti = posti_totali
        self.posti_prenotati = 0


    def prenota_posti(self, num_posti: int) -> str:
        
        posti_disponibili = self.posti - self.posti_prenotati
        if num_posti <= posti_disponibili :
            self.posti_prenotati += num_posti
            return f"Prenotazione andata a buon fine per {num_posti} posti"
        else:
            return "Numero di posti richiesti non disponibile"
        


    def posti_disponibili(self) -> int:
        
        return self.posti_disponibili - self.posti_prenotati


class Cinema:

    def __init__(self, nome):
        self.nome = nome
        self.sale = []

    def aggiungi_sala(self, sala):
        self.sale.append(sala)

    def prenota_film(self, titolo_film, num_posti):
        for sala in self.sale:
            if sala.film == titolo_film:
                return sala.prenota_posti(num_posti)
        return f"Il film '{titolo_film}' non è in programmazione in questo cinema."


cinema = Cinema("Cinema Centrale")
film1 = Film(titolo = "Interstellar", durata= 2.49)
film2 = Film(titolo="Inception", durata= 2.28)
sala1 = Sala(numero_identificativo=1, film="Interstellar", posti_totali=100)
sala2 = Sala(numero_identificativo=2, film="Inception", posti_totali=80)

cinema.aggiungi_sala(sala1)
cinema.aggiungi_sala(sala2)

print(cinema.prenota_film("Interstellar", 30))  
print(cinema.prenota_film("Titanic", 50))
print(cinema.prenota_film("Inception", 20))
print(cinema.prenota_film("Interstellar", 1000))