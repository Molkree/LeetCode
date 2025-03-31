# https://leetcode.com/problems/surrounded-regions/
# 130. Surrounded Regions


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        height, width = len(board), len(board[0])
        queue = (
            [(height - 1, j) for j in range(width)]
            + [(0, j) for j in range(width)]
            + [(i, 0) for i in range(height)]
            + [(i, width - 1) for i in range(height)]
        )
        while queue:
            i, j = queue.pop()
            if 0 <= i < height and 0 <= j < width and board[i][j] == "O":
                board[i][j] = "S"
                queue += [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for i in range(height):
            for j in range(width):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"


solution = Solution()


board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]
solution.solve(board)
assert board == [
    ["X", "X", "X", "X"],
    ["X", "X", "X", "X"],
    ["X", "X", "X", "X"],
    ["X", "O", "X", "X"],
]

board = [["X"]]
solution.solve(board)
assert board == [["X"]]
