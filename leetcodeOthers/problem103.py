# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        output = []

        if not root:
            return output

        current = deque()
        current.append(root)

        from_left_to_right = False

        while current:
            next_level = deque()

            output.append([])

            while current:
                node: TreeNode = current.popleft()
                output[-1].append(node.val)

                if node.left:
                    next_level.append(node.left)

                if node.right:
                    next_level.append(node.right)

            current = next_level

            if from_left_to_right:
                output[-1] = reversed(output[-1])

            from_left_to_right = not from_left_to_right

        return output
