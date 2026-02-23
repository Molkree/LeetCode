# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
# 559. Maximum Depth of N-ary Tree


class Node:
    def __init__(self, val: int, children: list[Node]):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node | None) -> int:  # noqa: N802
        # Slow version
        # max_depth = 1
        # stack: list[tuple[Node, int]] = [(root, 1)]
        # while stack:
        #     node, depth = stack.pop()
        #     max_depth = max(max_depth, depth)
        #     if node.children:
        #         stack += [(child, depth + 1) for child in node.children]
        # return max_depth

        # Faster version
        if not root:
            return 0

        depths: list[int] = []

        def dfs(root: Node, depth: int) -> None:
            for child in root.children:
                dfs(child, depth + 1)
            depths.append(depth)

        dfs(root, 1)
        return max(depths)
