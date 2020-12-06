from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = nums[0]
        tmp_sum = global_max
        for i in range(1, len(nums)):
            e = nums[i]
            tmp_sum = max(tmp_sum + e, e)

            if tmp_sum > global_max:
                global_max = tmp_sum

        return global_max


if __name__ == '__main__':
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
