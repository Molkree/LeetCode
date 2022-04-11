# https://leetcode.com/problems/shift-2d-grid/
# 1260. Shift 2D Grid


import itertools


class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:  # noqa: N802
        flat_grid = list(itertools.chain.from_iterable(grid))
        k %= len(flat_grid)
        new_flat_grid = flat_grid[-k:] + flat_grid[:-k]
        return [
            new_flat_grid[i : i + len(grid[0])]
            for i in range(0, len(new_flat_grid), len(grid[0]))
        ]


solution = Solution()


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 1
assert solution.shiftGrid(grid, k) == [[9, 1, 2], [3, 4, 5], [6, 7, 8]]

grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
k = 4
assert solution.shiftGrid(grid, k) == [
    [12, 0, 21, 13],
    [3, 8, 1, 9],
    [19, 7, 2, 5],
    [4, 6, 11, 10],
]

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 9
assert solution.shiftGrid(grid, k) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

grid = [[1], [2], [3], [4], [7], [6], [5]]
k = 23
assert solution.shiftGrid(grid, k) == [[6], [5], [1], [2], [3], [4], [7]]
