class MovieCatalog:
    def __init__(self):
        self.catalog = {}
    
    def add_movie(self, director_name, movies):
        if director_name in self.catalog:
            self.catalog[director_name].extend(movies)
        else:
            self.catalog[director_name] = movies
        return f"Film aggiunti per il regista {director_name}."

    def remove_movie(self, director_name, movie_name):
        if director_name in self.catalog:
            if movie_name in self.catalog[director_name]:
                self.catalog[director_name].remove(movie_name)
                if not self.catalog[director_name]:  # Se la lista dei film è vuota
                    del self.catalog[director_name]  # Opzionalmente rimuove il regista
                return f"Film '{movie_name}' rimosso dal regista {director_name}."
            else:
                return f"Film '{movie_name}' non trovato per il regista {director_name}."
        else:
            return f"Regista '{director_name}' non trovato nel catalogo."

    def list_directors(self):
        if self.catalog:
            return "Registi nel catalogo: " + ", ".join(self.catalog.keys())
        else:
            return "Nessun regista presente nel catalogo."

    def get_movies_by_director(self, director_name):
        if director_name in self.catalog:
            return f"Film di {director_name}: " + ", ".join(self.catalog[director_name])
        else:
            return f"Regista '{director_name}' non trovato nel catalogo."

    def search_movies_by_title(self, title):
        found_movies = []
        for director, movies in self.catalog.items():
            matching_movies = [movie for movie in movies if title.lower() in movie.lower()]
            if matching_movies:
                found_movies.append(f"{director}: " + ", ".join(matching_movies))
        
        if found_movies:
            return "Film trovati: " + "; ".join(found_movies)
        else:
            return f"Nessun film trovato contenente '{title}' nel titolo."


# Test Cases
if __name__ == "__main__":
    catalog = MovieCatalog()

    # Aggiungi film al catalogo
    print(catalog.add_movie("Quentin Tarantino", ["Pulp Fiction", "Kill Bill"]))
    print(catalog.add_movie("Christopher Nolan", ["Inception", "The Dark Knight"]))
    print(catalog.add_movie("Steven Spielberg", ["Jurassic Park", "E.T."]))

    # Visualizza tutti i registi
    print(catalog.list_directors())

    # Visualizza i film di un regista specifico
    print(catalog.get_movies_by_director("Quentin Tarantino"))
    print(catalog.get_movies_by_director("Christopher Nolan"))

    # Cerca film per titolo
    print(catalog.search_movies_by_title("Park"))
    print(catalog.search_movies_by_title("Knight"))

    # Rimuovi un film
    print(catalog.remove_movie("Christopher Nolan", "Inception"))
    print(catalog.get_movies_by_director("Christopher Nolan"))

    # Rimuovi un regista quando tutti i suoi film sono rimossi
    print(catalog.remove_movie("Christopher Nolan", "The Dark Knight"))
    print(catalog.list_directors())
    print(catalog.get_movies_by_director("Christopher Nolan"))
