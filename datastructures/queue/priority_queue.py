from heapq import heappush, heappop
from itertools import count


class PriorityQueue:
    def __init__(self) -> None:
        self._elements = []
        self._counter = count()

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (-priority, next(self._counter), value))

    def dequeue(self):
        return heappop(self._elements)[-1]


CRITICAL = 1
IMPORTANT = 2
NEUTRAL = 3

messages = PriorityQueue()
messages.enqueue_with_priority(CRITICAL, "Critical message")
messages.enqueue_with_priority(IMPORTANT, "Important message")
messages.enqueue_with_priority(NEUTRAL, "Neutral message")
messages.enqueue_with_priority(IMPORTANT, "Another important message")

print(messages.dequeue())
print(messages.dequeue())
