# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# 106. Construct Binary Tree from Inorder and Postorder Traversal


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(  # noqa: N802
        self, inorder: list[int], postorder: list[int]
    ) -> TreeNode | None:
        inorder_indices = {value: index for index, value in enumerate(inorder)}

        def build_subtree(low: int, high: int) -> TreeNode | None:
            if low > high:
                return None
            root = TreeNode(postorder.pop())
            root_index = inorder_indices[root.val]
            root.right = build_subtree(root_index + 1, high)
            root.left = build_subtree(low, root_index - 1)
            return root

        return build_subtree(0, len(inorder) - 1)
