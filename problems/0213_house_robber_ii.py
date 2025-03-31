# https://leetcode.com/problems/house-robber-ii/
# 213. House Robber II


class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_non_circular(nums: list[int]) -> int:
            if len(nums) == 1:
                return nums[0]
            prev_prev = nums[0]
            prev = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                cur = max(prev, nums[i] + prev_prev)
                prev_prev = prev
                prev = cur
            return prev

        return max(rob_non_circular(nums[:-1]), rob_non_circular(nums[1:]))


solution = Solution()


nums = [2, 3, 2]
assert solution.rob(nums) == 3

nums = [1, 2, 3, 1]
assert solution.rob(nums) == 4

nums = [1, 2, 3]
assert solution.rob(nums) == 3

nums = [0]
assert solution.rob(nums) == 0
