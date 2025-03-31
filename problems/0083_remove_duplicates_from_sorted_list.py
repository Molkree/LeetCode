# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# 83. Remove Duplicates from Sorted List


from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:  # noqa: N802
        node: ListNode | None = head
        while node:
            if node.next and node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
