# https://leetcode.com/problems/maximum-width-of-binary-tree/
# 662. Maximum Width of Binary Tree


from __future__ import annotations

from collections import deque


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:  # noqa: N802
        queue = deque[tuple[TreeNode, int, int]]([(root, 1, 1)])
        cur_level = 1
        min_index = 3001
        max_index = 1
        max_width = 1
        while queue:
            node, index, level = queue.popleft()
            if level > cur_level:
                cur_level += 1
                max_width = max(max_width, max_index - min_index + 1)
                min_index = index
                max_index = 1
            max_index = max(max_index, index)
            if node.left:
                queue.append((node.left, index * 2 - 1, level + 1))
            if node.right:
                queue.append((node.right, index * 2, level + 1))
        return max(max_width, max_index - min_index + 1)
