from typing import Any
from collections import deque
from mixins import IterableMixin


class Queue(IterableMixin):
    def __init__(self, *elements: Any):
        self._elements = deque(elements)

    def enqueue(self, value: Any):
        self._elements.append(value)

    def dequeue(self) -> Any:
        return self._elements.popleft()

    def empty(self) -> bool:
        return not self._elements


fifo = Queue()


print(fifo.empty())  # True

fifo.enqueue(1)
fifo.enqueue(2)
fifo.enqueue(3)

print(fifo.empty())  # False


# for item in fifo:
#     print(item, "popped from queue")

print(fifo.dequeue())  # 1
print(fifo.dequeue())  # 2
print(fifo.dequeue())  # 3
# print(fifo.dequeue())  # IndexError: pop from an empty deque
