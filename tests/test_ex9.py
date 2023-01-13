from sols.ex9 import *


def test_firstlast() -> None:
    assert firstlast([1, 2, 3, 4]) == [1, 4]
    assert firstlast("abcd") == ["a", "d"]


def test_square() -> None:
    assert square(3) == 9
    assert square(4.0) == 16.0
    assert square(1+0j) == 1+0j


def test_homerolled_max() -> None:
    assert homerolled_max(("ab", "cd", "def")) == "def"
    assert homerolled_max(["a","b","cd"]) == "cd"


def test_sum_split() -> None:
    assert sum_split([10, 20, 30, 40, 50, 60]) == [90, 120]


def test_plus_minus() -> None:
    assert plus_minus([10, 20, 30, 40, 50, 60]) == 50


def test_myzip() -> None:
    assert myzip([10, 20, 30], 'abc') == [(10, 'a'), (20, 'b'), (30, 'c')]
