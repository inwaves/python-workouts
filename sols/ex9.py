from typing import Sequence, Any


def firstlast(in_sequence: Sequence) -> Sequence:
    return [in_sequence[0], in_sequence[-1]]


def square(a: int | float | complex) -> int | float | complex:
    return a * a


def homerolled_max(in_sequence: Sequence) -> Any:
    it, max_len = 0, 0
    for el in in_sequence:
        if len(el) > max_len:
            max_len = len(el)
            it = el

    return it


def sum_split(in_sequence: Sequence) -> list:
    return [sum(in_sequence[::2]), sum(in_sequence[1::2])]


def plus_minus(in_sequence: Sequence) -> int:
    return - sum(in_sequence[2::2]) + sum(in_sequence[1::2]) + in_sequence[0]


def myzip(seq1: Sequence, seq2: Sequence) -> list:
    return [(seq1[i], seq2[i]) for i in range(len(seq1))]
