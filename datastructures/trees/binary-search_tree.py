# A binary search tree, or BST for short, is a tree whose nodes store a key that is
# greater than all of their left child nodes and less than all of their right child nodes.


class TreeNode:
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
            self.left = TreeNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = TreeNode(val)

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

    def preorder(self):

        if self.val:
            print(self.val, end=" ")

        if self.left:
            self.left.preorder()

        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()

        print(self.val, end=" ")

        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()

        if self.right:
            self.right.postorder()

        print(self.val, end=" ")

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

    def size(self):
        if self is None:
            return 0

        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def height(self):
        if self is None:
            return 0

        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))


def main():
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    tree = TreeNode()

    for num in nums:
        tree.insert(num)

    print("preorder:")
    tree.preorder()
    print("\ninorder:")
    tree.inorder()
    print("\npostorder")
    tree.postorder()

    print(f"\nSize of the tree {tree.size()}")
    print(f"Height of the tree {tree.height()}")


if __name__ == "__main__":
    main()
