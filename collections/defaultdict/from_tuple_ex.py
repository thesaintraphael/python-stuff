from collections import defaultdict, Counter

dd = defaultdict(list)

dep = [
    ("Sales", "John Doe"),
    ("Sales", "Martin Smith"),
    ("Accounting", "Jane Doe"),
    ("Marketing", "Elizabeth Smith"),
    ("Marketing", "Adam Doe"),
]


for department, employee in dep:
    dd[department].append(employee)


print(dd)
