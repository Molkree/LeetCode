# https://leetcode.com/problems/copy-list-with-random-pointer/
# 138. Copy List with Random Pointer


class Node:
    def __init__(self, x: int, next: Node | None = None, random: Node | None = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:  # noqa: N802
        if not head:
            return None
        copy_head = Node(head.val)
        node = head
        copy_node = copy_head
        old_to_new = {head: copy_head}
        while node.next:
            copy_node.next = Node(node.next.val)
            copy_node = copy_node.next
            node = node.next
            old_to_new[node] = copy_node
        node = head
        while node:
            if old_rand_node := node.random:
                new_node = old_to_new[node]
                new_rand_node = old_to_new[old_rand_node]
                new_node.random = new_rand_node
            node = node.next
        return copy_head
