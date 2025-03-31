# https://leetcode.com/problems/spiral-matrix-ii/
# 59. Spiral Matrix II


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:  # noqa: N802
        matrix = [[0] * n for _ in range(n)]
        num = 1
        for layer in range(n // 2 + 1):
            for i in range(layer, n - layer):
                matrix[layer][i] = num
                num += 1
            for i in range(layer + 1, n - layer):
                matrix[i][n - layer - 1] = num
                num += 1
            for i in range(n - layer - 2, layer - 1, -1):
                matrix[n - layer - 1][i] = num
                num += 1
            for i in range(n - layer - 2, layer, -1):
                matrix[i][layer] = num
                num += 1
        return matrix


solution = Solution()


n = 1
assert solution.generateMatrix(n) == [[1]]

n = 2
assert solution.generateMatrix(n) == [[1, 2], [4, 3]]

n = 3
assert solution.generateMatrix(n) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

n = 4
assert solution.generateMatrix(n) == [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7],
]

n = 5
assert solution.generateMatrix(n) == [
    [1, 2, 3, 4, 5],
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9],
]

n = 6
assert solution.generateMatrix(n) == [
    [1, 2, 3, 4, 5, 6],
    [20, 21, 22, 23, 24, 7],
    [19, 32, 33, 34, 25, 8],
    [18, 31, 36, 35, 26, 9],
    [17, 30, 29, 28, 27, 10],
    [16, 15, 14, 13, 12, 11],
]
