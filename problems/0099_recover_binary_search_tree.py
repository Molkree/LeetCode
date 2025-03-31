# https://leetcode.com/problems/recover-binary-search-tree/
# 99. Recover Binary Search Tree


from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:  # noqa: N802
        if not root:
            return

        first: TreeNode | None = None
        second: TreeNode | None = None
        prev = TreeNode(-(2**31) - 1)

        def inorder(node: TreeNode | None) -> None:
            if not node:
                return

            inorder(node.left)
            nonlocal prev, first, second
            if not first and prev.val > node.val:
                first = prev
            if first and prev.val > node.val:
                second = node
            prev = node
            inorder(node.right)

        inorder(root)
        first.val, second.val = second.val, first.val  # type: ignore
