from functools import partial


def add(a, b):
    print(a, b)
    return a + b


add_one = partial(add, 1)
print(add_one(4))  # 5

# by default in partial(add, 1) 1 is a first argument of add function
# you can do something like partial(add, b=1)
# but partial(add, a=1) will raise a TypeError: add() got multiple values for argument 'a'
