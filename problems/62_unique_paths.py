# https://leetcode.com/problems/unique-paths/
# 62. Unique Paths


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:  # noqa: N802
        paths = [[0] * n] * m
        for i in range(m):
            paths[i][0] = 1
        for j in range(n):
            paths[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
        return paths[-1][-1]


solution = Solution()


m = 3
n = 7
assert solution.uniquePaths(m, n) == 28

m = 3
n = 2
assert solution.uniquePaths(m, n) == 3

m = 7
n = 3
assert solution.uniquePaths(m, n) == 28

m = 3
n = 3
assert solution.uniquePaths(m, n) == 6

m = 23
n = 12
assert solution.uniquePaths(m, n) == 193536720
