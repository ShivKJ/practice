def fun(arr, n) -> bool:
    arr = sorted(arr)
    l = len(arr)

    for i in range(l - 2):
        e = arr[i]

        left = i + 1
        right = l - 1

        while left < right:
            s = e + arr[left] + arr[right]

            if s == n:
                return True

            if s < n:
                left += 1
            else:
                right -= 1

    return False


if __name__ == '__main__':
    print(fun([1, 2, 0, 4, 6], 10))
