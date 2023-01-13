from sols.ex5 import pig_latin_simple

def pl_sentence(in_str: str) -> str:
    return " ".join(pig_latin_simple(word) for word in in_str.split(" "))


def transpose_strings(in_list: list) -> list:
    """Input is a list of strings with multiple words. Concatenate the first words of all strings,
    the second ones of all strings, etc."""
    return [" ".join(tup) for tup in list(zip(*[sentence.split(" ") for sentence in in_list]))]


def nonsensical_read(filepath: str) -> str:
    words = []
    with open(filepath, "r", encoding="utf-8") as file_stream:
        for i in range(5):
            words += [next(file_stream).split(" ")[i]]

    return " ".join(words).strip()
