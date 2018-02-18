from ds.utils import Node, Tree


class Splay(Tree):
    def __init__(self):
        super().__init__()

    def splay(self, x: Node):
        while x is not self.root:
            y = x.p

            if x is y.l:
                self.right_rotation(y)
            else:
                self.left_rotation(y)

    def insert(self, key):
        self.splay(self.insertion(key))
