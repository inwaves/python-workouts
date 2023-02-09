from typing import Iterable, Iterator, Tuple, Any


class MyEnumerate:
    def __init__(self, data: Iterable[Any]) -> None:
        self.data = data

    def __iter__(self) -> Iterator:
        return MyEnumerateIterator(self.data)



class MyEnumerateIterator:
    def __init__(self, data: Iterable[Any]) -> None:
        self.data = data
        self.idx = 0

    def __next__(self) -> Tuple[int, Any]:
        if self.idx < len(self.data):
            res = (self.idx, self.data[self.idx])
            self.idx += 1
            return res
        else:
            raise StopIteration("No more elements in data.")

