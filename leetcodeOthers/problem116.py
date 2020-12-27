"""
# Definition for a Node.
"""
from typing import Dict


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def populate(n: Node, level, cache: Dict[int, Node]):
    if n.right:
        populate(n.right, level + 1, cache)

    n.next = cache.get(level)
    cache[level] = n

    if n.left:
        populate(n.left, level+1, cache)


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        populate(root, 0, {})
        return root
