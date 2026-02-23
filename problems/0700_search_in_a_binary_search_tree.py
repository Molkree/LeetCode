# https://leetcode.com/problems/search-in-a-binary-search-tree/
# 700. Search in a Binary Search Tree


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(  # noqa: N802
        self, root: TreeNode | None, val: int
    ) -> TreeNode | None:
        if not root:
            return None
        if val < root.val:
            return self.searchBST(root.left, val)
        if val > root.val:
            return self.searchBST(root.right, val)
        return root
