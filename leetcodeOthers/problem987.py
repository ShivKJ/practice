# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def process_dict(y_to_val: dict):
    out = []
    for k in sorted(y_to_val, reverse=True):
        out.extend(y_to_val[k])
    return out


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        queue = deque()
        queue.append((root, 0, 0))
        output = []

        while queue:
            e, x, y = queue.popleft()
            output.append((x, y, root.val))

            if e.left is not None:
                e.left.xy = x - 1, y + 1
                queue.append((e.left, x - 1, y + 1))

            if e.right is not None:
                queue.append((e.right, x + 1, y + 1))

        output.sort()

        tmp = defaultdict(list)

        for x, y, val in output:
            tmp[x].append(val)

        return list(tmp.values())
