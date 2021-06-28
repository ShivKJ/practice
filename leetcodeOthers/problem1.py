"""
author: Shiv, [please add your name if you update the script]
email: shivkj001@gmail.com
date: 28-06-2021
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index = {}
        for j, v in enumerate(nums):
            rest = target - v
            i = value_index.get(rest)

            if i is not None:
                return [i, j]

            value_index[v] = j

        raise ValueError()
