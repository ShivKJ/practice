from typing import List


def partitioning(arr: List[float], start_index: int, end_index: int):
    """
    between "start_index" and "end_index",
    :param arr:
    :param start_index:
    :param end_index:
    :return:
    """
    pivot_element = arr[end_index]  # in the end, all the elements less than this element will be on left of this
    # element and elements larger than this will be on right side of this element.

    j = start_index - 1

    for i in range(start_index, end_index):  # start_index + 1, start_index + 2, ... end_index - 1
        if arr[i] <= pivot_element:  # if ith element is smaller than or equal to pivot element, then swapping it
            # with the element which is larger than pivot element that is farther from ith index on left side
            j += 1
            arr[j], arr[i] = arr[i], arr[j]

    j += 1
    arr[j], arr[end_index] = arr[end_index], arr[j]

    return j


def sorting(arr: List[float], start_index: int = None, end_index: int = None):
    """
    sorting array between start_index and end_index (both inclusive), in place
    :param arr:
    :param start_index:
    :param end_index:
    """
    start_index = start_index or 0
    end_index = end_index or len(arr) - 1

    if start_index < end_index:
        pivot_index = partitioning(arr, start_index, end_index)  # element at this index is at its sorted position

        sorting(arr, start_index, pivot_index - 1)
        sorting(arr, pivot_index + 1, end_index)


if __name__ == '__main__':
    # array = [1, 4, 2, 5, 6, 7, 1, 0, 4]
    # output = sorted(array)
    # print(array)
    # sorting(array, 0, len(array) - 1)
    # print(array, array == output)
    array = [9, 8, 1]
    # sorting(array)
    print(partitioning(array, 0, 2))
    print(array)
