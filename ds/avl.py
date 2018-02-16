class Node:
    __slots__ = 'l', 'r', 'x', 'p', 'h'

    def __init__(self, x=None):
        self.x = x
        self.l = None
        self.r = None
        self.p = None
        self.h = 1

    def __str__(self):
        return 'x={}'.format(self.x)


def get_height(n: Node):
    l_h = 0 if n.l is None else n.l.h
    r_h = 0 if n.r is None else n.r.h

    return 1 + max(l_h, r_h)


def get_diff(n: Node):
    l_h = 0 if n.l is None else n.l.h
    r_h = 0 if n.r is None else n.r.h

    return l_h - r_h


class AVL:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, n: Node):
        c, p = self.root, None

        while c is not None:
            p, c = c, c.l if n.x <= c.x else c.r

        if p is None:
            self.root = n
        elif n.x <= p.x:
            p.l = n
        else:
            p.r = n

        n.p = p

        self.size += 1
        self.balance(n)

    def balance(self, x: Node):
        while x.p is not None and x.p.p is not None:
            x.h = get_height(x)
            p, gp = x.p, x.p.p

            p.h = max(1 + x.h, get_height(p))
            gp.h = max(1 + p.h, get_height(gp))

            if abs(get_diff(gp)) > 1:
                if p is gp.l:
                    if x is p.r:
                        self.left_rotation(p)
                        p.h -= 1
                        x.h += 1

                    self.right_rotation(gp)
                else:
                    if x is p.l:
                        self.right_rotation(p)
                        p.h -= 1
                        x.h += 1

                    self.left_rotation(gp)
                gp.h -= 2

                break

            x = x.p

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


if __name__ == '__main__':
    import random

    random.seed(0)

    data = [Node(random.randint(1, 10)) for _ in range(10)]
    avl = AVL()

    for x in data:
        avl.insert(x)

    print(avl.root)
    print(avl.size)
    print(avl.root.h)
