from typing import Any, Generator, Iterable


def mychain(*iterables: Iterable[Any]) -> Generator:
    yield from (elem for iterable in iterables for elem in iterable)


def myzip(*iterables: Iterable[Any]) -> Generator:
    yield from (tuple([iterable[i] for iterable in iterables]) for i in range(len(iterables[0])))

def myrange(start: int, stop: int, step: int = 1) -> Generator:
    current = start
    while current < stop:
        res = current
        current += step
        yield res

class MyRange:
    def __init__(self, start: int, stop: int, step: int = 1) -> None:
        self.start = self.current_index = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self


    def __next__(self) -> int:
        res = self.current_index
        if res >= self.stop:
            raise StopIteration()
        self.current_index += self.step
        return res

