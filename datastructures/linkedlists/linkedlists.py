from decorators import not_empty


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next

        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def reverse(self):
        previous = None
        current = self.head
        next_ = current.next

        while current:
            current.next = previous
            previous = current
            current = next_
            if next_:
                next_ = next_.next

        self.head = previous

    def append_left(self, node: Node) -> None:
        node.next = self.head
        self.head = node

    def append_right(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass

        current_node.next = node

    # insrting between 2 Nodes

    @not_empty
    def add_after(self, targeted_node_data, new_node: Node) -> None:
        for node in self:
            if node.data == targeted_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise ValueError(f"Node with data {targeted_node_data} not found")

    @not_empty
    def add_before(self, targeted_node_data, new_node: Node):

        if self.head.data == targeted_node_data:
            return self.append_left(new_node)

        prev_node = self.head
        for node in self:
            if node.data == targeted_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise ValueError(f"Node with data {targeted_node_data} not found")

    @not_empty
    def remove_node(self, targeted_node_data):

        if self.head.data == targeted_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == targeted_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise ValueError(f"Node with data {targeted_node_data} not found")

    def __getitem__(self, index: int) -> Node:

        node = self.head

        if node is None:
            raise IndexError("Empty list")

        if not index:
            return self.head

        count_iters = 0
        while node is not None:
            if count_iters == index:
                return node

            node = node.next
            count_iters += 1

        raise IndexError("list index out of range")


def main():
    llist = LinkedList()

    first_node = Node("a")
    llist.head = first_node
    # ("a -> None")

    second_node = Node("b")
    third_node = Node("c")

    first_node.next = second_node
    second_node.next = third_node

    print(llist)

    # a -> b -> c -> None

    # for i in llist:
    #     print(i, end=", ")  # iter ends at c -> None

    print(llist)
    llist.append_left(Node("d"))
    print(llist)
    # d -> a -> b -> c -> None

    llist.append_right(Node("e"))
    print(llist)
    # d -> a -> b -> c -> e -> None

    llist.add_after("c", Node("dd"))
    print(llist)
    # d -> a -> b -> c -> f -> dd -> None

    llist.add_before("b", Node("bb"))
    print(llist)
    # d -> a -> bb -> b -> c -> dd -> e -> None

    # llist.add_before("n", Node("l"))
    # exception

    llist.remove_node("bb")
    llist.remove_node("d")
    llist.remove_node("dd")
    print(llist)
    # a -> b -> c -> e -> None

    print(llist[3])

    llist.reverse()
    print(llist)


if __name__ == "__main__":
    main()
