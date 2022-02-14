# https://leetcode.com/problems/balanced-binary-tree/
# 110. Balanced Binary Tree


from __future__ import annotations

from functools import cache


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:  # noqa: N802
        @cache
        def get_depth(node: TreeNode | None) -> int:
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            left_depth = 0 if not node.left else get_depth(node.left)
            right_depth = 0 if not node.right else get_depth(node.right)
            return 1 + max(left_depth, right_depth)

        if not root:
            return True
        stack = [root]
        while stack:
            node = stack.pop()
            if abs(get_depth(node.left) - get_depth(node.right)) > 1:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return True
