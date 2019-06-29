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


# def tmp(arr, l, r):
#     p = arr[l]
#     t = l
#
#     while l <= r:
#         if arr[l] >= p:
#             j = get_next_min(arr, p, l + 1, r)
#             if j != -1:
#                 arr[l], arr[j] = arr[j], arr[l]
#             else:
#                 return max(t, l - 1)
#         l += 1
#
#     return r
#
#
# def get_next_min(arr, e, l, r):
#     for i in range(l, r + 1):
#         if arr[i] < e:
#             return i
#
#     for i in range(l, r + 1):
#         if arr[i] == e:
#             return i
#
#     return -1


def sorting(arr, l, r):
    if l < r:
        p_idx = partitioning(arr, l, r)
        # p_idx = tmp(arr, l, r)

        sorting(arr, l, p_idx - 1)
        sorting(arr, p_idx + 1, r)


if __name__ == '__main__':
    arr = [1, 4, 2, 5, 6, 7, 1, 0, 4]
    output = sorted(arr)
    print(arr)
    # print(tmp(arr, 0, len(arr) - 1))
    sorting(arr, 0, len(arr) - 1)
    print(arr, arr == output)
