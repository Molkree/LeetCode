# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
# 1160. Find Words That Can Be Formed by Characters


from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:  # noqa: N802
        count = 0
        chars_counter = Counter(chars)
        for word in words:
            if not (Counter(word) - chars_counter):
                count += len(word)
        return count


solution = Solution()


words = ["cat", "bt", "hat", "tree"]
chars = "atach"
assert solution.countCharacters(words, chars) == 6

words = ["hello", "world", "leetcode"]
chars = "welldonehoneyr"
assert solution.countCharacters(words, chars) == 10
