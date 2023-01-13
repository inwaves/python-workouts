from sols.ex8 import *


def test_strsort() -> None:
    assert quicksort([3, 1, 9, 10, 4]) == [1, 3, 4, 9, 10]
    assert quicksort(["Tom", "Dick", "Harry"]) == ["Dick", "Harry", "Tom"]
    assert strsort("cba") == "abc"
