# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# 1008. Construct Binary Search Tree from Preorder Traversal


from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def build_bst(
        self, min: int, max: int, preorder: list[int], index: int
    ) -> tuple[TreeNode | None, int]:
        if index == len(preorder):
            return None, index
        value = preorder[index]
        if value < min or value > max:
            return None, index
        root = TreeNode(value)
        index += 1
        root.left, index = self.build_bst(min, value - 1, preorder, index)
        root.right, index = self.build_bst(value + 1, max, preorder, index)
        return root, index

    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:  # noqa: N802
        return self.build_bst(0, 10 ** 8 + 1, preorder, 0)[0]


solution = Solution()

solution.bstFromPreorder([8, 5, 1, 7, 10, 12])
