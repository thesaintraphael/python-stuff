# implementing min HEAP data structure with list


class EmptyHeapException(Exception):
    pass


class MinHeap:
    def __init__(self, capacity: int = 10) -> None:

        if capacity <= 0:
            raise ValueError("Heap capacity must be greater than 0")

        self._elements: list[int] = []
        self._capacity = capacity

    def __len__(self) -> int:
        return self.size

    @staticmethod
    def _get_parent_index(child_index: int) -> int:
        return (child_index - 1) // 2

    @staticmethod
    def _get_left_child_index(parent_index: int) -> bool:
        return 2 * parent_index + 1

    @staticmethod
    def _get_right_child_index(parent_index: int) -> bool:
        return 2 * parent_index + 2

    def _has_left_child(self, parent_index: int) -> bool:
        return self._get_left_child_index(parent_index) < self.size

    def _hash_right_child(self, parent_index: int) -> bool:
        return self._get_right_child_index(parent_index) < self.size

    def _has_parent(self, child_index: int) -> bool:
        return self._get_parent_index(child_index) >= 0

    def _get_left_child(self, parent_index: int) -> int:
        return self._elements[self._get_left_child_index(parent_index)]

    def _get_right_child(self, parent_index: int) -> int:
        return self._elements[self._get_right_child_index(parent_index)]

    def _get_parent(self, child_index: int) -> int:
        return self._elements[self._get_parent_index(child_index)]

    def _swap(self, index_one: int, index_two: int) -> None:
        self._elements[index_one], self._elements[index_two] = (
            self._elements[index_two],
            self._elements[index_one],
        )

    def _ensure_extra_capacity(self) -> None:
        if self.size == self._capacity:
            self._capacity *= 2

    def peek(self):
        if self.size == 0:
            raise EmptyHeapException("Operation on empty heap cannot be performed")

        return self._elements[0]

    def pop(self) -> int:
        if self.size == 0:
            raise EmptyHeapException("Operation on empty heap cannot be performed")

        element = self._elements[0]
        self._elements[0] = self._elements.pop()
        self.heapify_down()

        return element

    def add(self, element: int) -> None:
        self._ensure_extra_capacity()

        self._elements.insert(self.size, element)
        self.heapify_up()

    def heapify_down(self) -> None:
        index = 0

        while self._has_left_child(index):
            smaller_child_index = self._get_left_child_index(index)

            if self._hash_right_child(index) and self._get_right_child(
                index
            ) < self._get_left_child(index):
                smaller_child_index = self._get_right_child_index(index)

            if self._elements[index] < self._elements[smaller_child_index]:
                break
            else:
                self._swap(index, smaller_child_index)

            index = smaller_child_index

    def heapify_up(self) -> None:
        index = self.size - 1

        while (
            self._has_parent(index) and self._get_parent(index) > self._elements[index]
        ):
            self._swap(self._get_parent(index), index)
            index = self._get_parent_index(index)

    @property
    def size(self) -> int:
        return len(self._elements)

    @property
    def elements(self) -> list:
        return self._elements.copy()


if __name__ == "__main__":

    heap = MinHeap()
    heap.add(10)
    heap.add(15)
    heap.add(20)
    heap.add(17)
    heap.add(25)

    print(heap.elements)

    print(heap.peek())
    print(heap.pop())

    print(heap.elements)
