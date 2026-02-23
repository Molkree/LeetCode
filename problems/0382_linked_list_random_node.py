# https://leetcode.com/problems/linked-list-random-node/
# 382. Linked List Random Node


import random


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    # Naive solution
    # def __init__(self, head: ListNode):
    #     self.head = head
    #     self.length = 0
    #     node = head
    #     while node:
    #         node = node.next
    #         self.length += 1

    # def getRandom(self) -> int:  # noqa: N802
    #     ind = random.randrange(self.length)
    #     node = self.head
    #     for _ in range(ind):
    #         node = node.next  # type: ignore
    #     return node.val  # type: ignore

    # Reservoir sampling
    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:  # noqa: N802
        rand = self.head.val
        count = 1
        node = self.head.next
        while node:
            count += 1
            if random.uniform(0, 1) <= 1 / count:
                rand = node.val
            node = node.next
        return rand
