# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/
# 828. Count Unique Characters of All Substrings of a Given String


from collections import defaultdict


class Solution:
    def uniqueLetterString(self, s: str) -> int:  # noqa: N802
        index = defaultdict[str, tuple[int, int]](lambda: (-1, -1))
        result = 0
        for ind, char in enumerate(s):
            prevprev, prev = index[char]
            result += (ind - prev) * (prev - prevprev)
            index[char] = prev, ind
        for char in index:
            prevprev, prev = index[char]
            result += (len(s) - prev) * (prev - prevprev)
        return result


solution = Solution()


s = "ABC"
assert solution.uniqueLetterString(s) == 10

s = "ABA"
assert solution.uniqueLetterString(s) == 8

s = "LEETCODE"
assert solution.uniqueLetterString(s) == 92
