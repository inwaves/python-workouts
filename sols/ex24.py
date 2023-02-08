import sys
import cProfile

def reverse_lines(input_filename: str, output_filename: str) -> None:
    """Side-effect only function."""

    if not len(input_filename) or not len(output_filename):
        raise ValueError(f"Filename problem: {input_filename=}, {output_filename=}")

    rev = lambda s: s[::-1]

    # Interesting note: if the file is large, it's better to
    # gather the lines in a generator than in a list. If it's small,
    # the generator actually takes up more space than the list.
    gen = (f"{rev(line)[1:]}\n" for line in open(input_filename))

    with open(output_filename, "w", encoding="utf-8") as file_out:
        # You could always just process sequentially here, reading
        # and writing one at a time.
        for line in gen:
            file_out.write(line)

if __name__ == "__main__":
    cProfile.run('reverse_lines("data/simple", "data/reversed")')
