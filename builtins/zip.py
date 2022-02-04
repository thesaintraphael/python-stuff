from itertools import zip_longest


letters = ["a", "b", "c"]
numbers = [1, 2, 3, 4]


# 4 will not appear in zip because it has no respective element in letters list
zipped = list(zip(letters, numbers))
print(zipped)


print()
for letter, number in zip(letters, numbers):
    print(f"{letter}'s respective value is {number}")


# It is possible to give a default value for all elements with no respective elements from other list
zipped_long = list(zip_longest(letters, numbers, fillvalue="d"))
print(zipped_long)
print()


# Unzipping
letters, numbers = zip(*zipped)
print(numbers, "\n", letters)
print()


# Zip Dicts
dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}

for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
    print(k1, ' ==> ', v1)
    print(k2, ' ==> ', v2)

print()


# Building dicts
new_dict = dict(zip(letters, numbers))
print(new_dict)
