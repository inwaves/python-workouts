from typing import Any, Generator, Iterable, Callable
from time import time, sleep

def timing_generator(data: Iterable[Any]) -> Generator:
    previous_time = 0.0
    for idx, item in enumerate(data):
        current_time = time()
        elapsed = current_time - previous_time if idx > 0 else 0
        previous_time = current_time
        yield elapsed, item


def scheduled_generator(data: Iterable[Any], timeout: float) -> Generator:
    previous_time = None
    for item in data:
        current_time = time()
        elapsed = current_time - (previous_time or time())
        print(f"{previous_time=}, {current_time=}")
        print(f"For item: {item}, {elapsed:.2f}s have elapsed.")
        if elapsed < timeout and previous_time is not None:
            print(f"Timeout not yet complete; sleeping for {timeout-elapsed:.2f}s.")
            sleep(timeout-elapsed)
        previous_time = time()
        yield item

def truth_generator(data: Iterable[Any], predicate: Callable[[Any], bool]) -> Generator:
    yield from (elem for elem in data if predicate(elem))
