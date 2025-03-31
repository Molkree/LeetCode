# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# 430. Flatten a Multilevel Doubly Linked List


from __future__ import annotations


class Node:
    def __init__(
        self, val: int, prev: Node | None, next: Node | None, child: Node | None
    ):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten_children(self, head: Node, next_node: Node | None) -> Node:
        node = head
        while node.next:
            if node.child:
                node.next = self.flatten_children(node.child, node.next)
                node.next.prev = node
                node.child = None
            node = node.next
        node.next = next_node
        if next_node:
            next_node.prev = node
        return head

    def flatten(self, head: Node) -> Node:
        node = head
        while node:
            if node.child:
                node.next = self.flatten_children(node.child, node.next)
                node.next.prev = node
                node.child = None
            node = node.next
        return head


solution = Solution()


head = Node(1, None, None, None)
head.child = Node(3, None, None, None)
node = Node(2, head, None, None)
head.next = node
head = solution.flatten(head)
while head:
    print(head.val)
    head = head.next

head = Node(1, None, None, Node(2, None, None, Node(3, None, None, None)))
head = solution.flatten(head)
while head:
    print(head.val)
    head = head.next
