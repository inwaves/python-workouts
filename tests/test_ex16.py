from sols.ex16 import *

def test_dictdiff() -> None:
    d1 = {"a": 1, "b": 2, "c": 3, "d": 5}
    d2 = {"a": 1, "b": 2, "c": 4}
    result = {"c": [3, 4], "d": [5, None]}
    assert dictdiff(d1, d2) == result


def test_dictmerge() -> None:
    d1 = {"a": 3}
    d2 = {"a": 4, "b": 5}
    d3 = {"c": 1, "d": 9}

    assert dictmerge(*[d1, d2, d3]) == {"a":4, "b": 5, "c": 1, "d": 9}


def test_dictpartition() -> None:
    d1 = {"a": 4, "b": 5, "e": 16, "d": 9}

    def is_vowel(tup: tuple) -> bool:
        return tup[0] in "aeiou"

    assert dictpartition(d1, is_vowel) == ({"a": 4, "e": 16}, {"b": 5, "d": 9})
    assert dictpartition(d1, lambda tup: tup[0].isnumeric()) == ({}, {"a": 4, "e": 16, "b": 5, "d": 9})
