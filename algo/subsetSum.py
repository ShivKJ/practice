def exact_subset_sum(S, t: int):
    '''
    To search for the existence of a subset of s such that
    sum of element of subset is equal to t
    :param S: collection of number
    :param t: subset sum
    :return: True if there exists such a subset
    '''

    L = {0}

    for x in S:
        L |= {y + x for y in L}
        L = {y for y in L if y <= t}

    return max(L) == t


if __name__ == '__main__':
    print(exact_subset_sum([1, 4, 7, 2], 9))