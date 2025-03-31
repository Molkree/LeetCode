# https://leetcode.com/problems/isomorphic-strings/
# 205. Isomorphic Strings


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:  # noqa: N802
        if len(s) != len(t):
            return False
        s2t: dict[str, str] = {}
        t2s: dict[str, str] = {}
        for i, char in enumerate(s):
            if s2t.setdefault(char, t[i]) != t[i] or t2s.setdefault(t[i], char) != char:
                return False
        return True


solution = Solution()


s = "egg"
t = "add"
assert solution.isIsomorphic(s, t)

s = "foo"
t = "bar"
assert not solution.isIsomorphic(s, t)

s = "paper"
t = "title"
assert solution.isIsomorphic(s, t)

s = "badc"
t = "baba"
assert not solution.isIsomorphic(s, t)
