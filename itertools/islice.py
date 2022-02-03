import itertools


# similar to list slicing. have start and stop points and steps
result = list(itertools.islice(range(10), 1, 5, 2))

# 1 arg in slice represents ==> stop point, 2 ==> start-stop, 3 ==> start-stop-step

print(result)
print()

with open("text.txt", "r") as file:
    header = itertools.islice(file, 3)  # taking first 3 lines


    for line in header:
        print(line, end="")
