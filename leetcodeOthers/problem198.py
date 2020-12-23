from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)  # all elements in array is non negative
        output = [None] * n

        def get(i):
            if i < 0:
                return 0

            if i < 2:
                return nums[i]

            if output[i] is not None:
                return output[i]

            output[i] = max(get(i - 1), max(get(i - 2), get(i - 3)) + nums[i])

            return output[i]

        best = 0

        for i in range(n):
            best = max(best, get(i))

        return best  # equivalently output[-1]


if __name__ == '__main__':
    print(Solution().rob([2, 1, 1, 2]))
