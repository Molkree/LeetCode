# https://leetcode.com/problems/swap-nodes-in-pairs/
# 24. Swap Nodes in Pairs


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:  # noqa: N802
        tmp_head = ListNode(-1, head)
        node = tmp_head
        while node and (left_node := node.next) and (right_node := left_node.next):
            node.next = right_node
            left_node.next = right_node.next
            right_node.next = left_node
            node = left_node
        return tmp_head.next
