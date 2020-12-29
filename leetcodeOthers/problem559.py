"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def get_depth(root: Node):
    if not root.children:
        return 1
    return 1 + max(get_depth(c) for c in root.children)


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        return get_depth(root)
