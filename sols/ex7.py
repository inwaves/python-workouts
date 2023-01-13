def ubbi_dubbi(in_str: str) -> str:
    return "".join(f"ub{letter}" if letter in "aeiou" else f"{letter}" for letter in in_str )


def url_encode(in_str: str) -> str:
    letters_and_numbers = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    return "".join(f"%{hex(ord(character))[2:]}" if character not in letters_and_numbers else f"{character}" for character in in_str )
