from BinaryTreeClass import BinaryTree
from RedBlackTreeClass import RedBlackTree


albero = BinaryTree()
albero.insert(5)
albero.insert(7)
albero.insert(57)
albero.insert(54)
albero.insert(1)
albero.insert(5)
albero.insert(77)
albero.insert(589)
albero.insert(98)
albero.insert(3)
alberoarray = tree_walk()
print(alberoarray)

'''
tree = RedBlackTree()
keys = [5, 3, 8, 1, 4, 7, 9]
for key in keys:
    tree.insert(key)

in_order_result = tree.in_order_traversal()
print(in_order_result)  # Output: [1, 3, 4, 5, 7, 8, 9]

'''