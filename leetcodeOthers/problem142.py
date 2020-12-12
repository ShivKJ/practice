class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def has_been_visited(node: ListNode) -> bool:
        if hasattr(node, 'visited'):
            return True
        setattr(node, 'visited', True)
        return False

    def detectCycle(self, head: ListNode) -> ListNode:
        while head is not None and not self.has_been_visited(head):
            head = head.next

        return head
