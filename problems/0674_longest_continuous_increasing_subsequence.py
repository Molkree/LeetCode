# https://leetcode.com/problems/longest-continuous-increasing-subsequence/
# 674. Longest Continuous Increasing Subsequence


class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:  # noqa: N802
        lcis = 1
        max_lcis = 1
        for i, num in enumerate(nums[:-1]):
            if num < nums[i + 1]:
                lcis += 1
            else:
                max_lcis = max(max_lcis, lcis)
                lcis = 1
        return max(max_lcis, lcis)


solution = Solution()


nums = [1, 3, 5, 4, 7]
assert solution.findLengthOfLCIS(nums) == 3

nums = [2, 2, 2, 2, 2]
assert solution.findLengthOfLCIS(nums) == 1
