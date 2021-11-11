# https://leetcode.com/problems/trim-a-binary-search-tree/
# 669. Trim a Binary Search Tree


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(  # noqa: N802
        self, root: TreeNode | None, low: int, high: int
    ) -> TreeNode | None:
        if not root:
            return root
        # trim left
        if root.val == low:
            root.left = None
        elif root.val > low:
            node = root
            while node.left and node.left.val >= low:
                node = node.left
            if node.left:
                node.left = self.trimBST(node.left.right, low, high)
        else:
            root = self.trimBST(root.right, low, high)
            if not root:
                return root
        # trim right
        if root.val == high:
            root.right = None
        elif root.val < high:
            node = root
            while node.right and node.right.val <= high:
                node = node.right
            if node.right:
                node.right = self.trimBST(node.right.left, low, high)
        else:
            root = self.trimBST(root.left, low, high)
        return root


solution = Solution()


root = TreeNode(1, TreeNode(0), TreeNode(2))
low = 1
high = 2
solution.trimBST(root, low, high)

root = TreeNode(3, TreeNode(0, right=TreeNode(2, TreeNode(1))), TreeNode(4))
low = 1
high = 3
solution.trimBST(root, low, high)

root = TreeNode(1)
low = 1
high = 2
solution.trimBST(root, low, high)

root = TreeNode(1, right=TreeNode(2))
low = 1
high = 3
solution.trimBST(root, low, high)

root = TreeNode(1, right=TreeNode(2))
low = 2
high = 4
solution.trimBST(root, low, high)
