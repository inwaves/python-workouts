def sum_numbers(input_str: str) -> int:
    return sum(map(int, filter(str.isnumeric, input_str.split())))


def transform_numbers_functional(numbers: list) -> list:
    incr_phone_num = lambda s: "-".join([str(int(s.split("-")[0])+1), s.split("-")[1], s.split("-")[2]])
    phone_is_changing = lambda s: s.split("-")[1][0] in "012345"
    return list(map(incr_phone_num, filter(phone_is_changing, numbers))) + list(filter(lambda v: not phone_is_changing(v), numbers))


def transform_numbers(numbers: list) -> list:
    def number_is_changing(phone_num: str) -> bool:
        elems = phone_num.split("-")
        print(elems)
        return elems[1].startswith(("0", "1", "2", "3", "4", "5"))

    def change_number(phone_num: str) -> str:
        elems = phone_num.split("-")
        return f"{str(int(elems[0])+1)}-{elems[1]}-{elems[2]}"

    return [change_number(number) if number_is_changing(number) else number for number in numbers]
