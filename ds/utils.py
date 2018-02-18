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


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insertion(self, key):
        x, y, n = self.root, None, None

        while x is not None:
            if key == x.x:
                n = x
                break
            y, x = x, x.l if key < x.x else x.r

        if n is None:
            n = Node(key)

            if y is None:
                self.root = n
            elif key < y.x:
                y.l = n
            else:
                y.r = n
            n.p = y

            self.size += 1

        return n

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
