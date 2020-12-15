# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.processed_max_height = 0

        return self.root_right_left(root, 0, [])

    def root_right_left(self, node: TreeNode, height, output: list):

        if height == self.processed_max_height:
            output.append(node.val)
            self.processed_max_height += 1

        height += 1

        if node.right is not None:
            self.root_right_left(node.right, height, output)

        if node.left is not None:
            self.root_right_left(node.left, height, output)

        return output
