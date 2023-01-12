from sols.ex2 import *

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
