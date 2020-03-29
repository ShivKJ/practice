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

from collections import deque
from typing import List


class RLEIterator:
    """
    This problem has run-time issue
    """

    def __init__(self, A: List[int]):
        self.data = deque()

        n = len(A) // 2

        for i in range(n):
            f, e = A[2 * i], A[2 * i + 1]
            self.data.extend((e for _ in range(f)))

    def next(self, n: int) -> int:
        if len(self.data) < n:
            return -1

        out = None

        for _ in range(n):
            out = self.data.popleft()

        return out


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
if __name__ == '__main__':
    rle = RLEIterator([3, 8, 0, 9, 2, 5])
    print(rle.data)
    print(rle.next(2))
    print(rle.next(1))
    print(rle.next(1))
