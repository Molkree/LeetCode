# https://leetcode.com/problems/spiral-matrix/
# 54. Spiral Matrix


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:  # noqa: N802
        if not matrix:
            return []
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            return [row[0] for row in matrix]
        height = len(matrix)
        width = len(matrix[0])
        res = list[int]()
        for layer in range((min(height, width) + 1) // 2):
            for i in range(layer, width - layer):
                res.append(matrix[layer][i])
            for i in range(layer + 1, height - layer):
                res.append(matrix[i][width - layer - 1])
            if layer < height // 2 or height % 2 == 0:
                for i in range(width - layer - 2, layer - 1, -1):
                    res.append(matrix[height - layer - 1][i])
            if layer < width // 2 or width % 2 == 0:
                for i in range(height - layer - 2, layer, -1):
                    res.append(matrix[i][layer])
        return res


solution = Solution()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
assert solution.spiralOrder(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
assert solution.spiralOrder(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

matrix = [[2, 5, 8], [4, 0, -1]]
assert solution.spiralOrder(matrix) == [2, 5, 8, -1, 0, 4]
