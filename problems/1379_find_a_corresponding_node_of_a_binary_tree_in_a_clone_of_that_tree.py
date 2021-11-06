# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(  # noqa: N802
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        stack = [cloned]
        while stack:
            node = stack.pop()
            if node.val == target.val:
                return node
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return cloned


solution = Solution()
