from typing import Dict


def get_parent(a: int, cache: Dict[int, int]) -> int:
    p = a
    gp = cache[a]

    while p != gp:
        p, gp = gp, cache[gp]

    return p


def connect(a: int, b: int, cache: Dict[int, int]):
    cache[get_parent(b, cache)] = get_parent(a, cache)


def connected(a: int, b: int, cache: Dict[int, int]) -> bool:
    return get_parent(a, cache) == get_parent(b, cache)


if __name__ == '__main__':
    cache = {i: i for i in range(5)}

    connect(0, 1, cache)
    connect(1, 2, cache)
    connect(3, 2, cache)
    print(cache)
    print(connected(2, 3, cache))
