from typing import List, Tuple

ADJACENT_CELLS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows = len(grid)
        columns = len(grid[0])
        status = [[0] * columns for _ in range(rows)]
        parent_index = [[None] * columns for _ in range(rows)]

        for i in range(rows):
            for j in range(columns):
                if status[i][j] == 0:  # cell has not been visited
                    output = self.dfs(i, j, grid, status, parent_index)

                    if output:
                        return output

        return False

    def dfs(self, i, j, gris: List[List[str]], visited: List[List[int]], parent: List[List[Tuple[int, int]]]):
        visited[i][j] = 1  # making cell active and running DFS on it

        for a, b in self.adjacent_cells(i, j, gris):  # finding all the adjacent grids which have same colors
            if visited[a][b] == 1 and parent[i][j] != (a, b):
                # cycle is formed when adjacent cell is active and that cell should
                # not be parent of current cell (i,j) to make sure that we are just not back-tracing on dfs-path
                return True
            elif visited[a][b] == 0:
                parent[a][b] = (i, j)
                out = self.dfs(a, b, gris, visited, parent)

                if out:
                    return out

        visited[i][j] = 2

        return False

    def adjacent_cells(self, i, j, grids):
        color = grids[i][j]

        for a, b in ADJACENT_CELLS:
            b_j = b + j
            a_i = a + i

            if 0 <= a_i < len(grids) and 0 <= b_j < len(grids[0]) and grids[a_i][b_j] == color:
                yield a_i, b_j
