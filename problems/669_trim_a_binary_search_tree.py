# https://leetcode.com/problems/trim-a-binary-search-tree/
# 669. Trim a Binary Search Tree


from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(  # noqa: N802
        self, root: TreeNode | None, low: int, high: int
    ) -> TreeNode | None:
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root


solution = Solution()


root = TreeNode(1, TreeNode(0), TreeNode(2))
low = 1
high = 2
solution.trimBST(root, low, high)

root = TreeNode(3, TreeNode(0, right=TreeNode(2, TreeNode(1))), TreeNode(4))
low = 1
high = 3
solution.trimBST(root, low, high)

root = TreeNode(1)
low = 1
high = 2
solution.trimBST(root, low, high)

root = TreeNode(1, right=TreeNode(2))
low = 1
high = 3
solution.trimBST(root, low, high)

root = TreeNode(1, right=TreeNode(2))
low = 2
high = 4
solution.trimBST(root, low, high)
