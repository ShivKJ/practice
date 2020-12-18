from typing import List


def permutation(index: int, values: List[int]):
    """
    creating recursive function to get all the permutation
    of elements from values
    Example:
    A) if values = [1, 2, 3] then output
        1) [1, 2, 3]
        2) [2, 1, 3]
        3) [2, 3, 1]
        4) [1, 3, 2]
        5) [3, 1, 2]
        6) [3, 2, 1]
    B) if values = [1], the output
        1) [1]
    number of elements in output = n! where 0! = 1
                                 = n * (n-1)!
    :param index:
    :param values:
    """
    n = len(values)
    v = values[index]

    if index == n - 1:
        yield from [[v]]  # only on element in output
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
