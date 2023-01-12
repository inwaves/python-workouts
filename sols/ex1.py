def dec_to_base(n: int, b: int) -> str:
    if n == 0:
        return str(n)
    digits = []
    while n:
        digits += [str(n % b)]
        n //= b
    return "".join(digits[::-1])


def base_to_dec(n: str, b: int) -> str:
    """
    >>> base_to_dec("10", 2)
    2
    """
    num = 0
    for i in range(len(n)-1, -1, -1):
        print(f"{i=}")
        if int(n[i]) != 0:
            print(f"Adding {b ** (i * int(n[i]))}")
            num += b ** (len(n)-i * int(n[i]))
    return str(num)
