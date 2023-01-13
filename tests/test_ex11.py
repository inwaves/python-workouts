from sols.ex11 import *


def test_alphabetise_names() -> None:
    SORTED_PEOPLE = [
        {'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
        {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'},
        {'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'},
     ]

    assert alphabetise_names() == SORTED_PEOPLE


def test_sort_magnitude() -> None:
    assert sort_magnitude(*[-3, -6, 14, 3, -9, 7]) == [-3, 3, -6, 7, -9, 14]


def test_sort_vowels() -> None:
    assert sort_vowels(["boom", "shlomp", "three", "elk"]) == ["shlomp", "elk", "boom", "three"]


def test_sort_inner_lists() -> None:
    assert sort_inner_lists([[1, 2], [6, 1, 3], [0, 1], []]) == [[], [0, 1], [1, 2], [6, 1, 3]]
