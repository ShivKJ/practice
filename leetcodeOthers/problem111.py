# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_depth(root: TreeNode):
    if root.left and not root.right:
        return 1 + get_depth(root.left)
    if root.right and not root.left:
        return 1 + get_depth(root.right)
    if root.left and root.right:
        return 1 + min(get_depth(root.left), get_depth(root.right))
    return 1


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return get_depth(root)
