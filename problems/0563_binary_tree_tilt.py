# https://leetcode.com/problems/binary-tree-tilt/
# 563. Binary Tree Tilt


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode | None) -> int:  # noqa: N802
        tilt = 0

        def node_sum(root: TreeNode | None) -> int:
            nonlocal tilt
            if not root:
                return 0
            left_sum = node_sum(root.left)
            right_sum = node_sum(root.right)
            tilt += abs(left_sum - right_sum)
            return left_sum + right_sum + root.val

        node_sum(root)
        return tilt
