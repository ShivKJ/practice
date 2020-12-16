from typing import List


def get_min(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[left] > arr[mid]:
            left += 1
            right = mid
        elif arr[mid] > arr[right]:
            left = mid + 1
        else:
            return min(arr[left], arr[mid], arr[right])

    return min(arr[left], arr[right])


if __name__ == '__main__':
    import numpy as np

    for size in [
        1000, 1001, 1,
        5,
        10, 11, 15
    ]:
        test_array = np.arange(size)

        min_element = test_array.min()

        for i in range(size):
            test_array = np.roll(test_array, 1)
            min_got = get_min(test_array)

            if min_got != min_element:
                raise ValueError(f'min_element expected={min_element} but got={min_got}, size={size}')
