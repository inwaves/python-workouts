from sols.ex6 import pl_sentence, transpose_strings, nonsensical_read

def test_pl_sentence() -> None:
    assert pl_sentence("this is a test translation") == "histay isway away esttay ranslationtay"


def test_transpose_strings() -> None:
    assert transpose_strings(["abc def ghi", "jkl mno pqr", "stu vwx yz"]) == ["abc jkl stu", "def mno vwx", "ghi pqr yz"]


def test_nonsensical_read() -> None:
    assert nonsensical_read("../sols/nonsense.txt") == "moreover times for with work"
