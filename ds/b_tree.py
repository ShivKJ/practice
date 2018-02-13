class Node:
    __slots__ = 'l', 'r', 'x', 'p'

    def __init__(self, x):
        self.x = x
        self.l = None
        self.r = None
        self.p = None

    def __str__(self):
        return 'x={}'.format(self.x)


def find_min(n: Node):
    while n.l is not None:
        n = n.l

    return n


def find_max(n):
    while n.r is not None:
        n = n.r
    return n


def successor(n):
    if n.r is not None:
        return find_min(n.r)

    y = n.p

    while y is not None and n is y.r:
        n, y = y, y.p

    return y


def predecessor(n):
    if n.l is not None:
        return find_max(n.l)
    y = n.p

    while y is not None and n is y.l:
        n, y = y, y.p

    return y


class BTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def search(self, key):
        n = self.root

        while n is not None:
            if n.x == key:
                return n

            n = n.l if key < n.x else n.r

        return None

    def insert_key(self, key):
        z = BTree.createNode(key)
        y = None
        x = self.root

        while x is not None:
            y, x = x, x.l if key < x.x else x.r

        z.p = y

        if y is None:
            self.root = z
        elif key < y.x:
            y.l = z
        else:
            y.r = z
        self.size += 1

    def transplant(self, u, v):
        if u.p is None:
            self.root = v
        elif u.p.l is u:
            u.p.l = v
        else:
            u.p.r = v

        if v is not None:
            v.p = u.p

    def delete_key(self, key):
        z = self.search(key)

        if z is not None:
            self.delete(z)

    def contains(self, key):
        return self.search(key) is not None

    def delete(self, z):
        if z.l is None:
            self.transplant(z, z.r)
        elif z.r is None:
            self.transplant(z, z.l)
        else:
            y = find_min(z.r)

            if y.p is not z:
                self.transplant(y, y.r)
                y.r = z.r
                z.r.p = y
            self.transplant(z, y)

            y.l = z.l
            z.l.p = y

        self.size -= 1

    @staticmethod
    def createNode(key):
        return Node(key)

    def __len__(self):
        return self.size

    def __bool__(self):
        return self.root is not None
