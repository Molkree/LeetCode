# https://leetcode.com/problems/delete-node-in-a-bst/
# 450. Delete Node in a BST


from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(  # noqa: N802
        self, root: TreeNode | None, key: int
    ) -> TreeNode | None:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            node = root.right
            while node.left:
                node = node.left
            root.val = node.val
            root.right = self.deleteNode(root.right, root.val)

        return root
