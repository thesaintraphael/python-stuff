import itertools


def lt_2(num):
    if num < 2:
        return True
    return False


letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 0, 4]

selectors = [True, True, False, True]

# a, b, d is result based on corresponding selectors
result = itertools.compress(letters, selectors)

result = itertools.dropwhile(lt_2, numbers)  # gets all after meeting true
print(list(result))

# gets everything untill meeting false
result = itertools.takewhile(lt_2, numbers)
print(list(result))
