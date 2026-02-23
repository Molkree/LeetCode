# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# 116. Populating Next Right Pointers in Each Node


class Node:
    def __init__(
        self,
        val: int = 0,
        left: Node | None = None,
        right: Node | None = None,
        next: Node | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node | None) -> Node | None:
        if not root:
            return root
        prev = root
        cur: Node | None = None
        while prev.left:
            cur = prev
            while cur:
                cur.left.next = cur.right  # type: ignore
                if cur.next:
                    cur.right.next = cur.next.left  # type: ignore
                cur = cur.next
            prev = prev.left
        return root
