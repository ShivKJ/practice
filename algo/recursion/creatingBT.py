SENTINAL = '*'


class Node:
    __slots__ = ('d', 'l', 'r')

    def __init__(self, d):
        self.d = d
        self.l = None
        self.r = None

    def __str__(self):
        return str(self.d)


def lc(i):
    return 2 * i + 1


def rc(i):
    return 2 * i + 2


def has_lc(i, data):
    l = lc(i)
    return l < len(data) and data[l] != SENTINAL


def has_rc(i, data):
    r = rc(i)
    return r < len(data) and data[r] != SENTINAL


def create_bt(s: str):
    data = s.split(',')
    print(data)

    root = Node(int(data[0]))
    recursion(root, 0, data)

    return root


def recursion(n: Node, i: int, data):
    if has_lc(i, data):
        left = Node(int(data[lc(i)]))

        n.l = left

        recursion(left, lc(i), data)

    if has_rc(i, data):
        right = Node(int(data[rc(i)]))

        n.r = right

        recursion(right, rc(i), data)


if __name__ == '__main__':
    s = '0,1,2,*,4'
    n = create_bt(s)
    print(n)
    print(n.l, n.l.r, n.l.l)
