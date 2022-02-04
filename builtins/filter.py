from itertools import filterfalse


numbers = [-2, 1, -6, 5]

pos_numbers = list(filter(lambda num: num > 0, numbers))
print(pos_numbers)

neg_numbers = list(filterfalse(lambda num: num >= 0, numbers))
print(neg_numbers)
