from sols.ex25 import *


def test_myxml() -> None:
    assert myxml("foo") == "<foo></foo>"
    assert myxml("foo", "bar") == "<foo>bar</foo>"
    assert myxml("foo", "bar", a=1, b=2, c=3) == '<foo a="1" b="2" c="3">bar</foo>'


def test_variadic_product() -> None:
    assert variadic_product(1, 2, 3) == 6
    assert variadic_product(10, 6) == 60
    assert variadic_product(2, 2, 2, 2, 2) == 32


def test_anyjoin() -> None:
    assert anyjoin(["abc", "def"], "*") == "*".join(["abc", "def"])
    assert anyjoin(("abc", "def"), "_") == "_".join(("abc", "def"))
    assert anyjoin((100, 312), "_") == "100_312"
