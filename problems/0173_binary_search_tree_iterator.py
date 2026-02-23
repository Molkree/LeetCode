# https://leetcode.com/problems/binary-search-tree-iterator/
# 173. Binary Search Tree Iterator


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode) -> None:
        self.stack = [root]
        while root.left:
            root = root.left
            self.stack.append(root)

    def next(self) -> int:
        node = self.stack.pop()
        result = node.val
        if node.right:
            self.stack.append(node.right)
            node = node.right
            while node.left:
                node = node.left
                self.stack.append(node)
        return result

    def hasNext(self) -> bool:  # noqa: N802
        return len(self.stack) > 0


root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
bst_iterator = BSTIterator(root)
assert bst_iterator.next() == 3
assert bst_iterator.next() == 7
assert bst_iterator.hasNext()
assert bst_iterator.next() == 9
assert bst_iterator.hasNext()
assert bst_iterator.next() == 15
assert bst_iterator.hasNext()
assert bst_iterator.next() == 20
assert not bst_iterator.hasNext()
