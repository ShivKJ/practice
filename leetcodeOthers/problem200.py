from typing import List

from algo.uf import UF


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        uf = UF(m * n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    index = i * n + j

                    if i > 0 and grid[i - 1][j] == '1':
                        uf.union(index, index - n)
                    if j > 0 and grid[i][j - 1] == '1':
                        uf.union(index, index - 1)
        output = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    output.add(uf.find(i * n + j))

        return len(output)
