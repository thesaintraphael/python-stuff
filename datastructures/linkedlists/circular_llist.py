# in circular lists the last Node is pointing the head Node instead of pointing None
# In terms of implementation, circular linked lists are very similar to singly linked list
# The only difference is that you can define the starting point when you traverse the list:


from linkedlists import Node


class CircularLinkedList:

    def __init__(self) -> None:
        self.head = None

    def traverse(self, starting_point=None):

        if starting_point is None:
            starting_point = self.head

        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next

        yield node

    def print_list(self, starting_point=None):

        nodes = []
        for node in self.traverse(starting_point=starting_point):
            nodes.append(str(node))

        print(" -> ".join(nodes))


print("---------------------------------------------------------------------")

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d
d.next = a


circular_llist = CircularLinkedList()
circular_llist.head = a

circular_llist.print_list(starting_point=c)
