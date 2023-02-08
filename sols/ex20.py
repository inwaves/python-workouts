def wc(filepath: str) -> tuple:
    line_ct, word_ct, char_ct = 0, 0, 0
    with open(filepath) as fileobj:
        for line in fileobj:
            line_ct += 1
            words = set([word for word in line.split(" ") if len(word) and word != "\n"])
            word_ct += len(words)
            char_ct += len(line)

    return line_ct, word_ct, char_ct


def file_sizes() -> dict:
    import os
    return {file: os.stat(file).st_size for file in os.listdir()}
