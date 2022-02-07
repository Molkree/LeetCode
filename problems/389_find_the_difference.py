# https://leetcode.com/problems/find-the-difference/
# 389. Find the Difference


from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:  # noqa: N802
        return (Counter(t) - Counter(s)).popitem()[0]


solution = Solution()


s = "abcd"
t = "abcde"
assert solution.findTheDifference(s, t) == "e"

s = ""
t = "y"
assert solution.findTheDifference(s, t) == "y"
