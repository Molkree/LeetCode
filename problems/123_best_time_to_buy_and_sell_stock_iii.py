# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# 123. Best Time to Buy and Sell Stock III


class Solution:
    def maxProfit(self, prices: list[int]) -> int:  # noqa: N802
        first_buy = 10 ** 5 + 1
        second_buy = 10 ** 5 + 1
        first_sell = 0
        second_sell = 0
        for i in range(len(prices)):
            first_buy = min(first_buy, prices[i])
            first_sell = max(first_sell, prices[i] - first_buy)
            second_buy = min(second_buy, prices[i] - first_sell)
            second_sell = max(second_sell, prices[i] - second_buy)
        return second_sell


solution = Solution()


prices = [3, 3, 5, 0, 0, 3, 1, 4]
assert 6 == solution.maxProfit(prices)

prices = [1, 2, 3, 4, 5]
assert 4 == solution.maxProfit(prices)

prices = [7, 6, 4, 3, 1]
assert 0 == solution.maxProfit(prices)

prices = [1]
assert 0 == solution.maxProfit(prices)
