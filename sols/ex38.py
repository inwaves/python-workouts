from dataclasses import dataclass, field
from typing import List

@dataclass
class Scoop:
    flavour: str

    def __repr__(self) -> str:
        return f"{self.flavour} scoop"

@dataclass
class Bowl:
    scoops: List[Scoop] = field(default_factory=list)
    MAX_SCOOPS = 3

    def add_scoops(self, *scoops: Scoop) -> None:
        if len(self.scoops) < self.MAX_SCOOPS:
            self.scoops += scoops

    def __repr__(self) -> str:
        return f"Bowl containing: {self.scoops}."


@dataclass
class BigBowl(Bowl):
    MAX_SCOOPS = 5

def create_scoops() -> Bowl:
    bowl = Bowl()
    bowl.add_scoops(*[Scoop(flavour) for flavour in ["chocolate", "pistachio", "coconut"]])
    return bowl
