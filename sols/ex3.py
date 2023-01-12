def crop_float(x: float, before: int, after: int) -> float:
    return ((x - x % 1) % (10 ** before)) + float(f"{x%1}"[:after+2])


def add_decimal(a: float, b: float) -> str:
    from decimal import Decimal
    dec_a = Decimal(a)
    dec_b = Decimal(b)

    print(dec_a + dec_b)
    print(float(dec_a + dec_b))

    return str(dec_a + dec_b)


def run_timing() -> tuple[float, int]:
    total, count = 0.0, 0

    while user_input := input("Enter 10km run time: "):
        try:
            total += float(user_input)
            count += 1
        except ValueError as e:
            print(f"{user_input} is not a valid number.")

    print(f"Ran an average of {total/count} over {count} runs.")

    return total/count, count


if __name__ == "__main__":
    assert run_timing()  == (15.0, 3)
