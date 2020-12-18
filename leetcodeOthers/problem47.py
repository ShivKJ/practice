from collections import Counter
from typing import List


def process(counter, cache, values, index):
    if len(cache) == index:
        yield cache
    else:
        for i in range(len(values)):
            if counter[i]:
                cache[index] = values[i]
                counter[i] -= 1
                yield from process(counter, cache, values, index + 1)
                counter[i] += 1


class Solution:
    def permuteUnique(self, nums: List[int]):
        n = len(nums)

        counter = Counter(nums)
        nums = sorted(counter.keys())
        return process([counter[e] for e in nums], [None] * n, nums, 0)
