# https://leetcode.com/problems/set-matrix-zeroes/
# 73. Set Matrix Zeroes


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:  # noqa: N802
        # O(n + m) memory
        # rows, columns = set[int](), set[int]()
        # for row_index, row in enumerate(matrix):
        #     for column_index, value in enumerate(row):
        #         if value == 0:
        #             rows.add(row_index)
        #             columns.add(column_index)
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if i in rows or j in columns:
        #             matrix[i][j] = 0
        # O(1) memory
        zero_first_col = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                zero_first_col = True
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if zero_first_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0


solution = Solution()


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
solution.setZeroes(matrix)
assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
solution.setZeroes(matrix)
assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
