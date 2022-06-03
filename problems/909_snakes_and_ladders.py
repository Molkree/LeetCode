# https://leetcode.com/problems/snakes-and-ladders/
# 909. Snakes and Ladders


from collections import deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:  # noqa: N802
        board_len = len(board)
        min_moves = board_len**2
        queue = deque[tuple[int, int]]([(1, 0)])
        visited = set[int]([1])
        while queue:
            pos, moves = queue.popleft()
            if pos == board_len**2:
                min_moves = min(min_moves, moves)
                continue
            if moves > min_moves:
                continue
            for i in range(1, 7):
                next_pos = pos + i
                if next_pos > board_len**2:
                    continue
                row, column = divmod(next_pos - 1, board_len)
                if row % 2 != 0:
                    column = board_len - column - 1
                row = board_len - row - 1
                if board[row][column] != -1:
                    next_pos = board[row][column]
                if next_pos in visited:
                    continue
                queue.append((next_pos, moves + 1))
                visited.add(next_pos)
        return min_moves if min_moves != board_len**2 else -1


solution = Solution()


board = [
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1],
]
assert solution.snakesAndLadders(board) == 4

board = [[-1, -1], [-1, 3]]
assert solution.snakesAndLadders(board) == 1

board = [[1, 1, -1], [1, 1, 1], [-1, 1, 1]]
assert solution.snakesAndLadders(board) == -1
