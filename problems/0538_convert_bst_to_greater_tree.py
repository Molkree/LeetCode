# https://leetcode.com/problems/convert-bst-to-greater-tree/
# 538. Convert BST to Greater Tree


from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode | None) -> TreeNode | None:  # noqa: N802
        prefix_sum = 0

        def fill_sums(root: TreeNode | None) -> None:
            if root is None:
                return
            fill_sums(root.right)
            nonlocal prefix_sum
            prefix_sum += root.val
            root.val = prefix_sum
            fill_sums(root.left)

        fill_sums(root)
        return root
