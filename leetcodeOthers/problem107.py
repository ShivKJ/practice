# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        output = []

        if root:
            tmp = deque()
            tmp.append((0, root))

            while tmp:
                level, root = tmp.popleft()

                if len(output) == level:
                    output.append([])

                output[level].append(root.val)

                if root.left:
                    tmp.append((level + 1, root.left))

                if root.right:
                    tmp.append((level + 1, root.right))

        return output[::-1]
