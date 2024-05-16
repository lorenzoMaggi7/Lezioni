class Zoo:
    def __init__(self,fences: list, zoo_keepers: list):
        self.fences = fences
        self.zoo_keepers = zoo_keepers

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
    def __init__(self, name, surname, id, zoo):
        self.name = name
        self.surname = surname
        self.id = id
        self.zoo = zoo


def add_fence(self, fence):
    self.zoo.fences.append(fence)

def add_animal(self, animal:Animal, fence:Fence):
    if fence in self.zoo.fences and fence.area >= animal.height * animal.width and fence.habitat == animal.preferred_habitat:
        fence.area -= animal.height * animal.width
        fence.animals.append(animal)


def remove_animal(self, animal:Animal, fence:Fence):
    if fence in self.zoo.fences and animal in fence.animals:
        fence.area += animal.height * animal.width
        fence.animals.remove(animal)


def feed(self):
    for fence in self.zoo.fences:
        self.feed_animals(fence)

def feed_animals(self, fence):
    for animal in fence.animals:
        new_height = animal.height * 1.02
        new_width = animal.width * 1.02
        required_space = new_height * new_width - animal.height * animal.width
    if animal.health < 100 and fence.area >= required_space:
        animal.health = min(100, animal.health + 1)
        fence.area -= required_space
        animal.height = new_height
        animal.width = new_width


def clean(self):
    total_cleaning_time = 0.0
    for fence in self.zoo.fences:
        total_cleaning_time += self.clean_fence(fence)
        return total_cleaning_time

def clean_fence(self, fence):
    occupied_area = sum(animal.height * animal.width for animal in fence.animals)
    cleaning_time = (fence.initial_area / (fence.initial_area - occupied_area)) if occupied_area else fence.initial_area
    return cleaning_time


def __str__(self):
    return f"ZooKeeper(name={self.name}, surname={self.surname}, id={self.id})"