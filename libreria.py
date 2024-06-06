class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        self.disponibile = True
    
    def __str__(self):
        return f"{self.titolo} di {self.autore} {'(Disponibile)' if self.disponibile else '(Non disponibile)'}"


class Biblioteca:
    def __init__(self):
        self.catalogo = []
    
    def aggiungi_libro(self, libro):
        self.catalogo.append(libro)
        return f"Libro '{libro.titolo}' aggiunto al catalogo."

    def presta_libro(self, titolo):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                if libro.disponibile:
                    libro.disponibile = False
                    return f"Libro '{titolo}' è stato prestato."
                else:
                    return f"Libro '{titolo}' non è disponibile."
        return f"Libro '{titolo}' non trovato nel catalogo."

    def restituisci_libro(self, titolo):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                if not libro.disponibile:
                    libro.disponibile = True
                    return f"Libro '{titolo}' è stato restituito."
                else:
                    return f"Libro '{titolo}' era già disponibile."
        return f"Libro '{titolo}' non trovato nel catalogo."

    def mostra_libri_disponibili(self):
        disponibili = [libro.titolo for libro in self.catalogo if libro.disponibile]
        if disponibili:
            return "Libri disponibili: " + ", ".join(disponibili)
        else:
            return "Nessun libro disponibile al momento."


if __name__ == "__main__":
    biblioteca = Biblioteca()


    print(biblioteca.aggiungi_libro(Libro("One Piece", "Eichiro Oda")))
    print(biblioteca.aggiungi_libro(Libro("1984", "George Orwell")))
    print(biblioteca.aggiungi_libro(Libro("To Kill a Mockingbird", "Harper Lee")))

 
    print(biblioteca.mostra_libri_disponibili())

    print(biblioteca.presta_libro("1984"))
    print(biblioteca.mostra_libri_disponibili())

    print(biblioteca.presta_libro("1984"))

    print(biblioteca.restituisci_libro("1984"))
    print(biblioteca.mostra_libri_disponibili())

    print(biblioteca.restituisci_libro("1984"))


    print(biblioteca.presta_libro("Il Grande Gatsby"))
    print(biblioteca.restituisci_libro("Il Grande Gatsby"))
