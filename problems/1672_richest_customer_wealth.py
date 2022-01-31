# https://leetcode.com/problems/richest-customer-wealth/
# 1672. Richest Customer Wealth


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:  # noqa: N802
        return max(map(sum, accounts))


solution = Solution()


accounts = [[1, 2, 3], [3, 2, 1]]
assert solution.maximumWealth(accounts) == 6

accounts = [[1, 5], [7, 3], [3, 5]]
assert solution.maximumWealth(accounts) == 10

accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
assert solution.maximumWealth(accounts) == 17
