# https://leetcode.com/problems/house-robber/
# 198. House Robber


class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev_prev = nums[0]
        prev = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            cur = max(prev, nums[i] + prev_prev)
            prev_prev = prev
            prev = cur
        return prev


solution = Solution()


nums = [1, 2, 3, 1]
assert solution.rob(nums) == 4

nums = [2, 7, 9, 3, 1]
assert solution.rob(nums) == 12

nums = [10, 0, 0, 10]
assert solution.rob(nums) == 20

nums = [0]
assert solution.rob(nums) == 0
