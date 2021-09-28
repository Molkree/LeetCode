# https://leetcode.com/problems/intersection-of-two-linked-lists/
# 160. Intersection of Two Linked Lists

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional[ListNode] = None


def to_list_node(def_list: list[int], tail: Optional[ListNode] = None):
    result = ListNode(def_list.pop(0))
    if not def_list and tail:
        result.next = tail
    cur_node = result
    while def_list:
        cur_node.next = ListNode(def_list.pop(0))
        cur_node = cur_node.next
        if not def_list and tail:
            cur_node.next = tail
    return result


class Solution:
    def getIntersectionNode(  # noqa: N802
        self, headA: ListNode, headB: ListNode  # noqa: N803
    ) -> Optional[ListNode]:
        # Naive O(n) space solution
        # visited: set[ListNode] = set()
        # head_a_copy = headA
        # head_b_copy = headB
        # while head_a_copy:
        #     visited.add(head_a_copy)
        #     head_a_copy = head_a_copy.next
        # while head_b_copy:
        #     if head_b_copy in visited:
        #         return head_b_copy
        #     head_b_copy = head_b_copy.next
        # return None

        # Cool O(1) space solution
        head_a_copy = headA
        head_b_copy = headB
        while head_a_copy is not head_b_copy:
            head_a_copy = headB if head_a_copy is None else head_a_copy.next
            head_b_copy = headA if head_b_copy is None else head_b_copy.next
        return head_a_copy


solution = Solution()

tail = to_list_node([8, 4, 5])
list_a = to_list_node([4, 1], tail)
list_b = to_list_node([5, 6, 1], tail)
assert tail == solution.getIntersectionNode(list_a, list_b)

tail = to_list_node([2, 4])
list_a = to_list_node([1, 9, 1], tail)
list_b = to_list_node([3], tail)
assert tail == solution.getIntersectionNode(list_a, list_b)

list_a = to_list_node([2, 6, 4])
list_b = to_list_node([1, 5])
assert solution.getIntersectionNode(list_a, list_b) is None
