# https://leetcode.com/problems/binary-tree-level-order-traversal/
# 102. Binary Tree Level Order Traversal


from collections import deque


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:  # noqa: N802
        if not root:
            return []
        prev_level = 0
        queue = deque[tuple[TreeNode, int]]([(root, prev_level)])
        levels = list[list[int]]([[]])
        while queue:
            node, level = queue.popleft()
            if prev_level != level:
                levels.append([])
                prev_level = level
            levels[-1].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return levels


solution = Solution()


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert solution.levelOrder(root) == [[3], [9, 20], [15, 7]]

root = TreeNode(1)
assert solution.levelOrder(root) == [[1]]

assert solution.levelOrder(None) == []
