# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 121. Best Time to Buy and Sell Stock


class Solution:
    def maxProfit(self, prices: list[int]) -> int:  # noqa: N802
        buy = 10**5 + 1
        sell = 0
        for price in prices:
            buy = min(buy, price)
            sell = max(sell, price - buy)
        return sell


solution = Solution()


prices = [7, 1, 5, 3, 6, 4]
assert solution.maxProfit(prices) == 5

prices = [7, 6, 4, 3, 1]
assert solution.maxProfit(prices) == 0
