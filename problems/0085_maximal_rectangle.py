# https://leetcode.com/problems/maximal-rectangle/
# 85. Maximal Rectangle


class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:  # noqa: N802
        if not matrix:
            return 0
        matrix_height, matrix_width = len(matrix), len(matrix[0])
        left = [0] * matrix_width
        right = [matrix_width] * matrix_width
        height = [0] * matrix_width
        max_area = 0
        for row in range(matrix_height):
            cur_left, cur_right = 0, matrix_width
            for column in range(matrix_width):
                if matrix[row][column] == "1":
                    height[column] += 1
                    left[column] = max(left[column], cur_left)
                else:
                    height[column] = 0
                    left[column] = 0
                    cur_left = column + 1
            for column in range(matrix_width - 1, -1, -1):
                if matrix[row][column] == "1":
                    right[column] = min(right[column], cur_right)
                else:
                    right[column] = matrix_width
                    cur_right = column
            for column in range(matrix_width):
                max_area = max(
                    max_area, (right[column] - left[column]) * height[column]
                )
        return max_area


solution = Solution()


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
assert solution.maximalRectangle(matrix) == 6

matrix: list[list[str]] = []
assert solution.maximalRectangle(matrix) == 0

matrix = [["0"]]
assert solution.maximalRectangle(matrix) == 0

matrix = [["1"]]
assert solution.maximalRectangle(matrix) == 1

matrix = [["1"], ["1"]]
assert solution.maximalRectangle(matrix) == 2

matrix = [["1", "1"]]
assert solution.maximalRectangle(matrix) == 2

matrix = [["0", "0"]]
assert solution.maximalRectangle(matrix) == 0
