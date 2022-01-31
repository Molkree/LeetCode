# https://leetcode.com/problems/nth-magical-number/
# 878. Nth Magical Number


import math


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:  # noqa: N802
        modulo = 10**9 + 7
        lcm = math.lcm(a, b)
        m = lcm // a + lcm // b - 1
        q, r = divmod(n, m)
        if r == 0:
            return q * lcm % modulo
        nums = [a, b]
        for _ in range(r - 1):
            if nums[0] < nums[1]:
                nums[0] += a
            else:
                nums[1] += b
        return (q * lcm + min(nums)) % modulo


solution = Solution()


n = 1
a = 2
b = 3
assert solution.nthMagicalNumber(n, a, b) == 2

n = 4
a = 2
b = 3
assert solution.nthMagicalNumber(n, a, b) == 6

n = 5
a = 2
b = 4
assert solution.nthMagicalNumber(n, a, b) == 10

n = 3
a = 6
b = 4
assert solution.nthMagicalNumber(n, a, b) == 8
