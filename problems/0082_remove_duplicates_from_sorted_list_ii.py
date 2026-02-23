# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# 82. Remove Duplicates from Sorted List II


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:  # noqa: N802
        fake_head = ListNode(-101, head)
        node: ListNode | None = fake_head
        while node:
            if node.next and node.next.next and node.next.val == node.next.next.val:
                next_distinct = node.next.next.next
                while next_distinct and next_distinct.val == node.next.val:
                    next_distinct = next_distinct.next
                node.next = next_distinct
            else:
                node = node.next
        return fake_head.next
