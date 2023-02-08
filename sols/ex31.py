from sols.ex6 import pl_sentence

def latin_file(filename: str) -> str:
    with open(filename) as fileobj:
        return " ".join(pl_sentence(line.strip("\n")) for line in fileobj)
