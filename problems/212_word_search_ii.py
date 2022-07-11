# https://leetcode.com/problems/word-search-ii/
# 212. Word Search II


from collections import Counter


class Trie:
    def __init__(self):
        self.children: dict[str, Trie] = {}
        self.is_word: bool = False

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.is_word

    def startsWith(self, prefix: str) -> bool:  # noqa: N802
        node = self
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True

    def delete(self, word: str) -> bool:
        def _delete(node: Trie, key: str, d: int) -> bool:
            if d == len(key):
                node.is_word = False
            else:
                char = key[d]
                if char in node.children and _delete(node.children[char], key, d + 1):
                    del node.children[char]
            return not node.is_word and len(node.children) == 0

        return _delete(self, word, 0)


class Solution:
    def find_words(
        self,
        board: list[list[str]],
        i: int,
        j: int,
        visited: set[tuple[int, int]],
        trie: Trie,
        prefix: str,
    ) -> set[str]:
        height = len(board)
        width = len(board[0])
        if i < 0 or i > height - 1 or j < 0 or j > width - 1 or (i, j) in visited:
            if trie.search(prefix):
                trie.delete(prefix)
                return {prefix}
            return set()
        result: set[str] = set()
        if trie.startsWith(prefix):
            if trie.search(prefix):
                result.add(prefix)
                trie.delete(prefix)
            visited.add((i, j))
            result |= (
                self.find_words(board, i - 1, j, visited, trie, prefix + board[i][j])
                | self.find_words(board, i + 1, j, visited, trie, prefix + board[i][j])
                | self.find_words(board, i, j - 1, visited, trie, prefix + board[i][j])
                | self.find_words(board, i, j + 1, visited, trie, prefix + board[i][j])
            )
            visited.remove((i, j))
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
        for i in range(height):
            for j in range(width):
                result |= self.find_words(board, i, j, set(), trie, prefix="")
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
