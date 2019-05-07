class Animal(object):
    def __init__(self, name: str, age, health: int, happiness: int):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
        self.species = str()

    def display_info(self):
        s = f"This {self.species} is named {self.name}, is {self.health}, and is {self.happiness}."
        return s

    def feed(self):
        self.health += 10
        self.happiness += 10


class Lion(Animal):
    def __init__(self, name: str, age="unknown", health: int = 3, happiness: int = 3, male: bool = True):
        super().__init__(name, age, health, happiness)
        self.male = male


class Bear(Animal):
    def __init__(self, name: str, age="unknown", health: int = 2, happiness: int = 10, color: str="brown"):
        super().__init__(name, age, health, happiness)
        self.color = color


class Tiger(Animal):
    def __init__(self, name: str, age="unknown", health: int = 4, happiness: int = 5):
        super().__init__(name, age, health, happiness)


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name):
        self.animals.append(Lion(name))

    def add_tiger(self, name):
        self.animals.append(Tiger(name))

    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.display_info()


zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()
