from typing import Any, Callable, Iterable, Sequence

def calc(expr: str) -> float:
    import operator
    from functools import reduce
    operations = {"+": operator.add, "-": operator.sub, "//": operator.floordiv,
                  "/": operator.truediv, "%": operator.mod, "**": operator.pow, "*": operator.mul}
    operator, operands = expr.strip("()").split(maxsplit=1)

    return reduce(operations[operator], list(map(int, operands.split())))


def mymap(func: Callable[[Any], Any], iterable: Iterable) -> Sequence:
    iter_type = type(iterable)
    return iter_type([func(item) for item in iterable])
