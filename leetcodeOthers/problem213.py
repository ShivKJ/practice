from functools import lru_cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        if n < 4:
            return max(nums)

        @lru_cache
        def process_linear(index, base=0):
            if index < base:
                return 0
            if index == base:
                return nums[base]

            return max(process_linear(index - 1, base=base), nums[index] + process_linear(index - 2, base=base))

        return max(
            process_linear(n - 2),  # not considering the last one
            nums[-1] + process_linear(n - 3, base=1)  # considering the last one
        )


if __name__ == '__main__':
    print(Solution().rob([200, 3, 140, 20, 10]))
