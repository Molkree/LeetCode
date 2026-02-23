# https://leetcode.com/problems/diameter-of-binary-tree/
# 543. Diameter of Binary Tree


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:  # noqa: N802
        if not root:
            return 0

        result = 0

        def height(root: TreeNode | None) -> int:
            if not root:
                return 0
            nonlocal result
            left = height(root.left)
            right = height(root.right)
            result = max(result, left + right)
            return 1 + max(left, right)

        height(root)
        return result


solution = Solution()

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(solution.diameterOfBinaryTree(root))
assert 3 == solution.diameterOfBinaryTree(root)

root = TreeNode(1, TreeNode(2))
assert 1 == solution.diameterOfBinaryTree(root)

root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(41)), TreeNode(5, TreeNode(51))))
assert 4 == solution.diameterOfBinaryTree(root)
