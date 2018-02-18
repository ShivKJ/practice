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


def find_min(n: Node):
    while n.l is not None:
        n = n.l

    return n


def pre_order(n: Node):
    if n.l is not None:
        yield from pre_order(n.l)

    yield n.x

    if n.r is not None:
        yield from pre_order(n.r)


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def node_creator(self, key):
        return Node(key)

    @abstractmethod
    def insert(self, key):
        pass

    @abstractmethod
    def delete(self, key):
        pass

    def find(self, key):
        x = self.root

        while x is not None:
            if x.x == key:
                return x

            x = x.l if key <= x.x else x.r

    def _insertion(self, key):
        x, y = self.root, None

        while x is not None:
            if key == x.x:
                return x

            y, x = x, x.l if key < x.x else x.r

        n = self.node_creator(key)

        if y is None:
            self.root = n
        elif key < y.x:
            y.l = n
        else:
            y.r = n

        n.p = y
        self.size += 1

        return n

    def _deletion(self, z: Node):

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

    def rr(self, y: Node):
        '''
        Right rotation with respect to y
        :param y:
        '''

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

    def lr(self, x: Node):
        '''
        left rotation with respect to x
        :param x:
        '''
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

    def __bool__(self):
        return self.root is not None

    def __len__(self):
        return self.size

    def __iter__(self):
        return pre_order(self.root) if self else iter(())

    def __contains__(self, item):
        return self.find(item) is not None

    def __delitem__(self, key):
        self.delete(key)

    def __add__(self, other):
        self.insert(other)

        return self
