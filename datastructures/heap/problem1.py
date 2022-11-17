import heapq

results = """\
Christania Williams      11.80
Marie-Josee Ta Lou       10.86
Elaine Thompson          10.71
Tori Bowie               10.83
Shelly-Ann Fraser-Pryce  10.86
English Gardner          10.94
Michelle-Lee Ahye        10.92
Dafne Schippers          10.90
"""

smallest_3 = heapq.nsmallest(
    n=3, iterable=results.splitlines(), key=lambda line: float(line.split()[-1])
)

largest_3 = heapq.nlargest(
    3, results.splitlines(), key=lambda line: float(line.split()[-1])
)


print("\n".join(smallest_3))
print()
print("\n".join(largest_3))
