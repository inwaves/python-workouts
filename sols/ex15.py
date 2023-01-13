def get_rainfall() -> None:
    rainfalls = {}
    while in_str := input("Enter city: "):
        rainfall = input("Rainfall: ")
        try:
            rain_int = int(rainfall)
        except:
            raise ValueError("Not a valid value for rainfall!")

        # Solution with fallback get.
        rainfalls[in_str] = (rainfalls.get(in_str, (0, 0))[0] + 1, rainfalls.get(in_str, (0, 0))[1] + int(rain_int))

        # "Classic" solution with an if block.
        # if in_str in rainfalls:
        #     rainfalls[in_str] += rain_int
        # else:
        #     rainfalls[in_str] = rain_int

    print("\n".join(f"{city}, avg: {rainfall[1]/rainfall[0]}, total: {rainfall[1]}" for city, rainfall in rainfalls.items()))


def count_words(filepath: str) -> dict:
    word_lengths = {}
    with open(filepath, "r", encoding="utf-8") as fileobj:
        for line in fileobj:
            for word in line.split(" "):
                word = word.strip("\n")
                print(f"{word=}")
                word_lengths[len(word)] = word_lengths.get(len(word), 0) + 1
    return word_lengths
