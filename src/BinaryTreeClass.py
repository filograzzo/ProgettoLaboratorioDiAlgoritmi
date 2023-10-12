class TreeNode:
    def __init__(self, key):
        self.key = key
        self.p = None  # puntatore al padre
        self.right = None  # puntatore al figlio destro
        self.left = None  # puntatore al figlio sinistro


class BinaryTree:
    def __init__(self):
        self.root = None

# TODO: metodi per inserìmento
    @staticmethod
    def recursive_insert(current, key):
        if current is None:

    def insert(self, key):
        recursive_insert(self.root, key)

# TODO: metodi per cancellazione
    @staticmethod
    def recursive_delete(current, key):
        if current.key == key:


    def delete(self, key):  # deve ritornare un booleano per dire se ha effettivamente cancellato o non ha trovato il numero da cancellare
        return recursive_delete(self.root, key)

# metodi di ricerca ci mette O(h) con h altezza dell'albero di ricerca
    @staticmethod
    def recursive_search(current, key):
        if current.key == key  or current is None:
            return current  # ritorno il nodo che ha il valore uguale a quello che sto cercando oppure None se sono arrivato lla fine dell'albero senza trovare nulla
        if current.key >= key:
            recursive_search(current.left, key)
        else:
            recursive_search(current.right, key)

    def search(self, key):
        return recursive_search(self.root, key)

# metodi per ricerca di minimo e massimo O(h)
    @staticmethod
    def iterative_maximum(current):
        if current.right is None:
            return current
        iterative_maximum(current.right)

    def find_maximum(self):
        return iterative_maximum(self.root)

    @staticmethod
    def iterative_minimum(current):
        if current.left is None:
            return current
        iterative_minimum(current.left)

    def find_minimum(self):
        return iterative_minimum(self.root)

# metodi per ritornare un array di interi per poi stamparli nel main. Occupa Θ(n) dato che si chima due volte per nodo.
    def tree_walk(self):
        result = []
        recursive_treewalk(self.root)
        return result

    @staticmethod
    def recursive_treewalk(current):
        if current is not None:
            recursive_treewalk(current.left)
            result.append(current.key)
            recursive_treewalk(current.right)
