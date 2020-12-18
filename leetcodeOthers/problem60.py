from math import ceil, factorial


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        Note: please see permutation for n = 5, pattern will be found
        :param n: between 1 and 9 (both inclusive)
        :param k: between 1 and n! (both inclusive)
        :return: kth permutation in sorted order
        """
        nums = list(range(1, n + 1))
        output = []

        while n > 0:
            x = factorial(n - 1)
            y = ceil(k / x)

            output.append(nums[y - 1])
            nums.remove(nums[y - 1])

            k = (k % x) or x
            n -= 1

        return ''.join(map(str, output))


if __name__ == '__main__':
    print(Solution().getPermutation(5, 11))
