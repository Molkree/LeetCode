# https://leetcode.com/problems/n-ary-tree-preorder-traversal/
# 589. N-ary Tree Preorder Traversal


from __future__ import annotations


class Node:
    def __init__(self, val: int, children: list[Node] = []):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node | None) -> list[int]:
        if not root:
            return []
        result = [root.val]
        for child in root.children:
            result += self.preorder(child)
        return result
