from math import inf
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]):
        """
        at any point in traversal, health should be positive (even
        at starting point 0,0)
        :param dungeon:
        :return:
        """
        m, n = len(dungeon), len(dungeon[0])

        cache = [[None] * n for _ in range(m)]

        def health_to_reach_final_location(i, j):
            """
            :param i:
            :param j:
            :return: minimum health required to reach from
                     (i, j) -> (m-1, n-1)
            """
            if i >= m or j >= n:
                # edge case
                return inf

            if cache[i][j] is not None:
                return cache[i][j]

            cache[i][j] = max(
                min(
                    health_to_reach_final_location(i + 1, j),
                    health_to_reach_final_location(i, j + 1)
                ) - dungeon[i][j],
                1
            )

            return cache[i][j]

        cache[m - 1][n - 1] = max(1 - dungeon[m - 1][n - 1], 1)

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                health_to_reach_final_location(i, j)

        return cache[0][0]  # equivalently health_to_reach_final_location(0, 0)


if __name__ == '__main__':
    print(Solution().calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
    # print(Solution().calculateMinimumHP([[1]]))
