# https://leetcode.com/problems/unique-paths-ii/
# 63. Unique Paths II


class Solution:
    def uniquePathsWithObstacles(  # noqa: N802
        self, obstacle_grid: list[list[int]]
    ) -> int:
        row = [1] * len(obstacle_grid)
        for j in range(len(obstacle_grid[0])):
            if obstacle_grid[0][j] == 1:
                for ind in range(j, len(row)):
                    row[ind] = 0
        return -1


solution = Solution()


obstacle_grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
assert solution.uniquePathsWithObstacles(obstacle_grid) == 2

obstacle_grid = [[0, 1], [0, 0]]
assert solution.uniquePathsWithObstacles(obstacle_grid) == 1
