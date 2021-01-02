# Definition for a binary tree node.
from functools import lru_cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def childs_child(root: TreeNode):
    if root.left:
        yield root.left.left
        yield root.left.right
    if root.right:
        yield root.right.left
        yield root.right.right


class Solution:
    @lru_cache
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0

        return max(
            root.val + sum((self.rob(c) for c in childs_child(root)), start=0),
            self.rob(root.left) + self.rob(root.right),
        )
