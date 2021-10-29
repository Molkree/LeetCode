# https://leetcode.com/problems/valid-anagram/
# 242. Valid Anagram


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  # noqa: N802
        return Counter(s) == Counter(t)


solution = Solution()


s = "anagram"
t = "nagaram"
assert solution.isAnagram(s, t)

s = "rat"
t = "car"
assert not solution.isAnagram(s, t)
