# https://leetcode.com/problems/partition-equal-subset-sum/
# 416. Partition Equal Subset Sum


class Solution:
    def canPartition(self, nums: list[int]) -> bool:  # noqa: N802
        total_sum = sum(nums)
        subset_target = total_sum // 2
        if total_sum % 2 == 1:
            return False

        dp = [True] + [False] * subset_target
        for num in nums:
            for i in range(subset_target, num - 1, -1):
                dp[i] |= dp[i - num]
        return dp[-1]


solution = Solution()


nums = [1, 5, 11, 5]
assert solution.canPartition(nums)

nums = [1, 2, 3, 5]
assert not solution.canPartition(nums)

nums = [1, 1, 1, 5, 11, 5]
assert solution.canPartition(nums)
