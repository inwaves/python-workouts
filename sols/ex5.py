def pig_latin(in_str: str) -> str:
    punct = in_str[-1] in ",.!?(){};:'`"
    if len(set("aeiou") - set(in_str.lower())) < 4:
        return f"{in_str}way" if not punct else f"{in_str[:-1]}way{in_str[-1]}"
    else:
        ret_string = f"{in_str[1].upper()}{in_str[2:]}{in_str[0].lower()}ay" if not punct else \
            f"{in_str[1].upper()}{in_str[2:-1]}{in_str[0].lower()}ay{in_str[-1]}"
        return ret_string
