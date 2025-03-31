# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# 104. Maximum Depth of Binary Tree


from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:  # noqa: N802
        if not root:
            return 0
        max_depth = 0
        stack: list[tuple[TreeNode, int]] = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
            if not node.left and not node.right:
                max_depth = max(max_depth, depth)
        return max_depth
