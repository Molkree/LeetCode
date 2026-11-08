# https://leetcode.com/problems/maximum-subarray/
# 53. Maximum Subarray


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:  # noqa: N802
        max_sum = nums[0]
        current_sum = nums[0]
        for x in nums[1:]:
            current_sum = max(x, current_sum + x)
            max_sum = max(max_sum, current_sum)
        return max_sum


solution = Solution()

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
assert solution.maxSubArray(nums) == 6

nums = [1]
assert solution.maxSubArray(nums) == 1

nums = [5, 4, -1, 7, 8]
assert solution.maxSubArray(nums) == 23
