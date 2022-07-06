# https://leetcode.com/problems/fibonacci-number/
# 509. Fibonacci Number


from functools import cache


class Solution:
    @cache
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 2) + self.fib(n - 1)


solution = Solution()


n = 0
assert solution.fib(n) == 0

n = 1
assert solution.fib(n) == 1

n = 2
assert solution.fib(n) == 1

n = 3
assert solution.fib(n) == 2

n = 4
assert solution.fib(n) == 3

n = 20
assert solution.fib(n) == 6765
