# https://leetcode.com/problems/cherry-pickup-ii/
# 1463. Cherry Pickup II


from functools import cache


class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:  # noqa: N802
        height = len(grid)
        width = len(grid[0])

        @cache
        def pickup(row: int, column_1: int, column_2: int) -> int:
            if not 0 <= column_1 < width or not 0 <= column_2 < width:
                return -1
            result = grid[row][column_1]
            if column_1 != column_2:
                result += grid[row][column_2]
            if row < height - 1:
                result += max(
                    pickup(row + 1, new_column_1, new_column_2)
                    for new_column_1 in (column_1 - 1, column_1, column_1 + 1)
                    for new_column_2 in (column_2 - 1, column_2, column_2 + 1)
                )
            return result

        return pickup(0, 0, width - 1)


solution = Solution()


grid = [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]
assert solution.cherryPickup(grid) == 24

grid = [
    [1, 0, 0, 0, 0, 0, 1],
    [2, 0, 0, 0, 0, 3, 0],
    [2, 0, 9, 0, 0, 0, 0],
    [0, 3, 0, 5, 4, 0, 0],
    [1, 0, 2, 3, 0, 0, 6],
]
assert solution.cherryPickup(grid) == 28
