# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# 1305. All Elements in Two Binary Search Trees


from __future__ import annotations

from heapq import merge


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(  # noqa: N802
        self, root1: TreeNode | None, root2: TreeNode | None
    ) -> list[int]:
        def visit(root: TreeNode | None, nodes: list[int]) -> None:
            if not root:
                return
            if root.left:
                visit(root.left, nodes)
            nodes.append(root.val)
            if root.right:
                visit(root.right, nodes)

        list1 = list[int]()
        list2 = list[int]()
        visit(root1, list1)
        visit(root2, list2)
        return list(merge(list1, list2))


solution = Solution()


root1 = TreeNode(2, TreeNode(1), TreeNode(4))
root2 = TreeNode(1, TreeNode(0), TreeNode(3))
assert solution.getAllElements(root1, root2) == [0, 1, 1, 2, 3, 4]

root1 = TreeNode(1, right=TreeNode(8))
root2 = TreeNode(8, TreeNode(1))
assert solution.getAllElements(root1, root2) == [1, 1, 8, 8]
