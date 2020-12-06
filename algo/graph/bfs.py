"""
author: Shiv
email: shivkj001@gmail.com
date: 3/30/20

MIT License

Copyright (c) [2018]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

from collections import deque
from dataclasses import dataclass, field
from enum import Enum
from typing import Deque, List


class Color(Enum):
    WHITE = 1
    GREY = 2
    BLACK = 3


@dataclass
class Vertex:
    id: int
    adjacent: List['Vertex'] = field(default_factory=list, init=False)

    info: dict = field(default_factory=dict, init=False)

    def __post_init__(self):
        self.info['color'] = Color.WHITE

    def __getitem__(self, item):
        return self.info[item]

    def __setitem__(self, key, value):
        self.info[key] = value

    def __contains__(self, item):
        return item in self.info

    def get(self, key, default):
        return self.info.setdefault(key, default)

    @property
    def uncolored(self) -> bool:
        return self.info['color'] == Color.WHITE


def bfs(v: Vertex):
    v['color'] = Color.GREY
    v['parent'] = v
    v['distance'] = 0

    q: Deque[Vertex] = deque()
    q.append(v)

    while q:
        u = q.popleft()

        for t in u.adjacent:
            if t.uncolored:
                t['parent'] = u
                t['distance'] = u['distance'] + 1
                t['color'] = Color.GREY

                q.append(t)

        u['color'] = Color.BLACK


def dfs(v: Vertex):
    v['parent'] = v

    _dfs(v, 0)


def _dfs(v: Vertex, time):
    v['color'] = Color.GREY

    for u in v.adjacent:
        if u.uncolored:
            u['parent'] = v
            _dfs(u, time)

    v['color'] = Color.BLACK
