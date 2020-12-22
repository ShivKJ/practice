"""
author: Shiv, [please add your name if you update the script]
email: shivkrishna.jaiswal@delhivery.com
date: 22/12/20
"""
from math import comb


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)
