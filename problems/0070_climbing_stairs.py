# https://leetcode.com/problems/climbing-stairs/
# 70. Climbing Stairs


from functools import cache


@cache
def climb_stairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb_stairs(n - 2) + climb_stairs(n - 1)


class Solution:
    def climbStairs(self, n: int) -> int:  # noqa: N802
        return climb_stairs(n)
