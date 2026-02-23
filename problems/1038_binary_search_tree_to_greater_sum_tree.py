# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
# 1038. Binary Search Tree to Greater Sum Tree


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:  # noqa: N802
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
