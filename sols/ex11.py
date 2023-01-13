PEOPLE = [
    {'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
    {'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'},
    {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'}
 ]


def alphabetise_names() -> list:
    return sorted(PEOPLE, key=lambda d: (d["last"], d["first"]))


def sort_magnitude(*integers: int) -> list:
    return sorted(integers, key=lambda x: x if x >= 0 else -x)


def sort_vowels(strings: list) -> list:
    def count_vowels(s: str) -> int:
        if len(s) == 0:
            return 0
        vowels = set("aeiou")
        from collections import Counter as C
        letter_counts = C(s)
        return sum(letter_counts[k] for k in letter_counts if k in vowels)

    return sorted(strings, key=lambda s: count_vowels(s))


def sort_inner_lists(lol: list) -> list:
    return sorted(lol, key=lambda li: sum(li))
