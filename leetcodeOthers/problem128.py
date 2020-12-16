from typing import List, Set


def process(e: int, s: Set[int]) -> int:
    out = 1
    t = e
    while s:
        t += 1
        if t in s:
            out += 1
        else:
            break
    t = e
    while s:
        t -= 1
        if t in s:
            out += 1
        else:
            break

    return out


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        result = 0
        for e in nums:
            if e in s:
                result = max(result, process(e, s))

        return result


if __name__ == '__main__':
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
