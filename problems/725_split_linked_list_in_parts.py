# https://leetcode.com/problems/split-linked-list-in-parts/
# 725. Split Linked List in Parts


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def to_list(node: ListNode | None) -> list[int] | None:
    if not node:
        return None
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
        self, head: ListNode | None, k: int
    ) -> list[ListNode | None]:
        length = 0
        copy_head = head
        while copy_head:
            length += 1
            copy_head = copy_head.next
        big_chunks = length % k
        chunk_size = length // k
        result: list[ListNode | None] = []
        copy_head = head
        for _ in range(big_chunks):
            result.append(copy_head)
            last_node = copy_head
            for _ in range(chunk_size):
                last_node = last_node.next
            copy_head = last_node.next
            last_node.next = None
        for _ in range(k - big_chunks):
            result.append(copy_head)
            if copy_head:
                last_node = copy_head
                for _ in range(chunk_size - 1):
                    last_node = last_node.next
                copy_head = last_node.next
                last_node.next = None
        return result


solution = Solution()

head = to_list_node([1, 2, 3])
k = 5
assert [[1], [2], [3], None, None] == [
    to_list(node) for node in solution.splitListToParts(head, k)
]

head = to_list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
k = 3
assert [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]] == [
    to_list(node) for node in solution.splitListToParts(head, k)
]
