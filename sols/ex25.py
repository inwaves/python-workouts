from typing import Sequence

def myxml(tagname: str = "foo", content: str = "", **attrs) -> str:
    attrib_string = "".join(f' {key}="{value}"' for key, value in attrs.items())
    return f'<{tagname}{attrib_string}>{content}</{tagname}>'


def variadic_product(*args) -> float:
    import operator
    from functools import reduce
    return float(reduce(operator.mul, args))


def anyjoin(elems: Sequence, separator: str) -> str:
    reprs = list(map(str, elems))
    ret_str = ""
    for rep in reprs:
        ret_str += f"{rep}{separator}"

    return ret_str[:-len(separator)]
