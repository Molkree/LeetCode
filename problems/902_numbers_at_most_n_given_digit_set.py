# https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
# 902. Numbers At Most N Given Digit Set


class Solution:
    def atMostNGivenDigitSet(self, digits: list[str], n: int) -> int:  # noqa: N802
        str_n = str(n)
        n_len = len(str_n)
        dp = [0] * n_len + [1]
        for i in range(n_len - 1, -1, -1):
            for digit in digits:
                if digit < str_n[i]:
                    dp[i] += len(digits) ** (n_len - i - 1)
                elif digit == str_n[i]:
                    dp[i] += dp[i + 1]
                    break
                else:
                    break
        return dp[0] + sum(len(digits) ** i for i in range(1, n_len))


solution = Solution()


digits = ["1", "3", "5", "7"]
n = 100
assert solution.atMostNGivenDigitSet(digits, n) == 20

digits = ["1", "4", "9"]
n = 1000000000
assert solution.atMostNGivenDigitSet(digits, n) == 29523

digits = ["7"]
n = 8
assert solution.atMostNGivenDigitSet(digits, n) == 1

digits = ["1", "3", "5", "7"]
n = 333
assert solution.atMostNGivenDigitSet(digits, n) == 42
