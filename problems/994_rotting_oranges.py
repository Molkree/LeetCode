# https://leetcode.com/problems/rotting-oranges/
# 994. Rotting Oranges


from collections import deque


class Solution:
    def rot_neighbor(self, grid: list[list[int]], i: int, j: int) -> bool:
        height = len(grid)
        width = len(grid[0])
        if 0 <= i < height and 0 <= j < width and grid[i][j] == 1:
            grid[i][j] = 2
            return True
        return False

    def orangesRotting(self, grid: list[list[int]]) -> int:  # noqa: N802
        queue: deque[tuple[int, int, int]] = deque()
        fresh_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh_count += 1
        if not fresh_count:
            return 0
        minute = -1
        while queue:
            i, j, minute = queue.popleft()
            if self.rot_neighbor(grid, i - 1, j):
                fresh_count -= 1
                queue.append((i - 1, j, minute + 1))
            if self.rot_neighbor(grid, i + 1, j):
                fresh_count -= 1
                queue.append((i + 1, j, minute + 1))
            if self.rot_neighbor(grid, i, j - 1):
                fresh_count -= 1
                queue.append((i, j - 1, minute + 1))
            if self.rot_neighbor(grid, i, j + 1):
                fresh_count -= 1
                queue.append((i, j + 1, minute + 1))
        return -1 if fresh_count else minute


solution = Solution()


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
assert solution.orangesRotting(grid) == 4

grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
assert solution.orangesRotting(grid) == -1

grid = [[0, 2]]
assert solution.orangesRotting(grid) == 0

grid = [[0]]
assert solution.orangesRotting(grid) == 0
