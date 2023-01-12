def hex_output(hex_num: str) -> int:
    hex_special_chars = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}

    if not isinstance(hex_num, str):
        hex_num = str(hex_num)

    if "0x" in hex_num:
        hex_num = hex_num[2:]

    dec_num = 0
    for i, digit in enumerate(reversed(hex_num)):
        try:
            int_digit = int(digit)
        except ValueError:
            if digit.lower() in hex_special_chars:
                int_digit = hex_special_chars[digit.lower()]
            else:
                raise ValueError

        dec_num += int_digit * (16**i)

    return dec_num
