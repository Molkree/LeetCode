# https://leetcode.com/problems/game-of-life/
# 289. Game of Life


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:  # noqa: N802
        def neighbour_count(i: int, j: int) -> int:
            count = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    if i + x < 0 or i + x >= len(board):
                        continue
                    if j + y < 0 or j + y >= len(board[0]):
                        continue
                    count += board[i + x][j + y] & 1
            return count

        for i in range(len(board)):
            for j in range(len(board[0])):
                count = neighbour_count(i, j)
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = -1
                else:
                    if count == 3:
                        board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0


solution = Solution()


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
solution.gameOfLife(board)
assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

board = [[1, 1], [1, 0]]
solution.gameOfLife(board)
assert board == [[1, 1], [1, 1]]
