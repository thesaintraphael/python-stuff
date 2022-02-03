from itertools import chain

letters = ["a", "b", "c", "d"]
numbers = [1, 2, 3, 4]
names = ["Alex", "Jo"]

combined = list(chain(numbers, letters, names))

print(combined)
