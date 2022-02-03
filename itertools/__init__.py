import itertools

squares = itertools.starmap(pow, [(2, 2), (3, 2), (4, 2)])

print(list(squares))
