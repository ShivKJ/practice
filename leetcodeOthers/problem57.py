"""
author: Shiv
email: shivkj001@gmail.com
date: 3/28/20

MIT License

Copyright (c) [2018]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

from bisect import bisect_left
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        idx = bisect_left(intervals, newInterval)
        output = intervals[: idx]

        if not output:
            prev = newInterval
            output.append(prev)
        else:
            prev = output[-1]
            if prev[1] >= newInterval[0]:
                prev[1] = max(prev[1], newInterval[1])
            else:
                output.append(newInterval)
                prev = newInterval

        for i in range(idx, len(intervals)):
            curr = intervals[i]

            if prev[1] >= curr[0]:
                prev[1] = max(prev[1], curr[1])
            else:
                prev = curr
                output.append(prev)
        return output


if __name__ == '__main__':
    print(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
