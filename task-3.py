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

    def find_sum(self):
        return self._find_sum(self.root)

    def _find_sum(self, node):
        if node is None:
            return 0
        return node.key + self._find_sum(node.left) + self._find_sum(node.right)


if __name__ == "__main__":
    tree = BinaryTree()
    values = [20, 8, 22, 4, 12, 10, 14]
    for value in values:
        tree.insert(value)

    total_sum = tree.find_sum()
    print(f"Сума всіх значень у дереві: {total_sum}")
