def fun(o, c, current, n):
    if o == c == n:
        yield current

    if o < c:
        return

    if o < n:
        yield from fun(o + 1, c, current + '(', n)

    if c < n:
        yield from fun(o, c + 1, current + ')', n)


def generate(n):
    yield from fun(0, 0, '', n)


if __name__ == '__main__':
    for i in generate(3):
        print(i)
