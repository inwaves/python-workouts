def get_final_line(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as fileobj:
        for line in fileobj:
            pass

    return line.strip("\n")


def sum_from_file(fileobj) -> float:
    total = 0.0
    for line in fileobj:
        elems = line.split("\t")
        if len(elems) == 1:
            continue
        try:
            fst, snd = float(elems[0]), float(elems[1])
            total += fst * snd
        except:
            continue
    return total
