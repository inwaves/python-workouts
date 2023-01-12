# Take in a sequence of numbers, return their sum.
# The number of arguments is not known in advance.

from typing import Tuple, Any


def ssum(*args: int | float) -> int | float:
    total = 0
    for el in args:
        total += el

    return total


def ssum2(args: list[int | float], start: int | float) -> int | float:
    return ssum(*args) + start


def avg(args: list[int | float]) -> float:
    return ssum(*args) / len(args)


def summarise_strings(strings: list[str]) -> Tuple[float, float, float]:
    m = len(min(strings, key=lambda string: len(string)))
    M = len(max(strings, key=lambda string: len(string)))
    a = avg([len(string) for string in strings])
    return (m, M, a)


def sumif_possible(args: Any) -> int:
    total = 0

    # Here it'd be more interesting if you could assert
    # hasattr(obj, "__add__") and that the output of that
    # operation is an integer. But it's faster to just check
    # that you can convert to an integer.
    for el in args:
        try:
            el_int = int(el)
            total += el_int
        except ValueError:
            pass

    return total


def test_ssum() -> None:
    assert ssum(*[1, 2, 3, 4, 5]) == 15
    assert ssum(*[]) == 0
    assert ssum(*[-3, 3, 1, -1]) == 0


def test_ssum2() -> None:
    assert ssum2([1, 2, 3], 4) == 10


def test_avg() -> None:
    assert avg([1, 2, 3]) == 2


def test_summarise_strings() -> None:
    strings = ["a", "boop"]
    assert summarise_strings(strings) == (1, 4, 2.5)


def test_sumif_possible() -> None:
    assert sumif_possible([13, "foo", False, 7.3]) == 20
