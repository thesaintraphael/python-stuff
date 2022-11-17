# h[k] <= h[2*k + 1] and h[k] <= h[2*k + 2]
# It might raise an IndexError if any of the indices is beyond the length of the list,
# but it will never be False.


import heapq


a = [6, 2, 1, 5]
heapq.heapify(a)
print(a)  # [1, 2, 6, 5]

value = heapq.heappop(a)  # 1
print(a)  # [2, 5, 6]

heapq.heappush(a, 3)
print(a)  # [2, 3, 6, 5]
