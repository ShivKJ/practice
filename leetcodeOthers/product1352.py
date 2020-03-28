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


class ProductOfNumbers:

    def __init__(self):
        self.mult = []
        self.last_zero_index = -1

    def add(self, num: int) -> None:
        x = num

        if x == 0:
            x = 1
            self.last_zero_index = len(self.mult)

        if self.mult:
            x *= self.mult[-1]

        self.mult.append(x)

    def getProduct(self, k: int) -> int:
        if self.last_zero_index > -1 and k >= len(self.mult) - self.last_zero_index:
            return 0

        a = self.mult[-1]

        if k == len(self.mult):
            return a

        b = self.mult[-(k + 1)]

        return int(a / b)


if __name__ == '__main__':
    p = ProductOfNumbers()
    p.add(1)
    # p.add(0)
    p.add(2)
    p.add(3)
    # p.add(4)
    # p.add(5)

    print(p.getProduct(3))
