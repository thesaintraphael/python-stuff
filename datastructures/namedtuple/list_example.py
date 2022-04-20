from collections import namedtuple


Person = namedtuple("Person", "name children")
john = Person("Jogn Doe", ["Timmy", "Tommy"])

print(john.children)
john.children.append("Tina")
print(john.children)


# Namedtuples can contain mutable objects
