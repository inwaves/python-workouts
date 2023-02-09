class Cage:
    def __init__(self, uid: int, space: float) -> None:
        self.uid = uid
        self.space = space
        self.animals = []

    def add_animals(self, *animals) -> None:
        for animal in animals:
            if self.space_remaining() >= animal.space_required:
                self.animals += [animal]
            else:
                raise ValueError(f"Cage {self.uid} reached capacity. Cannot add {animal}.")

    def space_remaining(self) -> float:
        return self.space - sum(animal.space_required for animal in self.animals)

    def __repr__(self) -> str:
        return f"Cage {self.uid} contains: {self.animals}"
