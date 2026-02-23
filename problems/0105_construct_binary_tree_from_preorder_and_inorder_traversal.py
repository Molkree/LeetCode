# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 105. Construct Binary Tree from Preorder and Inorder Traversal


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(  # noqa: N802
        self, preorder: list[int], inorder: list[int]
    ) -> TreeNode | None:
        inorder_indices = {value: index for index, value in enumerate(inorder)}

        def build_subtree(low: int, high: int) -> TreeNode | None:
            if low > high:
                return None
            root = TreeNode(preorder.pop(0))
            root_index = inorder_indices[root.val]
            root.left = build_subtree(low, root_index - 1)
            root.right = build_subtree(root_index + 1, high)
            return root

        return build_subtree(0, len(inorder) - 1)
