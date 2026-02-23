# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/submissions/
# 1026. Maximum Difference Between Node and Ancestor


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode | None) -> int:  # noqa: N802
        if not root:
            return 0

        def max_diff(node: TreeNode | None, cur_max: int, cur_min: int) -> int:
            if not node:
                return cur_max - cur_min
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            left = max_diff(node.left, cur_max, cur_min)
            right = max_diff(node.right, cur_max, cur_min)
            return max(left, right)

        return max_diff(root, root.val, root.val)
