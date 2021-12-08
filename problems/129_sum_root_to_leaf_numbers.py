# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# 129. Sum Root to Leaf Numbers


from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:  # noqa: N802
        sum = 0

        def dfs(root: TreeNode | None, num: int):
            if not root:
                return
            num = num * 10 + root.val
            if not root.left and not root.right:
                nonlocal sum
                sum += num
                return
            dfs(root.left, num)
            dfs(root.right, num)

        dfs(root, 0)
        return sum


solution = Solution()


root = TreeNode(1, TreeNode(2), TreeNode(3))
assert solution.sumNumbers(root) == 25

root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
assert solution.sumNumbers(root) == 1026

root = TreeNode(0, TreeNode(1))
assert solution.sumNumbers(root) == 1
