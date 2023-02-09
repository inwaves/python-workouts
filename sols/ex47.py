from typing import Any, Iterable, Sequence


class Circle:
    def __init__(self, seq: Sequence[Any], n: int) -> None:
        self.seq = seq
        self.n = n
        self.idx = 0

    def __iter__(self) -> "Circle":
        return self

    def __next__(self) -> Any:
        if self.idx == self.n:
            raise StopIteration()
        res = self.seq[self.idx % len(self.seq)]
        self.idx += 1
        return res

def circle_generator(sequence: Sequence[Any], max_times: int) -> Iterable:
    for i in range(max_times):
        yield sequence[i % len(sequence)]

    # n = len(sequence)
    # yield from (sequence[x % n] for x in range(max_times))
