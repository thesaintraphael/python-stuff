import itertools


cycler = itertools.cycle([1, 2])

print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))


# similar to itertools.repeat() but takes list
