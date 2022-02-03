import itertools
import operator

numbers = [1, 2, 3, 4]

result = itertools.accumulate(numbers, operator.mul)

print(list(result))
