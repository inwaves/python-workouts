def strsort(in_str: str) -> str:
    return "".join([chr(i) for i in quicksort([ord(character) for character in in_str])])


def quicksort(li: list) -> list:
    if len(li) <= 1:
        return li
    return quicksort([el for el in li[1:] if el <= li[0]]) + [li[0]] + quicksort([el for el in li[1:] if el > li[0]])
