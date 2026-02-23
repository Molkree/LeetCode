# https://leetcode.com/problems/middle-of-the-linked-list/
# 876. Middle of the Linked List


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:  # noqa: N802
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next
        return slow
