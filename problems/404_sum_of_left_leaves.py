# https://leetcode.com/problems/sum-of-left-leaves/
# 404. Sum of Left Leaves


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:  # noqa: N802
        sum = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                if not node.left.left and not node.left.right:
                    sum += node.left.val
                else:
                    stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return sum


solution = Solution()


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert solution.sumOfLeftLeaves(root) == 24

root = TreeNode(1)
assert solution.sumOfLeftLeaves(root) == 0
