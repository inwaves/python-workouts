from sols.ex30 import *


def test_flatten() -> None:
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
