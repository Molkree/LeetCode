# https://leetcode.com/problems/linked-list-cycle/
# 141. Linked List Cycle


from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


def to_list_node(def_list: list[int], pos: int = -1):
    if not def_list:
        return None
    result = ListNode(def_list.pop(0))
    cur_node = result
    nodes = [cur_node]
    while def_list:
        cur_node.next = ListNode(def_list.pop(0))
        cur_node = cur_node.next
        nodes.append(cur_node)
        if not def_list and pos != -1:
            nodes[-1].next = nodes[pos]
    return result


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:  # noqa: N802
        # Naive O(n) space solution
        # visited: set[ListNode] = set()
        # nodes_count = 0
        # while head:
        #     visited.add(head)
        #     if nodes_count == len(visited):
        #         return True
        #     nodes_count += 1
        #     head = head.next
        # return False

        # O(1) space solution
        fast_head = head
        while head and fast_head:
            head = head.next
            fast_head = fast_head.next
            if fast_head:
                fast_head = fast_head.next
            else:
                return False
            if head == fast_head:
                return True
        return False


solution = Solution()

head = to_list_node([3, 2, 0, -4], 1)
assert solution.hasCycle(head)

head = to_list_node([1, 2], 0)
assert solution.hasCycle(head)

head = to_list_node([1], -1)
assert not solution.hasCycle(head)
