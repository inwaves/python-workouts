from sols.ex29 import *


def test_sum_numbers() -> None:
    assert sum_numbers("10 abc 20 de44 30 55fg 40") == 100


def test_transform_numbers_functional() -> None:
    assert transform_numbers_functional(['123-456-7890', '123-333-4444', '123-777-8888']) == ['124-456-7890', '124-333-4444', '123-777-8888']
    assert transform_numbers(['123-456-7890', '123-333-4444', '123-777-8888']) == ['124-456-7890', '124-333-4444', '123-777-8888']
