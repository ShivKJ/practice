class Node:
    __slots__ = 'l', 'r', 'x', 'p', 'h'

    def __init__(self, x=None):
        self.x = x
        self.l = None
        self.r = None
        self.p = None
        self.h = 1

    def __str__(self) -> str:
        return 'x={}'.format(self.x)

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


def find_min(n: Node):
    while n.l is not None:
        n = n.l

    return n


class AVL:
    def __init__(self):
        self.root = None
        self.size = 0

    def find(self, key) -> Node:
        x = self.root

        while x is not None:
            if x.x == key:
                return x
            x = x.l if key < x.x else x.r

    def contains(self, key):
        return self.find(key) is not None

    def insert(self, key):
        self._insert(Node(key))

    def _insert(self, n: Node):
        child, parent = self.root, None

        while child is not None:
            parent, child = child, child.l if n.x <= child.x else child.r

        if parent is None:
            self.root = n
        elif n.x <= parent.x:
            parent.l = n
        else:
            parent.r = n

        n.p = parent

        self.size += 1
        self.balance(n)

    def balance(self, x: Node):
        while x.p is not None and x.p.p is not None:
            x.update_height()
            y, z = x.p, x.p.p

            y.update_height()
            z.update_height()

            if not z.balanced:
                if y is z.l:
                    if x is y.r:
                        self.left_rotation(y)
                        y.update_height()
                        x.update_height()

                    self.right_rotation(z)
                else:
                    if x is y.l:
                        self.right_rotation(y)
                        y.update_height()
                        x.update_height()

                    self.left_rotation(z)

                z.update_height()
                break  # balanced globally

            x = x.p

    def delete(self, key):
        z = self.find(key)

        if z is not None:
            self._delete(z)

    def _delete(self, z: Node):
        if z.l is None:
            balancing_node = z.p
            self.transplant(z, z.r)
        elif z.r is None:
            balancing_node = z.p
            self.transplant(z, z.l)
        else:
            y = find_min(z.r)

            if y.p is not z:
                balancing_node = y.p
                self.transplant(y, y.r)
                y.r = z.r
                z.r.p = y

            else:
                balancing_node = y  # as y will be taking z's place

            self.transplant(z, y)
            y.l = z.l
            z.l.p = y

        self.size -= 1

        if balancing_node is not None:  # will be None only when root is removed
            self.delete_bal(balancing_node)

    def delete_bal(self, z: Node):
        while z is not None:
            z.update_height()
            z_h_diff = z.height_diff

            if abs(z_h_diff) > 1:
                if z_h_diff > 0:
                    y = z.l
                    y_h_diff = y.height_diff

                    if y_h_diff < 0:
                        self.left_rotation(y)
                        y.update_height()
                        y.p.update_height()

                    self.right_rotation(z)
                else:
                    y = z.r
                    y_h_diff = y.height_diff

                    if y_h_diff > 0:
                        self.right_rotation(y)
                        y.update_height()
                        y.p.update_height()

                    self.left_rotation(z)

                z.update_height()

            z = z.p

    def right_rotation(self, y: Node):
        x = y.l

        '''
                    |                               |
                    y                               x
                   / \           R(y)              / \
                  x   G        ------>            A   y    
                 / \                                 / \
                A   B                               B   G
        '''
        y.l = x.r

        if x.r is not None:
            x.r.p = y

        x.p = y.p

        if y.p is None:
            self.root = x
        elif y is y.p.l:
            y.p.l = x
        else:
            y.p.r = x

        x.r = y
        y.p = x

    def left_rotation(self, x: Node):
        y = x.r
        x.r = y.l
        '''
                    |                               |
                    x                               y
                   / \           L(x)              / \
                  A   y        -------->          x   G
                     / \                         / \
                    B   G                       A   B
        '''

        if y.l is not None:
            y.l.p = x

        y.p = x.p

        if x.p is None:
            self.root = y
        elif x is x.p.l:
            x.p.l = y
        else:
            x.p.r = y

        y.l = x
        x.p = y

    def transplant(self, u: Node, v: Node):
        if u.p is None:
            self.root = v
        elif u.p.l is u:
            u.p.l = v
        else:
            u.p.r = v

        if v is not None:
            v.p = u.p
