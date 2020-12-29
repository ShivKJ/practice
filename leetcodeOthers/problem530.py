# Definition for a binary tree node.
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.prev = inf
        self.min_diff = inf

    def getMinimumDifference(self, root: TreeNode) -> int:
        self.get_mad(root)
        return self.min_diff

    def get_mad(self, root: TreeNode):
        if root:
            self.get_mad(root.left)

            self.min_diff = min(abs(self.prev - root.val), self.min_diff)
            self.prev = root.val

            self.get_mad(root.right)
