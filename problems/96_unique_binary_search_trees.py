# https://leetcode.com/problems/unique-binary-search-trees/
# 96. Unique Binary Search Trees


from functools import cache


class Solution:
    @cache
    def numTrees(self, n: int) -> int:  # noqa: N802
        if n < 2:
            return 1
        result = 0
        for i in range(n):
            left = self.numTrees(n - 1 - i)
            right = self.numTrees(i)
            result += left * right
        return result


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
