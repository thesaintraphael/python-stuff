from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])


point = Point(1, 2)
print(f"point = {point}")
print(f"x: {point.x}, y: {point.y}")

# point.x = 9 # AttributeError: can't set attribute (namedtuples are immutable)
print(point.x)


Point_2 = namedtuple("Point", "x", "_y")
# ValueError: Field names can't start with underscore: _y
