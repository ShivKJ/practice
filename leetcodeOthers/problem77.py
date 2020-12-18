from typing import List


def combination(k: int, available: List[int]):
    if k > len(available):
        yield from []
    elif k == 0:
        yield from [[]]
    elif k == len(available):
        yield from [available]
    else:
        e = available[-1]
        available = available[:-1]

        for a in combination(k - 1, available):
            a.append(e)
            yield a

        for a in combination(k, available):
            yield a


class Solution:
    def combine(self, n: int, k: int):
        return combination(k, list(range(1, n + 1)))


if __name__ == '__main__':
    for a in enumerate(Solution().combine(10, 7), start=1):
        print(a)
