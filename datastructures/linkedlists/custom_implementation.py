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

    def add_after(self, targed_node_data, new_node: Node) -> None:
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == targed_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f"Node with data {targed_node_data} not found")

    def add_before(self, targeted_node_data, new_node: Node):
        if self.head is None:
            raise Exception("Lits is empty")

        if self.head.data == targeted_node_data:
            return self.append_left(new_node)

        prev_node = self.head
        for node in self:
            if node.data == targeted_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception(f"Node with data {targeted_node_data} not found")

    def remove_node(self, targeted_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == targeted_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == targeted_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception(f"Node with data {targeted_node_data} not found")


llist = LinkedList()
print(llist)


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
