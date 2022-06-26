# A binary search tree, or BST for short, is a tree whose nodes store a key that is
# greater than all of their left child nodes and less than all of their right child nodes.


class Node:
    def __init__(self, val=None) -> None:
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val) -> None:

        if self.val is None:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = Node(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = Node(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left

        return current.val

    def get_max(self):

        current = self
        while current.right is not None:
            current = current.right

        return current.val

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val)

        if self.right is None:
            return False
        return self.right.exists(val)

    def inorder(self, vals):

        if self.left:
            self.left.inorder(vals)

        if self.val:
            vals.append(self.val)

        if self.right:
            self.right.inorder(vals)

        return vals

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals

    def delete(self, val):

        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self


def main():
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    tree = Node()

    for num in nums:
        tree.insert(num)

    print("preorder:")
    print(tree.preorder([]))
    print()

    print("postorder:")
    print(tree.postorder([]))
    print()

    print("inorder:")
    print(tree.inorder([]))
    print()

    print(f"Max values is: {tree.get_max()}")
    print(f"Min values is: {tree.get_min()}")

    print(tree.delete(3).val)
    print(tree.inorder([]))


if __name__ == "__main__":
    main()
