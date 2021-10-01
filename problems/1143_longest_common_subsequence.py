# https://leetcode.com/problems/longest-common-subsequence/
# 1143. Longest Common Subsequence


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:  # noqa: N802
        text1_len = len(text1)
        text2_len = len(text2)
        lcs: list[list[int]] = [[0] * (text2_len + 1) for _ in range(text1_len)]
        for i in range(text1_len):
            for j in range(text2_len):
                if text1[i] == text2[j]:
                    lcs[i][j] = lcs[i - 1][j - 1] + 1
                else:
                    lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
        return max(item for sublist in lcs for item in sublist)


solution = Solution()

text1 = "oxcpqrsvwf"
text2 = "shmtulqrypy"
assert 2 == solution.longestCommonSubsequence(text1, text2)

text1 = "abcde"
text2 = "ace"
assert 3 == solution.longestCommonSubsequence(text1, text2)

text1 = "abc"
text2 = "abc"
assert 3 == solution.longestCommonSubsequence(text1, text2)

text1 = "abc"
text2 = "def"
assert 0 == solution.longestCommonSubsequence(text1, text2)
