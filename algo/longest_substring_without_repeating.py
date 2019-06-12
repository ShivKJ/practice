def fun(string: str) -> str:
    if not string:
        return 0

    s, e = 0, 0
    start_idx, end_idx = 0, 0

    characters = [None] * 128
    characters[ord(string[0])] = 0

    for i in range(1, len(string)):
        key = ord(string[i])
        idx = characters[key]

        if idx is not None and idx >= start_idx:
            if e - s < end_idx - start_idx:
                s, e = start_idx, end_idx

            start_idx = idx + 1

        end_idx = i

        characters[key] = i
    else:
        if e - s < end_idx - start_idx:
            s, e = start_idx, end_idx
    return e - s + 1


if __name__ == '__main__':
    # print(fun('aabccccdefggg'))
    # print(fun("abcabcbb"))
    # print(fun('au'))
    print(fun("dvdf"))
