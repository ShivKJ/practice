def permutation(index: int, string: str):
    """
    creating recursive function to get all the permutation
    of elements from "string"

    Example:
    A) if string = ABC then output
        1) ABC
        2) ACB
        3) BAC
        4) CAB
        5) BCA
        6) CBA
    B) if string = A, the output
        1) A
    number of elements in output = n! where 0! = 1
                                 = n * (n-1)!
    :param index:
    :param string:
    :return generator of permutation of string
    """
    n = len(string)
    v = string[index]

    if index == n - 1:
        yield from [v]  # only on element in output
    else:
        for j in range(index, n):
            for e in permutation(index + 1, string):
                yield e[:j - index] + v + e[j - index:]


def generate(string: str):
    """
    :param string:
    :return: generator for permutation of given string
    """
    return permutation(0, string)


if __name__ == '__main__':
    for i, e in enumerate(sorted(generate('12345')), start=1):
        print(f'{i:3} {e}')
