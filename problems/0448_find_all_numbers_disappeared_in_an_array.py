# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# 448. Find All Numbers Disappeared in an Array


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:  # noqa: N802
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
        return [i for i in range(1, len(nums) + 1) if nums[i - 1] > 0]


solution = Solution()


nums = [4, 3, 2, 7, 8, 2, 3, 1]
assert solution.findDisappearedNumbers(nums) == [5, 6]

nums = [1, 1]
assert solution.findDisappearedNumbers(nums) == [2]
