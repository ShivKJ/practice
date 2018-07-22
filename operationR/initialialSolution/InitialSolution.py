from pprint import pprint

import numpy as np
from numpy import ndarray

from operationR.initialialSolution.vogel import Vogel


def northwest(supply: ndarray, demand: ndarray) -> ndarray:
    """
    Northwest method for getting initial solution.

        0   0   0   0 | 2
                      |
        0   0   0   0 | 3
                      |
        0   0   0   0 | 5
        --------------
        1   5   3   1

        Starting from north-west corner of matrix, if demand is less than fulfilling it and renaming resource
        is allocated to other demand location. If supply is less then fulfilling it with demand and then
        moving to other supply location.


        1   1   0   0 | 2
                      |
        0   3   0   0 | 3
                      |
        0   1   3   1 | 5
        --------------
        1   5   3   1


    :param supply:
    :param demand:
    :return:
    """

    supply = supply.copy()
    demand = demand.copy()

    ROWS, COLUMNS = len(demand), len(supply)

    solution = np.zeros((ROWS, COLUMNS))
    row, col = 0, 0

    while row < ROWS and col < COLUMNS:
        if demand[row] < supply[col]:
            solution[row][col] = demand[row]
            supply[col] -= demand[row]
            row += 1
        else:
            solution[row][col] = supply[col]
            demand[row] -= supply[col]
            col += 1

    return solution


def vogel(C: ndarray, supply: ndarray, demand: ndarray) -> ndarray:
    return Vogel(C, supply, demand).solve()


if __name__ == '__main__':
    pprint(northwest(np.array([1, 5, 3, 1]), np.array([2, 3, 5])))
