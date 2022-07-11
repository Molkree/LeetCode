# https://leetcode.com/problems/binary-tree-right-side-view/
# 199. Binary Tree Right Side View


from __future__ import annotations

from collections import deque


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:  # noqa: N802
        result = list[int]()
        queue: deque[tuple[TreeNode | None, int]] = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if node:
                if depth == len(result):
                    result.append(node.val)
                queue.append((node.right, depth + 1))
                queue.append((node.left, depth + 1))
        return result


solution = Solution()


root = TreeNode(1, TreeNode(2, right=TreeNode(5)), TreeNode(3, right=TreeNode(4)))
assert solution.rightSideView(root) == [1, 3, 4]

root = TreeNode(1, right=TreeNode(3))
assert solution.rightSideView(root) == [1, 3]

assert solution.rightSideView(None) == []

root = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4))
assert solution.rightSideView(root) == [1, 4, 3]
