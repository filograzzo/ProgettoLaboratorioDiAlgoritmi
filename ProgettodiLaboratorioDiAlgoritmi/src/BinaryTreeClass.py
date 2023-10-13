class TreeNode:
    def __init__(self, key):
        if key is None:
            raise ValueError("La key di un nodo non può essere nulla")
        self.key = key
        self.p = None  # puntatore al padre
        self.right = None  # puntatore al figlio destro
        self.left = None  # puntatore al figlio sinistro


class BinaryTree:
    def __init__(self):
        self.root = None
        self.result = []

    # metodi per inserìmento O(h)
    def insert(self, key):
        y = None
        x = self.root
        while x is not None:
            y = x
            if x.key == key:  # se il numero è già inserito ritorno senza fare nulla
                return
            if key < x.key:
                x = x.left
            else:
                x = x.right
        z = TreeNode(key)
        z.p = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    # metodi per cancellazione O(h)
    def delete(self, key):  # deve ritornare un booleano per dire se ha effettivamente cancellato o non ha trovato il
        # numero da cancellare
        z = self.search(key)
        if z is None:  # se il valore cercato non è presente nell'albero
            return False  # ritorno falso: il valore non è presente
        if z.left is None:
            self.delete_cycle(z, z.right)  # se non ho figli chiamo entrambi ma la seconda volta non fa nulla
        elif z.right is None:
            self.delete_cycle(z, z.left)
        else:  # se devo cancellare un nodo con entrambi i figli
            y = self.find_successor(z)  # prendo il successore in una variabile temporanea
            if y.p is not z:  # se z non è il padre
                self.delete_cycle(y, y.right)  # il figlio destro di y diventa figlio dell'ex padre di y
                y.right = z.right  # il nodo che ho appena preso avrà come figlio dx il figlio dx del nodo che elimino
                y.right.p = y  # e il rispettivo figlio avrà ora y come padre. Manca il sottoalbero sx
                y.left = z.left  # il nodo che ho appena preso avrà come figlio sx il figlio sx del nodo che elimino
                y.left.p = y  # e il rispettivo figlio avrà ora y come padre.
                return True
            self.delete_cycle(z, y)  # se z è il padre
            y.left = z.left  # il nodo che ho appena preso avrà come figlio sx il figlio sx del nodo che elimino
            y.left.p = y  # e il rispettivo figlio avrà ora y come padre.
        return True

    def delete_cycle(self, x, y):
        if x is not None and x.p is None:  # se sono la radice
            self.root = y  # il figlio diventa radice
        elif x is x.p.left:  # se sono il figlio sinistro
            x.p.left = y  # colui che era figlio diventa il nuovo figlio del padre
        elif x is x.p.right:
            x.p.right = y
        if y is not None:  # se il figlio esiste
            y.p = x.p  # suo padre diventa quello che era suo "nonno"

    # metodo per trovare il successore (serve poi nel metodo di cancellazione)
    def find_successor(self, node):
        if node.right is not None:
            return self.find_minimum(node.right)
        y = node.p
        while y is not None and node is y.right:
            node = y
            y = y.p
        return y

    # metodi di ricerca ci mette O(h) con h altezza dell'albero di ricerca
    def recursive_search(self, current, key):
        if current.key == key or current is None:
            return current  # ritorno il nodo che ha il valore uguale a quello che sto cercando oppure None se sono
            # arrivato lla fine dell'albero senza trovare nulla
        if current.key >= key:
            return self.recursive_search(current.left, key)
        else:
            return self.recursive_search(current.right, key)

    def search(self, key):
        return self.recursive_search(self.root, key)

    # metodi per ricerca di minimo e massimo O(h)
    def iterative_maximum(self, current):
        if current.right is None:
            return current
        return self.iterative_maximum(current.right)

    def find_maximum(self, node):
        return self.iterative_maximum(node)

    def iterative_minimum(self, current):
        if current.left is None:
            return current
        return self.iterative_minimum(current.left)

    def find_minimum(self, node):
        return self.iterative_minimum(node)

    # metodi per ritornare un array di interi per poi stamparli. Occupa Θ(n) dato che si chima due volte per nodo.
    def tree_walk(self):
        self.result = []
        self.recursive_treewalk(self.root)
        return self.result

    def recursive_treewalk(self, current):
        if current is not None:
            self.recursive_treewalk(current.left)
            self.result.append(current.key)
            self.recursive_treewalk(current.right)
