from abc import abstractmethod
from functools import total_ordering


@total_ordering
class Node:
    __slots__ = 'l', 'r', 'x', 'p'

    def __init__(self, x=None):
        self.x = x
        self.l = None
        self.r = None
        self.p = None

    def __str__(self) -> str:
        return 'x={}'.format(self.x)

    def __le__(self, other):
        return self.x <= other.x

    def __gt__(self, other):
        return self.x > other.x


def find_min(n: Node, NIL=None):
    while n.l is not NIL:
        n = n.l

    return n


def find_max(n: Node, NIL=None):
    while n.r is not NIL:
        n = n.r

    return n


def successor(n: Node, NIL=None):
    if n.r is not NIL:
        return find_min(n.r, NIL)

    y = n.p

    while y is not NIL and n is y.r:
        n, y = y, y.p

    return y


def predecessor(n: Node, NIL=None):
    if n.l is not NIL:
        return find_max(n.l, NIL)

    y = n.p

    while y is not NIL and n is y.l:
        n, y = y, y.p

    return y


def pre_order(n: Node, NIL=None):
    if n.l is not NIL:
        yield from pre_order(n.l)

    yield n.x

    if n.r is not NIL:
        yield from pre_order(n.r)


class Tree:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def node_creator(self, key):
        return Node(key)

    @abstractmethod
    def insert(self, key):
        pass

    @abstractmethod
    def delete(self, key):
        pass

    def find(self, key, NIL=None):
        x = self.root

        while x is not NIL:
            if x.x == key:
                return x

            x = x.l if key < x.x else x.r

        return NIL

    def _insertion(self, key, NIL=None):
        x, y = self.root, NIL

        while x is not NIL:
            if key == x.x:
                return x

            y, x = x, x.l if key < x.x else x.r

        n = self.node_creator(key)
        n.l = n.r = n.p = NIL

        if y is NIL:
            self.root = n
        elif key < y.x:
            y.l = n
        else:
            y.r = n

        n.p = y
        self.size += 1

        return n

    def _deletion(self, z: Node, NIL=None):

        if z.l is NIL:
            self.transplant(z, z.r)
        elif z.r is NIL:
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

    def rr(self, y: Node, NIL=None):
        '''
        Right rotation with respect to y
        :param y:
        '''

        '''
                    |                               |
                    y                               x
                   / \           R(y)              / \
                  x   G        ------>            A   y    
                 / \                                 / \
                A   B                               B   G
        '''
        x = y.l
        y.l = x.r

        if x.r is not NIL:
            x.r.p = y

        x.p = y.p

        if y.p is NIL:
            self.root = x
        elif y is y.p.l:
            y.p.l = x
        else:
            y.p.r = x

        x.r = y
        y.p = x

    def lr(self, x: Node, NIL=None):
        '''
        left rotation with respect to x
        :param x:
        '''
        '''
                    |                               |
                    x                               y
                   / \           L(x)              / \
                  A   y        -------->          x   G
                     / \                         / \
                    B   G                       A   B
        '''
        y = x.r
        x.r = y.l

        if y.l is not NIL:
            y.l.p = x

        y.p = x.p

        if x.p is NIL:
            self.root = y
        elif x is x.p.l:
            x.p.l = y
        else:
            x.p.r = y

        y.l = x
        x.p = y

    def transplant(self, u: Node, v: Node, NIL=None):
        if u.p is NIL:
            self.root = v
        elif u.p.l is u:
            u.p.l = v
        else:
            u.p.r = v

        if v is not NIL:
            v.p = u.p

    def __bool__(self):
        return bool(self.size)

    def __len__(self):
        return self.size

    def __iter__(self):
        return pre_order(self.root) if self else iter(())

    def __contains__(self, item):
        # TODO: check if None can be replaced with NIL, passed as parameter
        return self.find(item) is not None

    def __delitem__(self, key):
        self.delete(key)

    def __add__(self, other):
        self.insert(other)

        return self
