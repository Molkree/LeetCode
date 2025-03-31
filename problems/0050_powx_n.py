# https://leetcode.com/problems/powx-n/
# 50. Pow(x, n)


from functools import cache


class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:  # noqa: N802
        if not n:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        return x * self.myPow(x * x, n // 2) if n % 2 else self.myPow(x * x, n // 2)
        return x**n


solution = Solution()
eps = 0.000001


x = 2.00000
n = 10
assert abs(solution.myPow(x, n) - 1024.00000) < eps

x = 2.10000
n = 3
assert abs(solution.myPow(x, n) - 9.26100) < eps

x = 2.00000
n = -2
assert abs(solution.myPow(x, n) - 0.25000) < eps
