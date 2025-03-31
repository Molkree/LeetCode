# https://leetcode.com/problems/short-encoding-of-words/
# 820. Short Encoding of Words


class Trie:
    def __init__(self) -> None:
        self.children = dict[str, Trie]()
        self.is_word = False

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.is_word = True

    def is_leaf(self, word: str) -> bool:
        node = self
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return len(node.children) == 0


class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:  # noqa: N802
        # O(n ^ 2) time, where n is sum(len(word) for word in words)
        # for each word we try to remove all its suffixes
        # according to the task description, 1 <= words[i].length <= 7
        # which means we can just iterate over all word suffixes quickly
        # word_set = set(words)
        # for word in words:
        #     for i in range(1, len(word)):
        #         word_set.discard(word[i:])
        # return sum(len(word) + 1 for word in word_set)
        # O(n * l) time, where n is len(words) and l is an average word length
        # we add all words and then iterate over all words again
        trie = Trie()
        reversed_words = [word[::-1] for word in set(words)]
        for word in reversed_words:
            trie.insert(word)
        count = 0
        for word in reversed_words:
            if trie.is_leaf(word):
                count += len(word) + 1
        return count


solution = Solution()


words = ["time", "me", "bell"]
assert solution.minimumLengthEncoding(words) == 10

words = ["t"]
assert solution.minimumLengthEncoding(words) == 2

words = ["time", "time", "time", "time"]
assert solution.minimumLengthEncoding(words) == 5

words = ["time", "atime", "btime"]
assert solution.minimumLengthEncoding(words) == 12
