# https://leetcode.com/problems/cousins-in-binary-tree/
# 993. Cousins in Binary Tree

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:  # noqa: N802
        x_parent = 0
        y_parent = 0
        if not root:
            return False
        queue: deque[tuple[TreeNode, int]] = deque()
        queue.append((root, 0))
        while queue:
            width = len(queue)
            while width:
                node, parent = queue.popleft()
                if node.val == x:
                    x_parent = parent
                elif node.val == y:
                    y_parent = parent
                if node.left:
                    queue.append((node.left, node.val))
                if node.right:
                    queue.append((node.right, node.val))
                width -= 1
            if x_parent and y_parent and x_parent != y_parent:
                return True
            elif x_parent or y_parent:
                return False
        return False


solution = Solution()


root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
x = 4
y = 3
assert not solution.isCousins(root, x, y)

root = TreeNode(1, TreeNode(2, right=TreeNode(4)), TreeNode(3, right=TreeNode(5)))
x = 5
y = 4
assert solution.isCousins(root, x, y)

root = TreeNode(1, TreeNode(2, right=TreeNode(4)), TreeNode(3))
x = 2
y = 3
assert not solution.isCousins(root, x, y)
