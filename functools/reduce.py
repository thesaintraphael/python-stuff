from functools import reduce

numbers = [1, 2, 3, 4]

# similar to itertools.accumulate but this one returns only one reult(integers)
result = reduce(lambda a, b: a+b, numbers, 10)
print(result)

# it is possible to give an initatior to reduce.
# it will behave as a first elemnent of a list in this casse
