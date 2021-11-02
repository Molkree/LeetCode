# https://leetcode.com/problems/unique-paths-iii/
# 980. Unique Paths III


class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:  # noqa: N802
        height, width = len(grid), len(grid[0])
        start_row, start_column = -1, -1
        empty_count = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    start_row, start_column = i, j
                elif grid[i][j] == 0:
                    empty_count += 1

        final_count = 0

        def dfs(row: int, column: int, empty_count: int) -> None:
            if not (
                0 <= row < height and 0 <= column < width and grid[row][column] >= 0
            ):
                return
            if grid[row][column] == 2:
                nonlocal final_count
                final_count += empty_count == -1
                return
            grid[row][column] = -2
            dfs(row + 1, column, empty_count - 1)
            dfs(row - 1, column, empty_count - 1)
            dfs(row, column + 1, empty_count - 1)
            dfs(row, column - 1, empty_count - 1)
            grid[row][column] = 0

        dfs(start_row, start_column, empty_count)
        return final_count


solution = Solution()


grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
assert solution.uniquePathsIII(grid) == 2

grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
assert solution.uniquePathsIII(grid) == 4

grid = [[0, 1], [2, 0]]
assert solution.uniquePathsIII(grid) == 0
