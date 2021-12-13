# https://leetcode.com/problems/consecutive-characters/
# 1446. Consecutive Characters


class Solution:
    def maxPower(self, s: str) -> int:  # noqa: N802
        max_count = 1
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        return max(max_count, count)


solution = Solution()


s = "leetcode"
assert solution.maxPower(s) == 2

s = "l"
assert solution.maxPower(s) == 1

s = "abbcccddddeeeeedcba"
assert solution.maxPower(s) == 5

s = "triplepillooooow"
assert solution.maxPower(s) == 5

s = "hooraaaaaaaaaaay"
assert solution.maxPower(s) == 11

s = "tourist"
assert solution.maxPower(s) == 1

s = "cc"
assert solution.maxPower(s) == 2
