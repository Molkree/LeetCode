# https://leetcode.com/problems/merge-two-sorted-lists/
# 21. Merge Two Sorted Lists


from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


def to_list(node: ListNode | None) -> list[int]:
    if not node:
        return []
    result = [node.val]
    node = node.next
    while node:
        result.append(node.val)
        node = node.next
    return result


def to_list_node(def_list: list[int]) -> ListNode | None:
    if not def_list:
        return None
    result = ListNode(def_list.pop(0))
    cur_node = result
    while def_list:
        cur_node.next = ListNode(def_list.pop(0))
        cur_node = cur_node.next
    return result


class Solution:
    def mergeTwoLists(  # noqa: N802
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            l1, l2 = l2, l1
        result = ListNode(l1.val)
        l1 = l1.next
        cur_node = result
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    cur_node.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    cur_node.next = ListNode(l2.val)
                    l2 = l2.next
                cur_node = cur_node.next
            elif l1 and not l2:
                cur_node.next = l1
                break
            else:
                cur_node.next = l2
                break
        return result


solution = Solution()
l1 = to_list_node([1, 2, 4])
l2 = to_list_node([1, 3, 4])
assert [1, 1, 2, 3, 4, 4] == to_list(solution.mergeTwoLists(l1, l2))

l1 = to_list_node([])
l2 = to_list_node([])
assert [] == to_list(solution.mergeTwoLists(l1, l2))

l1 = to_list_node([])
l2 = to_list_node([0])
assert [0] == to_list(solution.mergeTwoLists(l1, l2))
