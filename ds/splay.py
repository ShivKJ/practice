from ds.utils import Node, Tree


class Splay(Tree):
    def __init__(self):
        super().__init__()

    def splay(self, x: Node):
        '''
        Splaying node x: https://en.wikipedia.org/wiki/Splay_tree#Operations
        :param x:
        '''
        while x is not self.root:
            y = x.p

            if y.p is None:
                '''         |                 |
                            y                 x
                           /       ->          \
                          x                     y   
                            
                          |                   |
                          y                   x 
                           \       ->        /
                            x               y
                '''
                (self.rr if x is y.l else self.lr)(y)
            else:
                z = y.p

                if y is z.l:
                    if x is y.l:
                        '''
                                |               |
                                z     ->        x
                               /                 \
                              y                   y
                             /                     \
                            x                       z
                        '''
                        self.rr(z)
                        self.rr(y)
                    else:
                        '''
                                |                    |
                                z                    x
                               /                    / \
                              y           ->       y   z
                               \
                                x
                        '''
                        self.lr(y)
                        self.rr(z)
                else:
                    if x is y.r:
                        self.lr(z)
                        self.lr(y)
                    else:
                        self.rr(y)
                        self.lr(z)

    def insert(self, key):
        self.splay(self._insertion(key))

    def delete(self, key):
        n = self.find(key)

        if n is not None:
            p = n.p
            self._deletion(n)

            if p is not None:
                self.splay(p)

    def find(self, key):
        x, y = self.root, None

        while x is not None:
            if x.x == key:
                self.splay(x)
                return x

            y, x = x, x.l if key < x.x else x.r

        if y is not None:  # key not found, splaying parent
            self.splay(y)
