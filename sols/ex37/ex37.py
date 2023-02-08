from typing import Literal
from sols.ex37.menu import menu
from sols.ex37.stuff import *


def func_a() -> Literal["A"]:
    return "A"

def func_b() -> Literal["B"]:
    return "B"

if __name__ == "__main__":
    # return_value = menu(a=func_a, b=func_b)
    # print(f"Result is: {return_value}")

    bar()
