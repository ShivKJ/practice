from typing import List, Set


def exact_subset_sum(array: List[float], t: float):
    """
    To search for the existence of a subset of s such that
    sum of element of subset is equal to t

    Example:
        exact_subset_sum([1, 4, 7, 2], 9) -> True

    :param array: collection of number
    :param t: subset sum
    :return: True if there exists such a subset
    """

    L = {0}  # this will be a set, element of which is a sum of some subset of array
    # if array = [1,2,3] then L =
    # {
    #   0,
    #   sum({1}),
    #
    #   sum({2}),
    #   sum({1, 2}),
    #
    #   sum({3}),
    #   sum({1,2}),
    #   sum({2,3}),
    #   sum({1,2,3})
    #  }

    for e in array:
        L |= {y + e for y in L if y + e <= t}
    return max(L) == t


def exact_subset_sum_approach2(array: Set[float], t: float):
    """
    :param array:
    :param t:
    :return:
    """
    if t == 0:
        return True
    elif not array or t < 0:
        return False

    x = next(iter(array))
    array = array - {x}

    return (
            exact_subset_sum_approach2(array, t - x)  # either this element x is part of the sum
            or
            exact_subset_sum_approach2(array, t)  # or "x" is not part of the sum
    )


if __name__ == '__main__':
    print(exact_subset_sum([1, 4, 7, 2], 9))
    print(exact_subset_sum_approach2({1, 4, 7, 2}, 9))
