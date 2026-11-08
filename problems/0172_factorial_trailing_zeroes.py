# https://leetcode.com/problems/factorial-trailing-zeroes/
# 172. Factorial Trailing Zeroes


class Solution:
    def trailingZeroes(self, n: int) -> int:  # noqa: N802
        zeroes = 0
        power_of_5 = 5
        while power_of_5 <= n:
            zeroes += n // power_of_5
            power_of_5 *= 5
        return zeroes


def factorial(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial(n - 1)


solution = Solution()

print(factorial(25))

n = 3
assert solution.trailingZeroes(n) == 0

n = 5
assert solution.trailingZeroes(n) == 1

n = 0
assert solution.trailingZeroes(n) == 0

n = 25
assert solution.trailingZeroes(n) == 6
