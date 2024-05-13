"""
Creaiamo un sistema di gestione di uno zoo virtuale

Sistema di gestione dello zoo virtuale

Classi:

1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.

2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, age, height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).

3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti possono contenere uno o più animali. I recinti possono hanno gli attributi area, temperature e habitat.

4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. I guardiani dello zoo hanno un name, un surname, e un id. Essi possono nutrire gli animali, pulire i recinti e svolgere altri compiti nel nostro zoo virtuale.

Funzionalità:

1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat e se c'è ancora spazio nel recinto, ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.

2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale dallo zoo. L'animale deve essere allontanato dal suo recinto. Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.

3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli animali dello zoo. Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. Perciò, l'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.

4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo di pulire tutti i recinti dello zoo. Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata.

5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo, sui recinti dello zoo che contengono animali. 

E.s.: Se abbiamo un guardiano chiamato Lorenzo Maggi con matricola 1234, e un recinto Fence(area=100, temperature=25, habitat=Continentale) con due animali Animal(name=Scoiattolo, species=Blabla, age=25, ...), Animal(name=Lupo, species=Lupus, age=14,...) ci si aspetta di avere una rappresentazione testuale dello zoo come segue:

Guardians:

ZooKeeper(name=Lorenzo, surname=Maggi, id=1234)

Fences:

Fence(area=100, temperature=25, habitat=Continent)

with animals:

Animal(name=Scoiattolo, species=Blabla, age=25)

Animal(name=Lupo, species=Lupus, age=14)
#########################

Fra un recinto e l'altro mettete 30 volte il carattere #.
"""

class Zoo:
    def __init__(self):
        self.fences = []
        self.zoo_keepers = []

    def add_animal(self, animal, fence):
        if fence in self.fences and fence.area >= animal.height * animal.width and fence.habitat == animal.preferred_habitat:
            fence.area -= animal.height * animal.width
            fence.animals.append(animal)
            print(f"{animal.name} è stato aggiunto al recinto {fence}.")
        else:
            print(f"Il recinto {fence} non può ospitare {animal.name}.")

    def remove_animal(self, animal, fence):
        if fence in self.fences and animal in fence.animals:
            fence.area += animal.height * animal.width
            fence.animals.remove(animal)
            print(f"{animal.name} è stato rimosso dal recinto {fence}.")
        else:
            print(f"{animal.name} non è presente nel recinto {fence}.")

    def feed(self):
        for fence in self.fences:
            for animal in fence.animals:
                if animal.health < 100 and fence.area >= animal.height * animal.width * 1.02:
                    animal.health += 1
                    animal.height *= 1.02
                    animal.width *= 1.02
                    fence.area -= animal.height * animal.width
                    print(f"{animal.name} è stato nutrito.")

    def clean(self):
        total_cleaning_time = 0.0
        for fence in self.fences:
            if fence.area > 0:
                cleaning_time = fence.area / (fence.area + (fence.initial_area - fence.area))
                total_cleaning_time += cleaning_time
                print(f"Il tempo di pulizia del recinto {fence} è {cleaning_time} unità di tempo.")
        return total_cleaning_time

    def describe_zoo(self):
        print("Guardiani:")
        for zoo_keeper in self.zoo_keepers:
            print(zoo_keeper)
        print("\nRecinti:")
        for fence in self.fences:
            print(fence)
            print("con animali:")
            for animal in fence.animals:
                print(animal)
            print("\n" + "#" * 30)


class Animal:
    def __init__(self, name, species, age, height, width, preferred_habitat):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)

    def __str__(self):
        return f"Animal(name={self.name}, species={self.species}, age={self.age}, health={self.health})"


class Fence:
    def __init__(self, area, temperature, habitat):
        self.initial_area = area
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []

    def __str__(self):
        return f"Fence(area={self.initial_area}, temperature={self.temperature}, habitat={self.habitat})"


class ZooKeeper:
    def __init__(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.id = id

    def __str__(self):
        return f"ZooKeeper(name={self.name}, surname={self.surname}, id={self.id})"


# Esempio di utilizzo
if __name__ == "__main__":
    zoo = Zoo()
    zoo_keeper = ZooKeeper("Lorenzo", "Maggi", 1234)
    zoo.zoo_keepers.append(zoo_keeper)

    fence = Fence(area=100, temperature=25, habitat="Continentale")
    zoo.fences.append(fence)

    animal1 = Animal(name="Scoiattolo", species="Blabla", age=25, height=5, width=2, preferred_habitat="Continentale")
    animal2 = Animal(name="Lupo", species="Lupus", age=14, height=8, width=3, preferred_habitat="Continentale")

    zoo.add_animal(animal1, fence)
    zoo.add_animal(animal2, fence)
    zoo.remove_animal(animal1, fence)

    zoo.describe_zoo()

    zoo.feed()

    zoo.describe_zoo()

    cleaning_time = zoo.clean()
    print(f"\nTempo totale impiegato per la pulizia: {cleaning_time}")
