# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int):
        self.value = None
        self.curr = 0
        self.k = k

        self.kth_smallest(root)

        return self.value

    def kth_smallest(self, root: TreeNode):
        if self.value is not None:
            return

        if root.left is not None:
            self.kth_smallest(root.left)

        self.curr += 1

        if self.curr == self.k:
            self.value = root.val

        if root.right is not None:
            self.kth_smallest(root.right)
