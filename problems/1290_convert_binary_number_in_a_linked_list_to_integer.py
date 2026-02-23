# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# 1290. Convert Binary Number in a Linked List to Integer


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:  # noqa: N802
        bin_value = "0b"
        node = head
        while node:
            bin_value += str(node.val)
            node = node.next
        return int(bin_value, 2)
