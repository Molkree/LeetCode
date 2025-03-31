# https://leetcode.com/problems/house-robber-iii/
# 337. House Robber III


from __future__ import annotations

from functools import cache


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @cache
    def rob(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return root.val
        left_haul = 0 if not root.left else self.rob(root.left)
        right_haul = 0 if not root.right else self.rob(root.right)
        left_left_haul = (
            0 if not root.left or not root.left.left else self.rob(root.left.left)
        )
        left_right_haul = (
            0 if not root.left or not root.left.right else self.rob(root.left.right)
        )
        right_left_haul = (
            0 if not root.right or not root.right.left else self.rob(root.right.left)
        )
        right_right_haul = (
            0 if not root.right or not root.right.right else self.rob(root.right.right)
        )
        return max(
            root.val
            + left_left_haul
            + left_right_haul
            + right_left_haul
            + right_right_haul,
            left_haul + right_haul,
        )


solution = Solution()


root = TreeNode(3, TreeNode(2, right=TreeNode(3)), TreeNode(3, right=TreeNode(1)))
assert solution.rob(root) == 7

root = TreeNode(
    3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, right=TreeNode(1))
)
assert solution.rob(root) == 9

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)))
assert solution.rob(root) == 8
