class Node:
    def __init__(self, key, parent=None, color='red'):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None
        self.color = color  # Il colore predefinito è rosso


class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = Node(key=None, color='black')  # Nodo nero nullo
        self.root = self.NIL_LEAF

    def insert(self, key):
        new_node = Node(key)  # creo un nuovo nodo senza figli
        new_node.left = self.NIL_LEAF
        new_node.right = self.NIL_LEAF

        y = None  # lo userò per memorizzare temporaneamente ilnodo mentre scendo
        x = self.root  # comincio a cercare dove mettere il nodo

        while x != self.NIL_LEAF:  # finchè non arrivo ad una foglia
            y = x
            if new_node.key < x.key:  # scendo nell'albero
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if y is None:  # se sono sceso su una foglia e non trovo il padre vuol dire che non c'è la radice
            self.root = new_node  # allora vuol dire che il nodo che inserisco è il primo inserito
        elif new_node.key < y.key:  # inserisco a sinistra o a destra dell'ultima foglia
            y.left = new_node
        else:
            y.right = new_node

        if new_node.parent is None:  # se sono radice
            new_node.color = 'black'  # mi coloro di nero
            return

        if new_node.parent.parent is None:  # se sono il primo figlio resto rosso (era il valore di default)
            return

        self._fix_insert(new_node)  # se non sono nè la radice nè il primo figlio chiamo fix insert
##################################### continua a leggere da qui
    def _fix_insert(self, node):
        while node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._left_rotate(node.parent.parent)
            if node == self.root:
                break
        self.root.color = 'black'

    def _left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left != self.NIL_LEAF:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def _right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right != self.NIL_LEAF:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def in_order_traversal(self):
        result = []
        self._in_order_traversal(self.root, result)
        return result

    def _in_order_traversal(self, node, result):
        if node != self.NIL_LEAF:
            self._in_order_traversal(node.left, result)
            result.append(node.key)
            self._in_order_traversal(node.right, result)
