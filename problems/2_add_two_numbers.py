# https://leetcode.com/problems/add-two-numbers/
# 2. Add Two Numbers


from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(  # noqa: N802
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        result = ListNode()
        node = result
        transfer = 0
        while l1 or l2:
            value = transfer
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            node.next = ListNode(value % 10)
            node = node.next
            transfer = value // 10
        if transfer:
            node.next = ListNode(1)
        return result.next
