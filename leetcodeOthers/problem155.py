from collections import deque
from dataclasses import dataclass, field
from typing import Deque


@dataclass
class MinStack:
    arr: Deque[int] = field(init=False, default_factory=deque)
    min_arr: Deque[int] = field(init=False, default_factory=deque)

    def push(self, x: int) -> None:
        self.arr.append(x)

        if not self.min_arr or x <= self.min_arr[-1]:
            self.min_arr.append(x)

    def pop(self) -> None:
        e = self.arr.pop()

        if e == self.min_arr[-1]:
            self.min_arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min_arr[-1]
