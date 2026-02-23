# https://leetcode.com/problems/path-sum-iii/
# 437. Path Sum III


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    roots: set[TreeNode] = set()

    def check_path(self, root: TreeNode | None, target_sum: int, cur_sum: int) -> int:
        if not root:
            return 0
        cur_sum += root.val
        result = self.check_path(root.left, target_sum, cur_sum)
        result += self.check_path(root.right, target_sum, cur_sum)
        if root.left and root.left not in self.roots:
            result += self.check_path(root.left, target_sum, 0)
            self.roots.add(root.left)
        if root.right and root.right not in self.roots:
            result += self.check_path(root.right, target_sum, 0)
            self.roots.add(root.right)
        if cur_sum == target_sum:
            result += 1
        return result

    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:  # noqa: N802, N803
        return self.check_path(root, targetSum, 0)


solution = Solution()


root = TreeNode(
    10,
    TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, right=TreeNode(1))),
    TreeNode(-3, right=TreeNode(11)),
)
target_sum = 8
assert 3 == solution.pathSum(root, target_sum)

root = TreeNode(
    5,
    TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
    TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))),
)
target_sum = 22
assert 3 == solution.pathSum(root, target_sum)

root = TreeNode(
    1, right=TreeNode(2, right=TreeNode(3, right=TreeNode(4, right=TreeNode(5))))
)
target_sum = 3
assert 2 == solution.pathSum(root, target_sum)
