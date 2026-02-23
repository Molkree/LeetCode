# https://leetcode.com/problems/merge-two-binary-trees/
# 617. Merge Two Binary Trees


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(  # noqa: N802
        self, root1: TreeNode | None, root2: TreeNode | None
    ) -> TreeNode | None:
        if not root1:
            return root2
        elif not root2:
            return root1
        return TreeNode(
            root1.val + root2.val,
            self.mergeTrees(root1.left, root2.left),
            self.mergeTrees(root1.right, root2.right),
        )


solution = Solution()


root1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
root2 = TreeNode(2, TreeNode(1, right=TreeNode(4)), TreeNode(3, right=TreeNode(7)))
result = solution.mergeTrees(root1, root2)
