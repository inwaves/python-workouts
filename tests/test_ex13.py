from sols.ex13 import *


def test_format_sort_records() -> None:
    assert format_sort_records() == 'Putin               Vladimir            3.63\nTrump               Donald              7.85\nXi                  Jinping             10.60'


def test_generic_format_multiple_sort() -> None:
    assert generic_format_multiple_sort("length name") == 'The Dark Knight     90.00               Nolan\nThe Dark Knight Rises90.00               Nolan\nInterstellar        120.00               Nolan'
