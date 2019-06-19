from math import inf


def mean(a, b):
    return (a + b) / 2


def median(arr1, arr2):
    """
    reference : https://www.youtube.com/watch?v=LPFhl65R7ww
    :param arr1:
    :param arr2:
    :return:
    """
    m, n = len(arr1), len(arr2)

    if m > n:
        return median(arr2, arr1)

    odd = (m + n) % 2

    if m == 0:
        return arr2[(n + 1) // 2 - 1] if odd else mean(arr2[n // 2 - 1], arr2[n // 2])

    start, end = 0, m

    while True:
        p_x = (start + end) // 2
        p_y = (m + n + 1) // 2 - p_x

        l1 = -inf if p_x == 0 else arr1[p_x - 1]
        l2 = inf if p_x == m else arr1[p_x]

        r1 = arr2[p_y - 1] if p_y != 0 else -inf
        r2 = arr2[p_y] if p_y != n else inf

        if l1 <= r2 and r1 <= l2:
            return max(l1, r1) if odd else mean(max(l1, r1), min(l2, r2))
        elif l2 < r1:
            start = p_x + 1
        else:
            end = p_x - 1


if __name__ == '__main__':
    print(median([1, 2, 3], [4, 5, 99]))
