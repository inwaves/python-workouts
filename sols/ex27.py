from string import punctuation
from typing import Callable


def create_pwd_generator(seed: str) -> Callable:
    def pwd_from_len(length: int) -> str:
        import random
        return "".join(random.choice(seed) for _ in range(length))
    return pwd_from_len


def create_pwd_checker(min_upper: int, min_lower: int, min_punct: int, min_digits: int) -> Callable:
    def check_pwd(pwd: str) -> bool:
        import string
        upper = sum(char.isupper() for char in pwd)
        lower = sum(char.islower() for char in pwd)
        punct = sum(char in string.punctuation for char in pwd)
        digit = sum(char.isdigit() for char in pwd)
        return all([upper >= min_upper, lower >= min_lower, punct >= min_punct, digit >= min_digits])
    return check_pwd
