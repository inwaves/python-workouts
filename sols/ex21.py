def find_longest_word(filename: str) -> str:
    maxword = ""
    try:
        with open(filename) as fileobj:
            for line in fileobj:
                cand = max(line.split(" "), key=lambda s: len(s))
                if len(cand) > len(maxword):
                    maxword = cand
    except IsADirectoryError:
        pass
    return maxword


def find_all_longest_words(dirname: str) -> dict:
    import os
    return {filename: find_longest_word(filename) for filename in os.listdir(dirname)}


def hash_file(filename: str) -> str:
    from hashlib import md5
    digest = md5()
    try:
        with open(filename) as fileobj:
            for line in fileobj:
                digest.update(bytes(line, encoding="utf-8"))
        return digest.hexdigest()
    except:
        return ""

def md5_digest(dirname: str) -> dict:
    import os
    return {filename: hash_file(filename) for filename in os.listdir(dirname)}
