from sols.ex26 import *

def test_calc() -> None:
    assert calc("(+ 1 2)") == 3
    assert calc("(* 1 2 3 4 5)") == 120


def test_mymap() -> None:
    assert mymap(lambda el: el**2, (3, 2, 1)) == (9, 4, 1)
