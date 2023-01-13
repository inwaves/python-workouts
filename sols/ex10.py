from typing import Any, List

def mysum(*args: Any) -> Any:
    if len(args) == 0:
        return args
    out = args[0]
    for item in args[1:]:
        out += item
    return out


def mysum_gt(floor: Any, *args: Any) -> Any:
    if len(args) == 0:
        return args
    out = floor
    for item in args:
        if item > floor:
            out += item
    return out - floor


def sum_numeric(*args: Any) -> Any:
    out = 0
    for item in args:
        try:
            as_int = int(item)
            out += as_int
        except ValueError:
            continue

    return out
