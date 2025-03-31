# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# 111. Minimum Depth of Binary Tree


from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode | None) -> int:  # noqa: N802
        if not root:
            return 0
        min_depth = 10**5
        stack: list[tuple[TreeNode, int]] = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if depth >= min_depth:
                continue
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
            if not node.left and not node.right:
                min_depth = depth
        return min_depth
