# https://leetcode.com/problems/insert-into-a-binary-search-tree/
# 701. Insert into a Binary Search Tree


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(  # noqa: N802
        self, root: TreeNode | None, val: int
    ) -> TreeNode | None:
        if not root:
            return TreeNode(val)
        node = root
        while node.left or node.right:
            if node.val > val and node.left:
                node = node.left
            elif node.val < val and node.right:
                node = node.right
            else:
                break
        if node.val > val:
            node.left = TreeNode(val)
        else:
            node.right = TreeNode(val)
        return root
