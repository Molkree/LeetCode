# https://leetcode.com/problems/divide-two-integers/
# 29. Divide Two Integers


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_positive = dividend < 0 and divisor < 0 or dividend > 0 and divisor > 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        for shift in range(31, -1, -1):
            if (dividend >> shift) >= divisor:
                quotient += 1 << shift
                dividend -= divisor << shift
        if not is_positive:
            quotient = -quotient
        if quotient > 2**31 - 1:
            return 2**31 - 1
        return quotient


solution = Solution()


dividend = 10
divisor = 3
assert solution.divide(dividend, divisor) == 3

dividend = 7
divisor = -3
assert solution.divide(dividend, divisor) == -2

dividend = -2147483648
divisor = -1
assert solution.divide(dividend, divisor) == 2147483647
