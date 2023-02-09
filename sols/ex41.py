from dataclasses import dataclass

@dataclass
class Envelope:
    weight: float = 0.0
    postage: float = 0.0
    was_sent: bool = False

    def send(self) -> bool:
        if self.postage >= self.weight * 10:
            self.was_sent = True
            return self.was_sent
        else:
            raise PostageException(f"{self.postage}/{self.postage_needed()} postage provided.")

    def add_postage(self, amount_to_add: float) -> None:
        self.postage += amount_to_add

    def postage_needed(self) -> float:
        return self.weight * 10


class BigEnvelope(Envelope):
    def postage_needed(self) -> float:
        return self.weight * 15


class PostageException(Exception):
    pass
