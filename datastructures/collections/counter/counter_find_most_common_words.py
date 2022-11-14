import re
from collections import Counter

cnt = Counter()

with open("text.txt", "r") as file:
    words = re.findall(r'\w+', file.read().lower())

print(Counter(words).most_common(10))  # listing most common words
