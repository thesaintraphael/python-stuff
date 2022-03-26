from dataclasses import dataclass
from functools import partial
import timeit
from unicodedata import name


# using __dict__ method to access instance variables
@dataclass
class Person:
    first_name: str
    second_name: str


# available in python 3.10+
@dataclass(slots=True)
class PersonSlots:
    first_name: str
    second_name: str


def get_set_delete(person: Person | PersonSlots) -> None:
    person.second_name = "Targaryen"
    person.second_name
    del person.second_name


def main():
    person = Person("Jon", "Snow")
    person_slots = PersonSlots("Jon", "Snow")

    no_slots_time = min(timeit.repeat(partial(get_set_delete, person), number=10_000))
    slots_time = min(
        timeit.repeat(partial(get_set_delete, person_slots), number=10_000)
    )

    print(f"No slots time: {no_slots_time}")
    print(f"Slots time: {slots_time}")

    print(
        f"% performance improvement: {(no_slots_time - slots_time) / no_slots_time:.2%}"
    )


if __name__ == "__main__":
    main()


# NOTE: slots fails in multiple inheritance
