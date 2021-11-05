# https://leetcode.com/problems/arranging-coins/
# 441. Arranging Coins


class Solution:
    def arrangeCoins(self, n: int) -> int:  # noqa: N802
        coins_per_row = 1
        while n > 0:
            coins_per_row += 1
            n -= coins_per_row
        return coins_per_row - 1


solution = Solution()


n = 5
assert solution.arrangeCoins(n) == 2

n = 8
assert solution.arrangeCoins(n) == 3

n = 1
assert solution.arrangeCoins(n) == 1

n = 3
assert solution.arrangeCoins(n) == 2
