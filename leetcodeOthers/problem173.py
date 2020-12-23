from dataclasses import dataclass, field


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


NIL = object()


@dataclass
class BSTIterator:
    root: TreeNode
    current_element: int = field(init=False, default=NIL)
    has_more_elements: bool = field(init=False, default=None)

    def __post_init__(self):
        self.itr = self._next(self.root)

    @staticmethod
    def _next(root: TreeNode):
        if root is not None:
            yield from BSTIterator._next(root.left)
            yield root.val
            yield from BSTIterator._next(root.right)

    def _try_next(self):
        try:
            return next(self.itr)
        except StopIteration:
            return NIL

    def next(self) -> int:
        if self.hasNext():
            self.has_more_elements = None
            return self.current_element

        raise ValueError(f'no element')

    def hasNext(self) -> bool:
        if self.has_more_elements is None:
            self.current_element = self._try_next()
            self.has_more_elements = self.current_element is not NIL

        return self.has_more_elements
