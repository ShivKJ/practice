def fun(prefix: str, s: str, container: list):
    if not s:
        container.append(prefix)

    for i, e in enumerate(s):
        fun(prefix + e, s[:i] + s[i + 1:], container)


def generate(s) -> list:
    container = []

    fun('', s, container)

    return container


if __name__ == '__main__':
    print(generate('ABC'))
