# https://leetcode.com/problems/count-complete-tree-nodes/
# 222. Count Complete Tree Nodes


from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def count_children(self, root: TreeNode, index: int, depth: int) -> int:
        while depth:
            max_leaves = 2**depth
            if index < max_leaves // 2:
                assert root.left
                root = root.left
                depth -= 1
            else:
                assert root.right
                root = root.right
                depth -= 1
                index -= max_leaves // 2
        if root.left and root.right:
            return 2
        if root.left or root.right:
            return 1
        return 0

    def countNodes(self, root: TreeNode | None) -> int:  # noqa: N802
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        node = root
        depth = -1
        while node:
            depth += 1
            node = node.left
        low = 0
        high = 2 ** (depth - 1) - 1
        while low < high:
            mid = low + (high - low) // 2
            if self.count_children(root, mid, depth - 1) == 2:
                low = mid + 1
            else:
                high = mid
        result = 0
        for i in range(depth):
            result += 2**i
        return result + 2 * low + self.count_children(root, low, depth - 1)


solution = Solution()


root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
assert solution.countNodes(root) == 6

root = TreeNode(
    1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))
)
assert solution.countNodes(root) == 7

root = None
assert solution.countNodes(root) == 0

root = TreeNode(1)
assert solution.countNodes(root) == 1

root = TreeNode(
    1,
    TreeNode(2, TreeNode(4, TreeNode(8)), TreeNode(5)),
    TreeNode(3, TreeNode(6), TreeNode(7)),
)
assert solution.countNodes(root) == 8

root = TreeNode(
    1,
    TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5)),
    TreeNode(3, TreeNode(6), TreeNode(7)),
)
assert solution.countNodes(root) == 9
