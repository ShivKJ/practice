from collections import deque

from math import inf


def preprocess(arr: list) -> deque:
    minimum = deque()
    minimum.append(None)

    last = inf

    for i in reversed(range(len(arr))):
        e = arr[i]

        if e < last:
            last = e
            minimum.append(i)

            if e == arr[0]:
                break

    return minimum


def longest_sub_array(arr: list):
    minimum = preprocess(arr)

    smaller = minimum.pop()

    max_size = 1
    max_start = 0

    for i in range(len(arr)):
        while smaller is not None and arr[i] > arr[smaller]:
            if smaller - i + 1 > max_size:
                max_size = smaller - i + 1
                max_start = i

            smaller = minimum.pop()

        if smaller is None:
            break

    return [] if max_size == 1 else arr[max_start:max_start + max_size]


if __name__ == '__main__':
    arr = [-5, -1, 7, 5, 1, -2]

    print(longest_sub_array(arr))
    print(preprocess(arr))
