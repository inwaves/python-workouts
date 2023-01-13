from collections import namedtuple

PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

MOVIES = [('Interstellar', 120, 'Nolan'),
          ('The Dark Knight Rises', 90, 'Nolan'),
          ('The Dark Knight', 90, 'Nolan')]

Person = namedtuple("Person", "first last arrival")
Movie = namedtuple("Movie", "name length director")

def format_sort_records() -> str:
    people = [Person(*tup) for tup in PEOPLE]
    return "\n".join(f"{person.last:<20s}{person.first:<20s}{person.arrival:>4.2f}".strip() for person in sorted(people, key=lambda person: (person.last, person.first)))


def generic_format_sort(sort_by: str) -> str:
    records = [Movie(*tup) for tup in MOVIES]
    return "\n".join(f"{record.name:<20s}{record.length:<4.2f}{record.director:>20s}".strip() for record in sorted(records, key=lambda record: getattr(record, sort_by, record[0])))


def generic_format_multiple_sort(sort_by: str) -> str:
    records = [Movie(*tup) for tup in MOVIES]
    return "\n".join(f"{record.name:<20s}{record.length:<4.2f}{record.director:>20s}".strip() for record in sorted(records, key=lambda record: tuple([getattr(record, sort_item, record[0]) for sort_item in sort_by.split(" ")])))
