# https://leetcode.com/problems/increasing-order-search-tree/
# 897. Increasing Order Search Tree


from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:  # noqa: N802
        new_root = TreeNode(-1)
        copy_root = new_root

        def rearrange(node: TreeNode) -> None:
            if node.left:
                rearrange(node.left)
            nonlocal copy_root
            copy_root.right = TreeNode(node.val)
            copy_root = copy_root.right
            if node.right:
                rearrange(node.right)

        rearrange(root)
        return new_root.right  # type: ignore
