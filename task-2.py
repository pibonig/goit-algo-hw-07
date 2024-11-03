class BinaryTree:
    class TreeNode:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = self.TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = self.TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = self.TreeNode(key)
            else:
                self._insert(node.right, key)

    def find_min(self):
        if self.root is None:
            raise ValueError("Дерево порожнє")
        current = self.root

        while current.left is not None:
            current = current.left

        return current.key


if __name__ == "__main__":
    tree = BinaryTree()
    values = [20, 8, 22, 4, 12, 10, 14]
    for value in values:
        tree.insert(value)

    min_value = tree.find_min()
    print(f"Найменше значення в дереві: {min_value}")
