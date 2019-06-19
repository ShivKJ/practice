def binary_search(arr):
    lo, hi = 0, len(arr) - 1
    mid = None

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[lo] == arr[mid]:
            lo += 1
        elif arr[mid] == arr[hi]:
            hi -= 1
        elif arr[lo] < arr[mid] < arr[hi]:
            return arr[lo]
        elif arr[lo] > arr[mid]:
            lo += 1
        else:
            lo = mid + 1

    return arr[mid]


if __name__ == '__main__':
    import numpy as np

    np.random.seed(10)
    a = np.random.randint(10, 100, 100)
    a.sort()
    a = list(a)
    a = a[10:] + a[:10]
    print(min(a))
    print(a)
    print(binary_search(a))
    print(binary_search(a))
    print(binary_search([1, 1, 1, 1, 1, 1, 1, 1, 1]))
    a = list(reversed(list(range(10))))
    print(a)
    print(binary_search(a))
