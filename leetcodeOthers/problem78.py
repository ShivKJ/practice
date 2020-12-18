from typing import List
from collections import deque


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for e in nums:
            for i in range(len(output)):
                copy = list(output[i])
                copy.append(e)
                output.append(copy)

        return output


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
