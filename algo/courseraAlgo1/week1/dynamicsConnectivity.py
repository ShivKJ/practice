class UnionFind:
    def __init__(self, n: int):
        self._cache = list(range(n))

    def connect(self, a: int, b: int):
        self._cache[self._parent(b)] = self._parent(a)

    def connected(self, a: int, b: int) -> bool:
        return self._parent(a) == self._parent(b)

    def _parent(self, a: int) -> int:
        while a != self._cache[a]:
            self._cache[a] = self._cache[self._cache[a]]
            a = self._cache[a]

        return a


if __name__ == '__main__':
    uf = UnionFind(5)

    uf.connect(0, 1)
    uf.connect(1, 2)
    uf.connect(3, 2)

    print(uf.connected(2, 3))
    print(uf.connected(3, 2))
    print(uf.connected(0, 2))
    print(uf.connected(0, 4))
