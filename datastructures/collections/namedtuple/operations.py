from collections import namedtuple


Person = namedtuple("Person", "name age height")

# creating a namedtuple from iterable

john = Person._make(["John", 30, 180])


# Converting a namedtuple to a dictionary

print(john._asdict())
print(id(john) != id(john._asdict()))  # _asdict() returns a new dictionary


# Replacing Fields in existing namedtuple

print(f"old age = {john.age}")

john_ = john._replace(age=31)
print(f"new age = {john_.age}")


print(id(john) != id(john_))
# _replace() returns a new namedtuple, because it is immutable
