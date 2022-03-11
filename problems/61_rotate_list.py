# https://leetcode.com/problems/rotate-list/
# 61. Rotate List


from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(  # noqa: N802
        self, head: ListNode | None, k: int
    ) -> ListNode | None:
        if not k or not head:
            return head
        lst_len = 0
        node: ListNode | None = head
        while node:
            lst_len += 1
            node = node.next
        k %= lst_len
        if not k:
            return head
        new_head_ind = lst_len - k
        new_head = head
        for _ in range(new_head_ind - 1):
            new_head = new_head.next  # type: ignore
        new_tail = new_head
        new_head = new_head.next  # type: ignore
        new_tail.next = None  # type: ignore
        node = new_head
        while node.next:  # type: ignore
            node = node.next  # type: ignore
        node.next = head  # type: ignore
        return new_head


solution = Solution()
lst = ListNode(1, ListNode(2, ListNode(3)))
solution.rotateRight(lst, 1)

lst = ListNode(1)
solution.rotateRight(lst, 1)
