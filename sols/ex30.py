def flatten(li: list) -> list:
    new_list = []
    for el in li:
        if isinstance(el, list):
            new_list += flatten(el)
        else:
            new_list += [el]
    return new_list


def flatten_one_liner(li: list) -> list:
    return [x for sublist in li for x in (flatten_one_liner(sublist) if isinstance(sublist, list) else [sublist])]
