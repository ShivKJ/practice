def partitioning(arr, l, r):
    p = arr[r]

    idx = l - 1
    # element at idx+1 will either be greater than p or idx+1 will be equal to r

    for i in range(l, r):
        if arr[i] <= p:
            idx += 1
            arr[idx], arr[i] = arr[i], arr[idx]

    idx += 1
    arr[idx], arr[r] = arr[r], arr[idx]

    return idx


def sorting(arr, l, r):
    if l < r:
        p_idx = partitioning(arr, l, r)

        sorting(arr, l, p_idx - 1)
        sorting(arr, p_idx + 1, r)


if __name__ == '__main__':
    arr = [1, 4, 2, 5, 6, 7, 1, 0, 4]
    print(arr)
    sorting(arr, 0, len(arr) - 1)
    print(arr)
