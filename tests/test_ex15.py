from sols.ex15 import *

def test_count_words() -> None:
    assert count_words("data/words.txt") == {1: 1, 3: 2, 5: 3, 6: 2}
