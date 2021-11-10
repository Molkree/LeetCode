# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# 122. Best Time to Buy and Sell Stock II


class Solution:
    def maxProfit(self, prices: list[int]) -> int:  # noqa: N802
        profit = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                profit += prices[i] - prices[i - 1]
        return profit


solution = Solution()


prices = [7, 1, 5, 2, 5, 4]
assert solution.maxProfit(prices) == 7

prices = [7, 1, 5, 3, 6, 4, 1, 2]
assert solution.maxProfit(prices) == 8

prices = [1, 2, 3, 4, 5]
assert solution.maxProfit(prices) == 4

prices = [7, 6, 4, 3, 1]
assert solution.maxProfit(prices) == 0
