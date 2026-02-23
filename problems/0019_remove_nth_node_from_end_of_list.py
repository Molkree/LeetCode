# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# 19. Remove Nth Node From End of List


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode | None:  # noqa: N802
        if n == 1 and not head.next:
            return None
        head = ListNode(-1, head)
        slow = head
        fast = head
        for _ in range(n + 1):
            fast = fast.next  # type: ignore
        while fast:
            slow = slow.next  # type: ignore
            fast = fast.next
        slow.next = slow.next.next  # type: ignore
        head = head.next  # type: ignore
        return head
