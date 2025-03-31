# https://leetcode.com/problems/subtree-of-another-tree/
# 572. Subtree of Another Tree


from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # chunky slow solution
    # from collections import deque
    # def isSubtree(self, root: TreeNode, sub_root: TreeNode) -> bool:  # noqa: N802
    #     queue: deque[TreeNode] = deque()
    #     queue.append(root)
    #     while queue:
    #         node = queue.popleft()
    #         if node.val == sub_root.val:
    #             sub_queue: deque[TreeNode] = deque()
    #             tmp_queue: deque[TreeNode] = deque()
    #             sub_queue.append(sub_root)
    #             tmp_queue.append(node)
    #             while sub_queue:
    #                 sub_node = sub_queue.popleft()
    #                 tmp_node = tmp_queue.popleft()
    #                 if (
    #                     sub_node.val != tmp_node.val
    #                     or bool(sub_node.left) ^ bool(tmp_node.left)
    #                     or bool(sub_node.right) ^ bool(tmp_node.right)
    #                 ):
    #                     break
    #                 if sub_node.left:
    #                     sub_queue.append(sub_node.left)
    #                 if sub_node.right:
    #                     sub_queue.append(sub_node.right)
    #                 if tmp_node.left:
    #                     tmp_queue.append(tmp_node.left)
    #                 if tmp_node.right:
    #                     tmp_queue.append(tmp_node.right)
    #                 if len(sub_queue) != len(tmp_queue):
    #                     break
    #                 if not sub_queue and not tmp_queue and sub_node.val == tmp_node.val:
    #                     return True
    #         if node.left:
    #             queue.append(node.left)
    #         if node.right:
    #             queue.append(node.right)
    #     return False

    # faster solution
    def isSubtree(  # noqa: N802
        self, root: TreeNode | None, sub_root: TreeNode | None
    ) -> bool:
        if not root:
            return False

        def is_same(root: TreeNode | None, sub_root: TreeNode | None) -> bool:
            if not root or not sub_root:
                return root == sub_root
            if root.val != sub_root.val:
                return False
            return is_same(root.left, sub_root.left) and is_same(
                root.right, sub_root.right
            )

        if is_same(root, sub_root):
            return True
        return self.isSubtree(root.left, sub_root) or self.isSubtree(
            root.right, sub_root
        )


solution = Solution()


root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
sub_root = TreeNode(4, TreeNode(1), TreeNode(2))
assert solution.isSubtree(root, sub_root)

root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
sub_root = TreeNode(4, TreeNode(1), TreeNode(2))
assert not solution.isSubtree(root, sub_root)

root = TreeNode(
    -1,
    TreeNode(-4, TreeNode(-6, right=TreeNode(-5)), TreeNode(-2)),
    TreeNode(8, TreeNode(3, TreeNode(0), TreeNode(7)), TreeNode(9)),
)
sub_root = TreeNode(3, TreeNode(0), TreeNode(5848))
assert not solution.isSubtree(root, sub_root)

root = TreeNode(
    -9,
    right=TreeNode(
        3,
        TreeNode(2, TreeNode(-1, TreeNode(-4, TreeNode(-5)), TreeNode(0))),
        TreeNode(8, TreeNode(7, TreeNode(6))),
    ),
)
sub_root = TreeNode(-1, TreeNode(1515, TreeNode(-5)), TreeNode(0))
assert not solution.isSubtree(root, sub_root)

root = TreeNode(4, TreeNode(5))
sub_root = TreeNode(4, right=TreeNode(5))
assert not solution.isSubtree(root, sub_root)
