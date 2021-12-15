# https://leetcode.com/problems/insertion-sort-list/
# 147. Insertion Sort List


from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:  # noqa: N802
        temp_node = ListNode(-5001)
        node = head
        prev = temp_node
        while node:
            next_node = node.next
            while prev.next and prev.next.val < node.val:
                prev = prev.next
            node.next = prev.next
            prev.next = node
            prev = temp_node
            node = next_node
        return temp_node.next


solution = Solution()


head = ListNode(4, ListNode(2))
sorted_list = solution.insertionSortList(head)

head = ListNode(4, ListNode(2, ListNode(3)))
sorted_list = solution.insertionSortList(head)

head = ListNode(-1, ListNode(5, ListNode(3, ListNode(0))))
sorted_list = solution.insertionSortList(head)
pass
