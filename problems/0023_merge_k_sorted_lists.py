# https://leetcode.com/problems/merge-k-sorted-lists/
# 23. Merge k Sorted Lists


from __future__ import annotations

import heapq


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(  # noqa: N802
        self, lists: list[ListNode | None]
    ) -> ListNode | None:
        if not lists:
            return None
        builtin_lists = list[list[int]]()
        for lst in lists:
            builtin_lst = list[int]()
            while lst:
                builtin_lst.append(lst.val)
                lst = lst.next
            if builtin_lst:
                builtin_lists.append(builtin_lst)
        if not builtin_lists:
            return None
        sorted_builtin_list = list(heapq.merge(*builtin_lists))
        sorted_list = ListNode(sorted_builtin_list[-1])
        for num in sorted_builtin_list[-2::-1]:
            sorted_list = ListNode(num, sorted_list)
        return sorted_list
