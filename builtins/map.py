# map(function, iterable[, iterable1, iterable2,..., iterableN])

numbers = [1, 2, 3]


def square(num: int) -> int:
    return num**2


squares = list(map(square, numbers))
squares_lambda = list(map(lambda num: num**2, numbers))

print(squares)
print(squares_lambda)

first_it = [1, 2, 3]
second_it = [4, 5, 6, 7]

pows = list(map(pow, first_it, second_it))
print(pows)
