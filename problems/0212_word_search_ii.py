# https://leetcode.com/problems/word-search-ii/
# 212. Word Search II


from collections import Counter


class Trie:
    def __init__(self) -> None:
        self.children: dict[str, Trie] = {}
        self.is_word: bool = False

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.is_word = True


class Solution:
    def find_words(
        self,
        board: list[list[str]],
        row: int,
        column: int,
        visited: set[tuple[int, int]],
        trie: Trie,
        prefix: str,
    ) -> set[str]:
        prefix += board[row][column]
        parent_trie = trie
        trie = trie.children[board[row][column]]
        result = set[str]()
        if trie.is_word:
            result = {prefix}
            trie.is_word = False
            if len(trie.children) == 0:
                del parent_trie.children[board[row][column]]
                return result
        visited.add((row, column))
        for new_row, new_column in (
            (row, column - 1),
            (row, column + 1),
            (row - 1, column),
            (row + 1, column),
        ):
            if (
                (new_row, new_column) not in visited
                and 0 <= new_row < len(board)
                and 0 <= new_column < len(board[0])
                and board[new_row][new_column] in trie.children
            ):
                result |= self.find_words(
                    board,
                    new_row,
                    new_column,
                    visited,
                    trie,
                    prefix,
                )
        visited.remove((row, column))
        return result

    def findWords(  # noqa: N802
        self, board: list[list[str]], words: list[str]
    ) -> list[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        height = len(board)
        width = len(board[0])
        result: set[str] = set()
        for row in range(height):
            for column in range(width):
                if board[row][column] in trie.children:
                    result |= self.find_words(board, row, column, set(), trie, "")
                if len(result) == len(words):
                    break
        return list(result)


solution = Solution()

board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]
words = ["oath", "pea", "eat", "rain"]
assert Counter(["eat", "oath"]) == Counter(solution.findWords(board, words))

board = [["a"]]
words = ["a"]
assert Counter(["a"]) == Counter(solution.findWords(board, words))

board = [["a", "b"], ["c", "d"]]
words = ["abcb"]
assert Counter([]) == Counter(solution.findWords(board, words))

board = [
    ["o", "a", "b", "n"],
    ["o", "t", "a", "e"],
    ["a", "h", "k", "r"],
    ["a", "f", "l", "v"],
]
words = ["oa", "oaa"]
assert Counter(["oa", "oaa"]) == Counter(solution.findWords(board, words))

board = [["a", "b", "c", "e"], ["x", "x", "c", "d"], ["x", "x", "b", "a"]]
words = ["abc", "abcd"]
assert Counter(["abc", "abcd"]) == Counter(solution.findWords(board, words))
