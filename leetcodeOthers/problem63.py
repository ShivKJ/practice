from itertools import accumulate
from operator import mul
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        cache = list(accumulate((1 - e for e in obstacleGrid[0]), mul))

        for x in range(1, m):
            if obstacleGrid[x][0] == 1:
                cache[0] = 0

            for y in range(1, n):
                cache[y] = (
                        (1 - obstacleGrid[x][y]) *
                        (
                                cache[y] * (1 - obstacleGrid[x - 1][y])  # paths from up-side
                                +
                                cache[y - 1] * (1 - obstacleGrid[x][y - 1])  # paths from left side
                        )
                )

        return cache[-1]
