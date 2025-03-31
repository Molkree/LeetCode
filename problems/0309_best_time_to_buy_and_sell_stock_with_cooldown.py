# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# 309. Best Time to Buy and Sell Stock with Cooldown


class Solution:
    def maxProfit(self, prices: list[int]) -> int:  # noqa: N802
        buy = -prices[0]
        sell = 0
        prev_sell = 0
        for price in prices:
            prev_buy = buy
            buy = max(prev_buy, prev_sell - price)
            prev_sell = sell
            sell = max(prev_sell, prev_buy + price)
        return sell


solution = Solution()


prices = [1, 2, 3, 0, 2]
assert 3 == solution.maxProfit(prices)

prices = [1]
assert 0 == solution.maxProfit(prices)
