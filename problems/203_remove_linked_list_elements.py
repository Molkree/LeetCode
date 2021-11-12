# https://leetcode.com/problems/remove-linked-list-elements/
# 203. Remove Linked List Elements


class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(  # noqa: N802
        self, head: ListNode | None, val: int
    ) -> ListNode | None:
        while head and head.val == val:
            head = head.next
        node = head
        while node and node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return head
