# https://leetcode.com/problems/reverse-string/
# 344. Reverse String


class Solution:
    def reverseString(self, s: list[str]) -> None:  # noqa: N802
        s.reverse()
        # Reverse list using two pointers
        # length = len(s)
        # for i in range(length // 2):
        #     s[i], s[length - 1 - i] = s[length - 1 - i], s[i]
