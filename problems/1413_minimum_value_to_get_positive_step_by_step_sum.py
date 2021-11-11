# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
# 1413. Minimum Value to Get Positive Step by Step Sum


class Solution:
    def minStartValue(self, nums: list[int]) -> int:  # noqa: N802
        min_sum = 0
        cur_sum = 0
        for num in nums:
            cur_sum += num
            min_sum = min(min_sum, cur_sum)
        return max(0, -min_sum) + 1


solution = Solution()


nums = [-3, 2, -3, 4, 2]
assert solution.minStartValue(nums) == 5

nums = [1, 2]
assert solution.minStartValue(nums) == 1

nums = [1, -2, -3]
assert solution.minStartValue(nums) == 5
