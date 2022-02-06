def my_generator():

    yield 1
    yield 2
    yield 3


g = my_generator()

# value = next(g)  # 1
# value = next(g)  # 2
# value = next(g)  # 3
# value = next(g)  StopIteration

# print(sum(g))
print(sorted(g))  # [1, 2, 3]
