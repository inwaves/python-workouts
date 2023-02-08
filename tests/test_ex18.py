from sols.ex18 import *


def test_get_final_line() -> None:
    assert get_final_line("data/nonsense.txt") == "Pig Latin examples won't work"


def test_sum_from_file() -> None:
    from io import StringIO

    file = StringIO("""7\t10
    13\t10
    abc\tdef
    9\tfoo
    """)

    assert sum_from_file(file) == 200.0
