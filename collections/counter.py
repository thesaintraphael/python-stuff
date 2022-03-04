from collections import Counter

cnt = Counter()

for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1

print(cnt)  # Counter({'blue': 3, 'red': 2, 'green': 1})
print(cnt['blue'])  # 3
print(cnt['yellow'])  # 0

cnt['yellow'] = 1
del cnt['yellow']


# .elements()
# Return an iterator over elements repeating each as
# many times as its count. Elements are returned in the order
# first encountered. If an element’s count is less than one,
# elements() will ignore it.


# .total()
# Compute the sum of the counts


# Subtract

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4, e=9)
c.subtract(d)
# print(c)  # Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6, 'e': -9})

# c.clear()                        reset all counts
# list(c)                          list unique elements
# set(c)                           convert to a set
# dict(c)                          convert to a regular dictionary
# c.items()                        convert to a list of (elem, cnt) pairs
# Counter(dict(list_of_pairs))     convert from a list of (elem, cnt) pairs
# c.most_common()[:-n-1:-1]        n least common elements
# +c                               remove zero and negative counts
