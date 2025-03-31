# https://leetcode.com/problems/burst-balloons/
# 312. Burst Balloons


class Solution:
    def maxCoins(self, nums: list[int]) -> int:  # noqa: N802
        nums = [1] + [num for num in nums if num > 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                for i in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right],
                    )
        return dp[0][-1]


solution = Solution()


nums = [3, 1, 5, 8]
assert solution.maxCoins(nums) == 167

nums = [1, 5]
assert solution.maxCoins(nums) == 10
