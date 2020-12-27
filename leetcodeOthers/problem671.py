# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.min = None
        self.second_min = None

        self.second_min_value_search(root)

        return -1 if self.second_min is None else self.second_min

    def second_min_value_search(self, root: TreeNode):
        if self.second_min is not None:
            return

        if root.left is not None:
            self.second_min_value_search(root.left)

        if self.min is None:
            self.min = root.val
        elif self.second_min is None and self.min != root.val:
            self.second_min = root.val

        if root.right is not None:
            self.second_min_value_search(root.right)
