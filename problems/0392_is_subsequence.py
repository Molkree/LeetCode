# https://leetcode.com/problems/is-subsequence/
# 392. Is Subsequence


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:  # noqa: N802
        # smart solution
        iterator = iter(t)
        return all(char in iterator for char in s)
        # my straightforward solution
        if not s:
            return True
        start = 0
        for s_index, s_char in enumerate(s):
            found = False
            for t_index, t_char in enumerate(t[start:], start):
                if s_char == t_char:
                    if s_index == len(s) - 1:
                        return True
                    start = t_index + 1
                    found = True
                    break
            if not found:
                return False
        return False


solution = Solution()


s = "abc"
t = "ahbgdc"
assert solution.isSubsequence(s, t)

s = "axc"
t = "ahbgdc"
assert not solution.isSubsequence(s, t)

s = ""
t = ""
assert solution.isSubsequence(s, t)

s = "aaa"
t = "baa"
assert not solution.isSubsequence(s, t)
