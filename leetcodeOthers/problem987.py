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
        queue.append(root)
        output = defaultdict(lambda: defaultdict(list))

        root.xy = 0, 0
        while queue:
            e = queue.popleft()
            x, y = e.xy

            output[x][y].append(e.val)

            if e.left is not None:
                e.left.xy = x - 1, y - 1
                queue.append(e.left)

            if e.right is not None:
                e.right.xy = x + 1, y - 1
                queue.append(e.right)

        return [process_dict(output[k]) for k in sorted(output.keys())]
