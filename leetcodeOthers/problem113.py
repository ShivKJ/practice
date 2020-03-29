"""
author: Shiv
email: shivkj001@gmail.com
date: 3/28/20

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


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque
from typing import Deque, List, Union


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        container = [deque()]

        Solution._path_sum(root, sum, container)

        return container[:-1]

    @staticmethod
    def _path_sum(root: TreeNode, sum, container: List[Union[Deque[int], List[int]]]):
        d = container[-1]
        d.append(root.val)

        if not root.left and not root.right:
            if sum == root.val:
                container[-1] = list(d)
                container.append(d)

        else:
            if not root.right:
                Solution._path_sum(root.left, sum - root.val, container)
            elif not root.left:
                Solution._path_sum(root.right, sum - root.val, container)
            else:
                Solution._path_sum(root.left, sum - root.val, container)
                Solution._path_sum(root.right, sum - root.val, container)
        d.pop()
