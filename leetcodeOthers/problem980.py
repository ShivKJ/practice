from typing import List

NEIGHBORS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]
VISITED = -1


def move(x: int, y: int, grid: List[List[int]], zeros) -> int:
    """
    :param x:
    :param y:
    :param grid:
    :param zeros:
    :return: total number of paths from (x,y) to the grid box containing 2 and before
             reaching to that box visiting all the zeros in grid
    """
    grid_value = grid[x][y]
    grid[x][y] = VISITED

    paths = 0

    for dx, dy in NEIGHBORS:
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            value = grid[nx][ny]

            if value == 2 and zeros == 0:  # reached to destination and no zero in grid
                paths += 1
            elif value == 0:
                zeros -= 1
                paths += move(nx, ny, grid, zeros)
                zeros += 1

    # ---------------------------------------------------------------
    grid[x][y] = grid_value

    return paths


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start_x, start_y = None, None
        zeros = 0

        for i, arr in enumerate(grid):
            for j, e in enumerate(arr):
                if e == 1:
                    start_x = i
                    start_y = j
                elif e == 0:
                    zeros += 1

        if start_x is None:
            raise ValueError('start x,y not found')

        return move(start_x, start_y, grid, zeros)


if __name__ == '__main__':
    g = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
    print(Solution().uniquePathsIII(g))
