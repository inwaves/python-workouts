from sols.ex12 import *

def test_most_repeating_word() -> None:
    assert most_repeating_word_alt(["this", "is", "an", "elementary", "test", "example"]) == "elementary"


def test_most_repeating_word_vowel() -> None:
    assert most_repeating_word_vowel(["lemmmma", "element"]) == "element"
