def fun(arr, e):
    mapping = {}

    for i, a in enumerate(arr):
        target = a - e

        if target in mapping:
            return mapping[target], i

        mapping[a] = i

    return None
