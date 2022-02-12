# https://leetcode.com/problems/word-ladder/
# 127. Word Ladder


from collections import deque


class Solution:
    def ladderLength(  # noqa: N802
        self, begin_word: str, end_word: str, word_list: list[str]
    ) -> int:
        word_set = set(word_list)
        char_set = {char for word in word_set for char in word}
        queue = deque[tuple[str, int]]([(begin_word, 1)])
        while queue:
            word, length = queue.popleft()
            if word == end_word:
                return length
            for i in range(len(word)):
                for char in char_set:
                    next_word = word[:i] + char + word[i + 1 :]
                    if next_word in word_set:
                        queue.append((next_word, length + 1))
                        word_set.remove(next_word)
        return 0


solution = Solution()


begin_word = "hit"
end_word = "cog"
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
assert solution.ladderLength(begin_word, end_word, word_list) == 5

begin_word = "hit"
end_word = "cog"
word_list = ["hot", "dot", "dog", "lot", "log"]
assert solution.ladderLength(begin_word, end_word, word_list) == 0
