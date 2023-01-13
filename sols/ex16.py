from typing import Callable


def dictdiff(d1: dict, d2: dict) -> dict:
    res = {}
    for k in set(d1.keys()) | set(d2.keys()):
        v1 = d1.get(k, None)
        v2 = d2.get(k, None)
        if v1 != v2:
            res[k] = [v1, v2]

    return res


def dictmerge(*dicts: dict) -> dict:
    """Reimplements the | operator for dicts."""

    def _dictmerge(d1: dict, d2: dict) -> dict:
        out = {}
        for key in set(d1.keys()) | set(d2.keys()):
            v1 = d1.get(key)
            v2 = d2.get(key)
            if v2 is None:
                out[key] = v1
            else:
                out[key] = v2
        return out

    accumulate = dicts[0]
    for d1 in dicts[1:]:
        accumulate = _dictmerge(accumulate, d1)

    return accumulate


def dictpartition(d: dict, f: Callable[[tuple], bool]) -> tuple:
    d1, d2 = {}, {}
    for key, value in d.items():
        if f((key, value)):
            d1[key] = value
        else:
            d2[key] = value
    return (d1, d2)
