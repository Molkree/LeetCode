# https://leetcode.com/problems/majority-element/
# 169. Majority Element


class Solution:
    def majorityElement(self, nums: list[int]) -> int:  # noqa: N802
        weight = 0
        majority_element = nums[0]
        for num in nums:
            if num == majority_element:
                weight += 1
            else:
                weight -= 1
            if weight == 0:
                majority_element = num
                weight = 1
        return majority_element


solution = Solution()

nums = [3, 2, 3]
assert 3 == solution.majorityElement(nums)

nums = [2, 2, 1, 1, 1, 2, 2]
assert 2 == solution.majorityElement(nums)
