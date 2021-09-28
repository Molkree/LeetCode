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
assert 0 == solution.trailingZeroes(n)

n = 5
assert 1 == solution.trailingZeroes(n)

n = 0
assert 0 == solution.trailingZeroes(n)

n = 25
assert 6 == solution.trailingZeroes(n)
