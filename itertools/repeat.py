import itertools


repeater = itertools.repeat(2, times=2)

print(next(repeater))
print(next(repeater))

try:
    print(next(repeater))
except StopIteration:
    print("Limit is passed\n")


squares = list(map(pow, range(10), itertools.repeat(2)))
print(squares)
