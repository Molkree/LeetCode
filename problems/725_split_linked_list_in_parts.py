# https://leetcode.com/problems/split-linked-list-in-parts/
# 725. Split Linked List in Parts

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def to_list(node: Optional[ListNode]) -> list[int]:
    if not node:
        return []
    result: list[int] = [node.val]
    node = node.next
    while node:
        result.append(node.val)
        node = node.next
    return result


def to_list_node(def_list: list[int]):
    if not def_list:
        return None
    result = ListNode(def_list.pop(0))
    cur_node = result
    while def_list:
        cur_node.next = ListNode(def_list.pop(0))
        cur_node = cur_node.next
    return result


class Solution:
    def splitListToParts(  # noqa: N802
        self, head: Optional[ListNode], k: int
    ) -> list[Optional[ListNode]]:
        length = 0
        while head:
            length += 1
            head = head.next
        return []


solution = Solution()

head = to_list_node([1, 2, 3])
k = 5

assert [[1], [2], [3], None, None] == solution.splitListToParts(head, k)
