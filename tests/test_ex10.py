from sols.ex10 import *

def test_mysum() -> None:
    assert mysum("abc", "def") == "abcdef"
    assert mysum([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert mysum(1, 2, 3) == 6


def test_mysum_gt() -> None:
    assert mysum_gt(10, 5, 20, 30, 6) == 50


def test_sum_numeric() -> None:
    assert sum_numeric(10, 20, 'a', '30', 'bcd') == 60
