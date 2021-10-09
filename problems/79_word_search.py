# https://leetcode.com/problems/word-search/
# 79. Word Search


class Solution:
    def word_starts_here(
        self,
        board: list[list[str]],
        word: str,
        i: int,
        j: int,
        visited: set[tuple[int, int]],
    ) -> bool:
        if not word:
            return True
        height = len(board)
        width = len(board[0])
        if i < 0 or i > height - 1 or j < 0 or j > width - 1 or (i, j) in visited:
            return False
        if board[i][j] == word[0]:
            visited.add((i, j))
            if (
                self.word_starts_here(board, word[1:], i - 1, j, visited)
                or self.word_starts_here(board, word[1:], i + 1, j, visited)
                or self.word_starts_here(board, word[1:], i, j - 1, visited)
                or self.word_starts_here(board, word[1:], i, j + 1, visited)
            ):
                return True
            visited.remove((i, j))
        return False

    def exist(self, board: list[list[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])
        for i in range(height):
            for j in range(width):
                if self.word_starts_here(board, word, i, j, set()):
                    return True
        return False


solution = Solution()

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
assert solution.exist(board, word)

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
assert solution.exist(board, word)

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
assert not solution.exist(board, word)

board = [["a"]]
word = "a"
assert solution.exist(board, word)
