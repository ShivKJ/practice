from algo.courseraAlgo1.week1.dynamicsConnectivity import UnionFind


def kruskal(n, edge_weight: dict):
    uf = UnionFind(n)
    out = []

    for (u, v), w in sorted(edge_weight.items(), key=lambda x: x[1]):
        if not uf.connected(u, v):
            out.append((u, v))
            uf.connect(u, v)

    return out


if __name__ == '__main__':
    out = kruskal(10, {
        (0, 1): 4,
        (1, 2): 8,
        (2, 3): 7,
        (3, 4): 9,
        (4, 5): 10,
        (5, 6): 2,
        (6, 7): 1,
        (7, 0): 8,
        (7, 1): 11,
        (7, 8): 7,
        (8, 6): 6,
        (8, 2): 2,
        (2, 5): 4,
        (3, 5): 14
    })
    print(sorted(out)   )
