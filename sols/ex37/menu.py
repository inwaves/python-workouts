from typing import Callable, Dict, Any


def menu(**kwargs: Dict[str, Callable]) -> Any:
    while choice := input("Select a function: "):
        if choice in kwargs:
            return kwargs[choice]()
        print("You didn't select a valid function!")
