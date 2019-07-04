from typing import List


def get_parent(a: int, cache: List[int]) -> int:
    p = a
    gp = cache[a]

    while p != gp:
        p, gp = gp, cache[gp]

    return p


def connect(a: int, b: int, cache: List[int]):
    cache[get_parent(b, cache)] = get_parent(a, cache)


def connected(a: int, b: int, cache: List[int]) -> bool:
    return get_parent(a, cache) == get_parent(b, cache)


if __name__ == '__main__':
    cache = list(range(5))

    connect(0, 1, cache)
    connect(1, 2, cache)
    connect(3, 2, cache)
    print(cache)
    print(connected(2, 3, cache))
