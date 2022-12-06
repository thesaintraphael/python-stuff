from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Person:
    name: str


class PersonSimple:
    def __init__(self, name: str) -> None:
        self.name = name


if __name__ == "__main__":

    person1 = Person("Rafael")
    person2 = Person("Rafael")

    person3 = PersonSimple("Rafael")
    person4 = PersonSimple("Rafael")

    set_ = set([person1, person2])
    print(set_)  # {Person(name='Rafael')} only one object

    set_1 = set([person3, person4])
    print(set_1)  # both objects present


# NOTE By default dataclasses are unhashable,
# that's it is not possible to add them to set.
# We should set eq and frozen to True to handle this situation
