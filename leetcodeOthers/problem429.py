"""
# Definition for a Node.
"""
from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        output = []

        if not root:
            return output
        
        current_level = deque()
        current_level.append(root)

        while current_level:
            next_level = deque()
            output.append([])

            while current_level:
                node: Node = current_level.popleft()
                next_level.extend(node.children)

                output[-1].append(node.val)

            current_level = next_level

        return output
