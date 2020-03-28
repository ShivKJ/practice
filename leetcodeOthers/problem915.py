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

from typing import List


class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        left_list_ending_index = 0

        _max = _next_max = A[0]

        for i, e in enumerate(A):
            if _next_max <= e:
                _next_max = e

            if _max > e:
                left_list_ending_index = i
                _max = _next_max

        return left_list_ending_index + 1


if __name__ == '__main__':
    print(Solution().partitionDisjoint([1, 1, 1, 0, 6, 12]), 4)
    print(Solution().partitionDisjoint([5, 0, 3, 8, 6]), 3)
    print(Solution().partitionDisjoint([24, 11, 49, 80, 63, 8, 61, 22, 73, 85]), 9)
