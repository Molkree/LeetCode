# https://leetcode.com/problems/min-cost-climbing-stairs/
# 746. Min Cost Climbing Stairs


from functools import cache


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:  # noqa: N802
        @cache
        def min_cost(index: int) -> int:
            if index >= len(cost):
                return 0
            return cost[index] + min(min_cost(index + 1), min_cost(index + 2))

        return min(min_cost(0), min_cost(1))


solution = Solution()


cost = [10, 15, 20]
assert solution.minCostClimbingStairs(cost) == 15

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
assert solution.minCostClimbingStairs(cost) == 6
