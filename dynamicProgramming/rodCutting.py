import numpy as np
from numpy import ndarray

'''

Implementation Notes: Given a rod of length "n", cut it in pieces such that
                      generated revenue is maximum.
                      In input length of rod and it's corresponding price is
                      given.
'''


def max_revenue(p: ndarray, n: int):
    '''
    Optimal structure:
                    r[j] = max(p[i] + r[n-i]),   r[0] = 0
                         1 <= i <= j

                                OR

                    r[j] = max(p[i], max(r[i] + r[n-i]),    r[0] = 0
                        1 <= i <= j

          eg.       r[3] = max(p[1] + r[2], p[2] + r[1], p[3] + r[0])
                         = max(p[1] + r[2], p[2] + r[1], p[3])

    :param p: price of length segment.
    :param n: length of rod to be cut
    :return:
    '''

    r = np.zeros(n + 1, dtype=p.dtype)

    for i in range(1, n + 1):
        r[i] = max(r[:i] + p[:i][::-1])

    return r[n]


def extended_bottom_up(price: ndarray, length: int):
    optimal = np.zeros(length + 1, dtype=price.dtype)
    cut = np.zeros(length + 1, dtype=price.dtype)

    for j in range(1, length + 1):
        q = -np.inf
        for i in range(1, j + 1):
            if q < price[i - 1] + optimal[j - i]:
                q = price[i - 1] + optimal[j - i]
                cut[j] = i
        optimal[j] = q

    return optimal, cut


def print_rod_cut(s, n):
    print('length of rod cutting: ', end='')

    while n > 0:
        print(s[n], end=' ')
        n -= s[n]

    print()

