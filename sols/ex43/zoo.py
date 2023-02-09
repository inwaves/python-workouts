from sols.ex43.cages import Cage

class Zoo:
    def __init__(self) -> None:
        self.cages = []

    def add_cages(self, *cages: Cage) -> None:
        self.cages += cages

    def animals_by_colour(self, colour: str) -> list:
        return [animal for cage in self.cages for animal in cage.animals if animal.colour == colour]

    def animals_by_legs(self, num_legs: int) -> list:
        return [animal for cage in self.cages for animal in cage.animals if animal.number_of_legs == num_legs]

    def number_of_legs(self) -> int:
        return sum(animal.number_of_legs for cage in self.cages for animal in cage.animals)

    def __repr__(self) -> str:
        return f"Zoo containing: {self.cages}"
