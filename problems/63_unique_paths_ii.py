# https://leetcode.com/problems/unique-paths-ii/
# 63. Unique Paths II


class Solution:
    def uniquePathsWithObstacles(  # noqa: N802
        self, obstacle_grid: list[list[int]]
    ) -> int:
        m, n = len(obstacle_grid), len(obstacle_grid[0])
        row = [1] * n
        for j in range(n):
            if obstacle_grid[0][j] == 1:
                for ind in range(j, len(row)):
                    row[ind] = 0
                break
        for i in range(1, m):
            for j in range(n):
                if obstacle_grid[i][j] == 1:
                    row[j] = 0
                elif j > 0:
                    row[j] += row[j - 1]
        return row[-1]


solution = Solution()


obstacle_grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
assert solution.uniquePathsWithObstacles(obstacle_grid) == 2

obstacle_grid = [[0, 1], [0, 0]]
assert solution.uniquePathsWithObstacles(obstacle_grid) == 1

obstacle_grid = [[0, 1]]
assert solution.uniquePathsWithObstacles(obstacle_grid) == 0

obstacle_grid = [[0], [1]]
assert solution.uniquePathsWithObstacles(obstacle_grid) == 0

obstacle_grid = [[1, 0]]
assert solution.uniquePathsWithObstacles(obstacle_grid) == 0
