# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# 230. Kth Smallest Element in a BST


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:  # noqa: N802
        result = -1

        def inorder(root: TreeNode | None) -> None:
            if not root:
                return
            inorder(root.left)
            nonlocal k
            k -= 1
            if not k:
                nonlocal result
                result = root.val
                return
            inorder(root.right)

        inorder(root)
        return result
