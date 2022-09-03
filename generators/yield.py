numbers = [1, 2, 3, 4, 5]


def yield_from_list():
    """Yielding from a list"""
    yield from numbers


print("Yielding from a list")
for i in yield_from_list():
    print(i)


def generator1():
    yield from range(1, 6)


def generator2():
    yield from range(6, 11)


def yield_from_generators():
    """Yielding from generators"""

    # possible to chain and yield
    yield from generator1()
    yield from generator2()


print("Yielding from generators")
for i in yield_from_generators():
    print(i)
