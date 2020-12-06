from typing import List


class Stack:
    def __init__(self):
        self._stack = []

    def push(self, e):
        self._stack.append(e)

    def pop(self):
        return self._stack.pop()

    def __bool__(self):
        return bool(self._stack)

    def peek(self):
        return self._stack[-1]


def max_area(arr: List[int]):
    stack = Stack()
    area = 0

    for i, e in enumerate(arr):
        if not stack or arr[stack.peek()] < arr[i]:
            stack.push(i)
        else:
            out = stack.pop()
            area = max([area, arr[out]])

    return area


if __name__ == '__main__':
    s = Stack()

    print(bool(s))
