# https://leetcode.com/problems/odd-even-linked-list/
# 328. Odd Even Linked List


from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:  # noqa: N802
        if not head:
            return head
        odd = head
        even_head = head.next
        even = even_head
        while even and even.next and odd:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head
