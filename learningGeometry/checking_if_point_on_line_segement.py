"""
author: Shiv
email: shivkj001@gmail.com
date: 3/25/20

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

import numpy as np
from numpy import cross, ndarray
from numpy.linalg import norm


def is_on(a: ndarray, b: ndarray, c: ndarray, tol=10e-8) -> bool:
    """

    :param a:
    :param b:
    :param c:
    :param tol:
    :return: True if c lies on line segment ab
    """
    return (
            norm(cross(a - b, b - c)) <= tol

            and

            (
                    (np.all(a <= c) and np.all(c <= b))
                    or
                    (np.all(b <= c) and np.all(c <= a))
            )
    )
