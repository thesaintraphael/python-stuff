import itertools


counter = itertools.count(start=1, step=-3.5)

print(next(counter))  # 1
print(next(counter), end="\n\n")  # -2.5

data = [100, 200, 300, 400]

daily_data = list(zip(itertools.count(), data))

print(daily_data)
