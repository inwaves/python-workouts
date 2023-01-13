from collections import Counter as C


def most_repeating_word(strings: list) -> str:
    letter_counts = {s: C(s.lower()) for s in strings}
    return sorted(strings, key=lambda s: max(letter_counts[s]), reverse=True)[0]


def most_repeating_word_alt(strings: list) -> str:
    return max(strings, key=lambda string: C(string).most_common(1)[0][1])


def most_repeating_word_vowel(strings: list) -> str:
    return max(strings,
               key=lambda string: C({letter: count for letter, count in C(string).items() if letter in "aeiou"}).most_common(1)[0][1])
