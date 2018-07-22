from ds.tree import Node, Tree, find_min


class AVLNode(Node):
    __slots__ = 'h'

    def __init__(self, x=None):
        super().__init__(x)
        self.h = 1

    def update_height(self):
        self.h = 1 + max(self._child_heights())

    def _child_heights(self) -> tuple:
        l_h = 0 if self.l is None else self.l.h
        r_h = 0 if self.r is None else self.r.h

        return l_h, r_h

    @property
    def height_diff(self) -> int:
        l, r = self._child_heights()

        return l - r

    @property
    def balanced(self) -> bool:
        return abs(self.height_diff) <= 1


class AVL(Tree):
    def __init__(self):
        super().__init__()

    def node_creator(self, key):
        return AVLNode(key)

    def insert(self, key):
        size = self.size

        n = self._insertion(key)

        if size != self.size:
            self._insert_balance(n)

    def _insert_balance(self, x: AVLNode):
        while x.p is not None and x.p.p is not None:
            x.update_height()
            x.p.update_height()
            x.p.p.update_height()

            if not x.p.p.balanced:
                self._balance(x)
                break  # balanced globally

            x = x.p

    def _balance(self, x: AVLNode):
        y, z = x.p, x.p.p

        if y is z.l:
            if x is y.r:
                self.lr(y)
                y.update_height()
                x.update_height()

            self.rr(z)
        else:
            if x is y.l:
                self.rr(y)
                y.update_height()
                x.update_height()

            self.lr(z)

        z.update_height()

    def delete(self, key):
        z = self.find(key)

        if z is not None:
            self._delete(z)

    def _delete(self, z: AVLNode):
        if z.l is None:
            balancing_node = z.p
        elif z.r is None:
            balancing_node = z.p
        else:
            y = find_min(z.r)
            balancing_node = y.p if y.p is not z else y

        self._deletion(z)

        if balancing_node is not None:  # will be None only when root is removed
            self._delete_balance(balancing_node)

    def _delete_balance(self, z: AVLNode):
        while z is not None:
            z.update_height()
            zh_diff = z.height_diff

            if abs(zh_diff) > 1:
                if zh_diff > 0:
                    y = z.l
                    self._balance(y.r if y.height_diff < 0 else y.l)
                else:
                    y = z.r
                    self._balance(y.l if y.height_diff > 0 else y.r)

                z.update_height()

            z = z.p


if __name__ == '__main__':
    tree = AVL()
    for e in range(1000):
        tree.insert(e)

    for i in range(1000):
        tree.delete(i)
