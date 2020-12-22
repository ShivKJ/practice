# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def travel(root: TreeNode, container: List):
    if root is None:
        return
    container.append(root.val)
    travel(root.left, container)
    travel(root.right, container)


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        travel(root, output)
        return output
