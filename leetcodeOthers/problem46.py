from typing import List


def permutation(index, values):
    n = len(values)
    v = values[index]

    if index == n - 1:
        yield from [[v]]
    else:
        for e in permutation(index + 1, values):
            for j in range(index, n):
                yield e[:j - index] + [v] + e[j - index:]


class Solution:
    def permute(self, nums: List[int]):
        return permutation(0, nums)


if __name__ == '__main__':
    for e in Solution().permute([1, 2, 3]):
        print(e)
