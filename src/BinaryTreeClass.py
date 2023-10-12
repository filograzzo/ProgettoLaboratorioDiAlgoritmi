class TreeNode:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_recursive(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        if key > root.key:
            root.right = self._insert_recursive(root.right, key)
        return root

    def insert(self, key):
        self.root = self.insert_recursive(self.root, key)

    def print_tree(self):
        self._print_inorder(self.root)

    def _print_inorder(self, node):
        if node is not None:
            self._print_inorder(node.left)
            print(node.key, end=' ')
            self._print_inorder(node.right)
