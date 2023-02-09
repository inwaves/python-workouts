class Animal:
    species: str = "Default species"
    number_of_legs: int = 1

    def __init__(self, colour: str, space_required: float) -> None:
        self.colour = colour
        self.space_required = space_required

    def __repr__(self,) -> str:
        return f"{self.colour.capitalize()} {self.species}, {self.number_of_legs} legs"


class Quadruped(Animal):
    number_of_legs: int = 4

class Biped(Animal):
    number_of_legs: int = 2

class Limbless(Animal):
    number_of_legs: int = 0

class Sheep(Quadruped):
    species: str = "Sheempus Scronchius"

class Wolf(Quadruped):
    species: str = "Canis lupus"

class Snake(Limbless):
    species: str = "Snek"

class Parrot(Biped):
    species: str = "Honk Honk"
