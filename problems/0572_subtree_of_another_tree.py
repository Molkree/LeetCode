# https://leetcode.com/problems/subtree-of-another-tree/
# 572. Subtree of Another Tree


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
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
