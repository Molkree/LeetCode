# https://leetcode.com/problems/maximal-square/
# 221. Maximal Square


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:  # noqa: N802
        matrix_height, matrix_width = len(matrix), len(matrix[0])
        # Naive brute force solution but passes tests

        # def all_ones(start_row: int, start_column: int, width: int) -> bool:
        #     for row in range(start_row, start_row + width):
        #         for column in range(start_column, start_column + width):
        #             if matrix[row][column] == "0":
        #                 return False
        #     return True

        # max_width = min(matrix_height, matrix_width)
        # for width in range(max_width, 0, -1):
        #     for row in range(matrix_height - width + 1):
        #         for column in range(matrix_width - width + 1):
        #             if all_ones(row, column, width):
        #                 return width * width
        # return 0

        # Smarty pants DP solution
        # dp = [[0] * (matrix_width + 1) for _ in range(matrix_height + 1)]
        # max_width = 0
        # for row in range(1, matrix_height + 1):
        #     for column in range(1, matrix_width + 1):
        #         if matrix[row - 1][column - 1] == "1":
        #             dp[row][column] = (
        #                 min(
        #                     dp[row - 1][column],
        #                     dp[row][column - 1],
        #                     dp[row - 1][column - 1],
        #                 )
        #                 + 1
        #             )
        #             max_width = max(max_width, dp[row][column])
        # return max_width * max_width

        # Even smarter 1D DP solution
        dp = [0] * (matrix_width + 1)
        max_width, prev = 0, 0
        for row in range(1, matrix_height + 1):
            for column in range(1, matrix_width + 1):
                temp = dp[column]
                if matrix[row - 1][column - 1] == "1":
                    dp[column] = min(dp[column], dp[column - 1], prev) + 1
                    max_width = max(max_width, dp[column])
                else:
                    dp[column] = 0
                prev = temp
        return max_width * max_width


solution = Solution()


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
assert solution.maximalSquare(matrix) == 4

matrix = [["0", "1"], ["1", "0"]]
assert solution.maximalSquare(matrix) == 1

matrix = [["0"]]
assert solution.maximalSquare(matrix) == 0
