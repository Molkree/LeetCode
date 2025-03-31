# https://leetcode.com/problems/interleaving-string/
# 97. Interleaving String


from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:  # noqa: N802
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def dfs(s1_index: int, s2_index: int) -> bool:
            if s1_index == len(s1) and s2_index == len(s2):
                return True
            if s1_index == len(s1):
                return s2[s2_index:] == s3[s1_index + s2_index :]
            if s2_index == len(s2):
                return s1[s1_index:] == s3[s1_index + s2_index :]
            if s1[s1_index] == s3[s1_index + s2_index] and dfs(s1_index + 1, s2_index):
                return True
            if s2[s2_index] == s3[s1_index + s2_index] and dfs(s1_index, s2_index + 1):
                return True
            return False

        return dfs(0, 0)


solution = Solution()


s1 = "a"
s2 = "ab"
s3 = "aba"
assert solution.isInterleave(s1, s2, s3)

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
assert solution.isInterleave(s1, s2, s3)

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
assert not solution.isInterleave(s1, s2, s3)

s1 = ""
s2 = ""
s3 = ""
assert solution.isInterleave(s1, s2, s3)

s1 = ""
s2 = ""
s3 = "a"
assert not solution.isInterleave(s1, s2, s3)

s1 = "aa"
s2 = "ab"
s3 = "aaba"
assert solution.isInterleave(s1, s2, s3)
