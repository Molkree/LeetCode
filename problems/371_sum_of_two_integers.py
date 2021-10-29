# https://leetcode.com/problems/sum-of-two-integers/
# 371. Sum of Two Integers


class Solution:
    def getSum(self, a: int, b: int) -> int:  # noqa: N802
        mask = 0xFFFFFFFF
        while (b & mask) > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return (a & mask) if b > 0 else a


solution = Solution()


a = 1
b = 2
assert solution.getSum(a, b) == 3

a = 2
b = 3
assert solution.getSum(a, b) == 5

a = -2
b = -3
assert solution.getSum(a, b) == -5

a = -1
b = 1
assert solution.getSum(a, b) == 0

a = -1
b = 0
assert solution.getSum(a, b) == -1
