# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
# 2160. Minimum Sum of Four Digit Number After Splitting Digits


class Solution:
    def minimumSum(self, num: int) -> int:  # noqa: N802
        digits = sorted(map(int, str(num)))
        return digits[0] * 10 + digits[1] * 10 + digits[2] + digits[3]


solution = Solution()


num = 2932
assert solution.minimumSum(num) == 52

num = 4009
assert solution.minimumSum(num) == 13
