# https://leetcode.com/problems/unique-binary-search-trees/
# 96. Unique Binary Search Trees


from functools import cache


@cache
def num_trees(n: int) -> int:
    if n < 2:
        return 1
    result = 0
    for i in range(n):
        left = num_trees(n - 1 - i)
        right = num_trees(i)
        result += left * right
    return result


class Solution:
    def numTrees(self, n: int) -> int:  # noqa: N802
        return num_trees(n)


solution = Solution()


n = 1
assert solution.numTrees(n) == 1

n = 2
assert solution.numTrees(n) == 2

n = 3
assert solution.numTrees(n) == 5

n = 4
assert solution.numTrees(n) == 14

n = 5
assert solution.numTrees(n) == 42

n = 19
assert solution.numTrees(n) == 1767263190
