# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# 2095. Delete the Middle Node of a Linked List


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:  # noqa: N802
        if not head or not head.next:
            return None
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next
        slow.next = slow.next.next  # type: ignore
        return head
