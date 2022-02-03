import itertools

numbers_a = [1, 2]
numbers_b = [3]

# Cartesian product
products = itertools.product(numbers_a, numbers_b, repeat=1)
print(list(products), end="\n\n")

products = itertools.product(numbers_a, numbers_b, repeat=2)
print(list(products))
