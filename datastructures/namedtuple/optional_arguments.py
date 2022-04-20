from collections import namedtuple

Developer = namedtuple(
    "Developer", "name level language", defaults=("Junior", "Python")
)

# level and language are optional (default values are set)

dev = Developer(name="John")
# name is not optional, because it does not have a default value
print(dev)
