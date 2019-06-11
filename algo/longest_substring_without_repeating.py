def fun(string: str) -> str:
    s, e = 0, 0
    start_idx, end_idx = 0, 0

    for i in range(1, len(string)):
        if string[i] == string[end_idx]:
            if e - s < end_idx - start_idx:
                s, e = start_idx, end_idx

            start_idx = end_idx = i
        else:
            end_idx = i

    return string[s:e + 1]


if __name__ == '__main__':
    print(fun('aabccccdefggg'))
