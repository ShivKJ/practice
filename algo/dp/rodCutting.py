from numpy import array, inf, ndarray, zeros
from ortools.linear_solver.pywraplp import Solver


def max_revenue_lp(price: ndarray, n: int = None):
    price = price[1:]

    if n is None:
        n = price.size

    solver = Solver('rod-cutting', Solver.SCIP_MIXED_INTEGER_PROGRAMMING)

    x = [solver.IntVar(0, n // i, str(i)) for i in range(1, n + 1)]

    objective = solver.Sum([x_i * p for x_i, p in zip(x, price)])

    solver.Maximize(objective)
    solver.Add(solver.Sum([i * x_i for i, x_i in enumerate(x, 1)]) <= n)

    solver.Solve()

    return [int(x_i.SolutionValue()) for x_i in x]


def max_profit(profit: ndarray, n: int = None):
    """
    Optimal structure:
                    r[j] = max(p[i] + r[j-i]),   r[0] = 0
                         1 <= i <= j

                                OR

                    r[j] = max(p[i], max(r[i] + r[j-i]),    r[0] = 0
                        1 <= i <= j

          eg.       r[3] = max(p[1] + r[2], p[2] + r[1], p[3] + r[0])
                         = max(p[1] + r[2], p[2] + r[1], p[3])

    Implementation Notes: Given a rod of length "n" (profit.size - 1), cut it in pieces
                          such that generated profit is maximum.
    Example:
        import numpy as np
        prices = np.array([0, 1, 5, 8, 10, 13, 17, 18, 22, 25, 30])
        print(max_profit(arr))

    :param profit: ith index represent profit of (i+1) length
    :param n: length of rod to be cut
    :return: total optimal profit
    """

    if n is None:
        n = profit.size - 1

    optimal = zeros(n + 1, dtype=profit.dtype)

    for l in range(1, n + 1):
        optimal[l] = (
                optimal[:l] +  # 0,  1,    2,    3,..., l-1 (optimal profit if rod is cut for length 1 to l-1)
                profit[l:0:-1]  # l, l-1, l-2, l-3,...., 1   (profit of length of sizes 1 to l in reverse order)
        ).max()

    return optimal[n]


def extended_bottom_up(profit: ndarray, n: int = None):
    """
    :param profit:
    :param n: 
    :return: 
    """
    if n is None:
        n = profit.size - 1

    optimal = zeros(n + 1, dtype=profit.dtype)  # value at ith index will be optimal profit if rod is but for ith length
    cuts = zeros(n + 1, dtype=profit.dtype)  # value at ith index is size of one part of rod that is cut

    for l in range(1, n + 1):
        q = -inf

        for i in range(1, l + 1):
            temp = profit[i] + optimal[l - i]

            if q < temp:
                q = temp
                cuts[l] = i

        optimal[l] = q

    return optimal, cuts


def print_rod_cut(s, n):
    print('length of rod cutting: ', end='')

    n -= 1

    while n > 0:
        cut_at = s[n]
        n -= cut_at

        if n > 0:
            print(cut_at, end='|')
        else:
            print(cut_at)

    print()


if __name__ == '__main__':
    prices = array([0, 1, 5, 8, 9, 10, 17, 17, 20])
    print(max_revenue_lp(prices))
    print(sum(i * p for p, i in zip(prices[1:], max_revenue_lp(prices))))
    print(max_profit(prices))

    print_rod_cut(extended_bottom_up(prices)[1], len(prices))
