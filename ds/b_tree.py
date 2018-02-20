from ds.utils import Tree


class BTree(Tree):

    def __init__(self):
        super().__init__()

    def insert(self, key):
        self._insertion(key)

    def delete(self, key):
        n = self.find(key)

        if n is not None:
            self._deletion(n)
