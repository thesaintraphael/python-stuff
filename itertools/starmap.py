import itertools

# for map this line of code wil raise a TypeError
squares = list(itertools.starmap(pow, [(2, 2), (3, 2), (4, 2)]))

print(squares)
