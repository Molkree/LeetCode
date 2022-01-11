# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# 1022. Sum of Root To Leaf Binary Numbers


from __future__ import annotations

from typing import Literal


class TreeNode:
    def __init__(
        self,
        val: Literal[0, 1] = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:  # noqa: N802
        stack: list[tuple[TreeNode, str]] = [(root, "0")]
        result = 0
        while stack:
            node, cur_num = stack.pop()
            cur_num += str(node.val)
            if node.left:
                stack.append((node.left, cur_num))
            if node.right:
                stack.append((node.right, cur_num))
            if not node.left and not node.right:
                result += int(cur_num, 2)
        return result
