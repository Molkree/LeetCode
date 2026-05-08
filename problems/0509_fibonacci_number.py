# https://leetcode.com/problems/fibonacci-number/
# 509. Fibonacci Number


from functools import cache


@cache
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)


class Solution:
    def fib(self, n: int) -> int:
        return fib(n)


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
