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
                    count += board[i + x][j + y]
            return count

        next_state = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = neighbour_count(i, j)
                if board[i][j] == 1:
                    if count in (2, 3):
                        next_state[i][j] = 1
                else:
                    if count == 3:
                        next_state[i][j] = 1
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = next_state[i][j]


solution = Solution()


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
solution.gameOfLife(board)
assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

board = [[1, 1], [1, 0]]
solution.gameOfLife(board)
assert board == [[1, 1], [1, 1]]
