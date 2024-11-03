class BinarySearchTree:
    class TreeNode:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = self.TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = self.TreeNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = self.TreeNode(value)
            else:
                self._insert(node.right, value)

    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value


if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [10, 5, 15, 3, 7, 12, 18]
    for value in values:
        bst.insert(value)

    result = bst.find_max()
    print("Максимальне значення у дереві:", result)
