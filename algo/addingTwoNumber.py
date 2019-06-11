def adding_two_number(arr1, arr2):
    """
    if num1 is 123 then arr1 = [3,2,1]

    :param arr1:
    :param arr2:

    :return:
    """

    if len(arr1) > len(arr2):
        return adding_two_number(arr2, arr1)

    out = []
    extra = 0

    for i, (a1, a2) in enumerate(zip(arr1, arr2)):
        e = a1 + a2 + extra
        out.append(e % 10)
        extra = e // 10

    for i in range(len(arr1), len(arr2)):
        e = arr2[i] + extra
        out.append(e % 10)
        extra = e // 10

    if extra:
        out.append(extra)

    return out


if __name__ == '__main__':
    print(adding_two_number([9, 9, 9], [9, 9, 9]))
