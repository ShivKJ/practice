from numpy import inf, ndarray, zeros


def max_revenue(price: ndarray, n: int = None):
    """
    Optimal structure:
                    r[j] = max(p[i] + r[j-i]),   r[0] = 0
                         1 <= i <= j

                                OR

                    r[j] = max(p[i], max(r[i] + r[j-i]),    r[0] = 0
                        1 <= i <= j

          eg.       r[3] = max(p[1] + r[2], p[2] + r[1], p[3] + r[0])
                         = max(p[1] + r[2], p[2] + r[1], p[3])

    Implementation Notes: Given a rod of length "n" (price.size - 1), cut it in pieces
                          such that generated revenue is maximum.
    Example:
        import numpy as np
        prices = np.array([0, 1, 5, 8, 10, 13, 17, 18, 22, 25, 30])
        print(max_revenue(arr))

    :param price: price of length segment.
    :param n: length of rod to be cut
    :return:
    """

    if n is None:
        n = price.size - 1

    optimal = zeros(n + 1, dtype=price.dtype)

    for l in range(1, n + 1):
        optimal[l] = max(optimal[:l] + price[l:0:-1])

    return optimal[n]


def extended_bottom_up(price: ndarray, n: int = None):
    if n is None:
        n = price.size - 1

    optimal = zeros(n + 1, dtype=price.dtype)
    cuts = zeros(n + 1, dtype=price.dtype)

    for l in range(1, n + 1):
        q = -inf

        for i in range(1, l + 1):
            temp = price[i] + optimal[l - i]

            if q < temp:
                q = temp
                cuts[l] = i

        optimal[l] = q

    return optimal, cuts


def print_rod_cut(s, n):
    print('length of rod cutting: ', end='')

    while n > 0:
        cut_at = s[n]
        n -= cut_at

        if n > 0:
            print(cut_at, end='|')
        else:
            print(cut_at)

    print()
