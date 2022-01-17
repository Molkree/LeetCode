# https://leetcode.com/problems/word-pattern/
# 290. Word Pattern


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:  # noqa: N802
        words = s.split()
        if len(pattern) != len(words):
            return False
        mapping = dict[str, str]()
        for ind, char in enumerate(pattern):
            if char not in mapping:
                mapping[char] = words[ind]
            elif mapping[char] != words[ind]:
                return False
        return len(mapping.values()) == len(set(mapping.values()))


solution = Solution()


pattern = "abba"
s = "dog cat cat dog"
assert solution.wordPattern(pattern, s)

pattern = "abba"
s = "dog cat cat fish"
assert not solution.wordPattern(pattern, s)

pattern = "aaaa"
s = "dog cat cat dog"
assert not solution.wordPattern(pattern, s)

pattern = "abba"
s = "dog cat cat"
assert not solution.wordPattern(pattern, s)

pattern = "abba"
s = "dog dog dog dog"
assert not solution.wordPattern(pattern, s)

pattern = "aaa"
s = "aa aa aa aa"
assert not solution.wordPattern(pattern, s)
